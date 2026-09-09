import threading

import pytest
from fastapi.testclient import TestClient

from agentforge_jarvis.app import create_app
from agentforge_jarvis.engine import Engine
from agentforge_jarvis.models import RunRequest
from agentforge_jarvis.providers import Settings, public_error
from agentforge_jarvis.security import BusyError, RateLimiter, TeamAuth
from agentforge_jarvis.storage import Store


def test_authenticated_team_cannot_read_or_write_other_team(tmp_path, monkeypatch):
    monkeypatch.setenv("AGENTFORGE_AUTH_REQUIRED", "true")
    auth = TeamAuth(Store(tmp_path))
    auth.provision("alpha", "a-very-long-access-code")
    auth.provision("beta", "another-long-access-code")
    with TestClient(create_app(tmp_path, Settings())) as c:
        assert c.get("/api/bootstrap?team=alpha").status_code == 401
        assert (
            c.post("/api/auth/login", json={"team": "alpha", "password": "wrong"}).status_code
            == 401
        )
        response = c.post(
            "/api/auth/login", json={"team": "alpha", "password": "a-very-long-access-code"}
        )
        assert response.status_code == 200
        assert (
            "HttpOnly" in response.headers["set-cookie"]
            and "SameSite=strict" in response.headers["set-cookie"]
        )
        assert c.get("/api/bootstrap?team=alpha").status_code == 200
        assert c.get("/api/bootstrap?team=beta").status_code == 403
        assert c.get("/api/bootstrap").status_code == 403
        assert (
            c.post("/api/notes", json={"team": "beta", "title": "x", "text": "y"}).status_code
            == 403
        )
        assert c.post("/api/runs", json={}).status_code == 403
        assert c.post("/api/auth/logout").status_code == 200
        assert c.get("/api/bootstrap?team=alpha").status_code == 401


def test_rotation_revokes_sessions_and_passwords_are_hashed(tmp_path):
    store = Store(tmp_path)
    auth = TeamAuth(store)
    auth.provision("alpha", "private-secret")
    token = auth.login("alpha", "private-secret")
    assert auth.team(token) == "alpha"
    with store.connection() as db:
        row = db.execute("SELECT digest FROM credentials").fetchone()
        assert "private-secret" not in row["digest"]
        db.execute("UPDATE sessions SET expires=0")
    assert auth.team(token) is None
    auth.provision("alpha", "new-secret")
    assert auth.login("alpha", "private-secret") is None
    assert auth.login("alpha", "new-secret")


def test_team_admission_prevents_duplicate_live_spend(tmp_path, monkeypatch):
    e = Engine(Store(tmp_path), Settings())
    gate = threading.Event()
    monkeypatch.setattr(e, "graph", lambda *a, **kw: gate.wait(2) or {})
    try:
        e.start_run(RunRequest(team="alpha"))
        with pytest.raises(BusyError):
            e.start_run(RunRequest(team="alpha"))
    finally:
        gate.set()
        e.close()


def test_rate_limit_bounded_and_errors_do_not_leak():
    limiter = RateLimiter(2, 60, 3)
    assert limiter.allow("x") and limiter.allow("x") and not limiter.allow("x")
    for i in range(10):
        limiter.allow(str(i))
    assert len(limiter.entries) == 3
    assert "secret-key" not in public_error(RuntimeError("429 secret-key quota"))
    assert "quota" in public_error(RuntimeError("429 secret-key quota"))


def test_production_rejects_rehearsal(tmp_path, monkeypatch):
    monkeypatch.setenv("AGENTFORGE_ENV", "production")
    with pytest.raises(ValueError):
        create_app(tmp_path, Settings())


def test_partial_reports_survive_a_later_failure(tmp_path, monkeypatch):
    e = Engine(Store(tmp_path), Settings())
    original = e.domain_agent

    def fail_later(domain, *args, **kwargs):
        if domain == "marketing":
            raise RuntimeError("provider unavailable")
        return original(domain, *args, **kwargs)

    monkeypatch.setattr(e, "domain_agent", fail_later)
    try:
        run = e.start_run(RunRequest(team="checkpoint"))
        for _ in range(100):
            saved = e.store.get_run(run["id"], "checkpoint")
            if saved["status"] == "failed":
                break
            threading.Event().wait(0.01)
        assert saved["status"] == "failed"
        assert "analytics" in saved["reports"]
        assert "marketing" not in saved["reports"]
    finally:
        e.close()


def test_image_validation_happens_before_provider_call(tmp_path):
    from agentforge_jarvis.media import extract_image

    e = Engine(Store(tmp_path), Settings("gemini", "test"))
    try:
        with pytest.raises(ValueError, match="base64"):
            extract_image(e, "alpha", "not-base64!", "image/png")
        with pytest.raises(ValueError, match="format"):
            extract_image(e, "alpha", "aGVsbG8=", "image/png")
        assert not e.active_teams
    finally:
        e.close()


def test_gemini_agents_share_one_request_budget(monkeypatch):
    from agentforge_jarvis.providers import Settings, gemini_limiter, make_model

    monkeypatch.setenv("GEMINI_API_KEY", "fictional-test-key")
    monkeypatch.setenv("AGENTFORGE_GEMINI_RPM", "12")
    a = make_model(Settings("gemini", "gemini-3.1-flash-lite"), "analytics")
    b = make_model(Settings("gemini", "gemini-3.1-flash-lite"), "finance")
    assert a.rate_limiter is b.rate_limiter is gemini_limiter()
    assert a.rate_limiter.requests_per_second == 0.2
    monkeypatch.setenv("AGENTFORGE_GEMINI_RPM", "nan")
    assert "between 1 and 6000" in Settings("gemini", "test").error()
