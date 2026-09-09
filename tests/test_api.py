import time

from fastapi.testclient import TestClient

from agentforge_jarvis.app import create_app
from agentforge_jarvis.models import Scenario
from agentforge_jarvis.providers import Settings


def wait_run(client, run_id, team="test-team"):
    for _ in range(200):
        run = client.get(f"/api/runs/{run_id}?team={team}").json()
        if run["status"] not in {"queued", "running"}:
            return run
        time.sleep(0.02)
    raise AssertionError("Run did not complete")


def test_run_stream_export_assessment_and_persistence(tmp_path):
    with TestClient(create_app(tmp_path, Settings())) as client:
        assert client.get("/").status_code == 200
        assert client.get("/static/app.js").status_code == 200
        boot = client.get("/api/bootstrap?team=test-team").json()
        assert len(boot["agents"]) == 6
        start = client.post("/api/runs", json={"team": "test-team", "challenge": "budget-cut"})
        assert start.status_code == 202
        run_id = start.json()["id"]
        run = wait_run(client, run_id)
        assert run["status"] == "completed", run
        assert len(run["reports"]) == 6
        stream = client.get(f"/api/runs/{run_id}/events?team=test-team")
        assert "tool_completed" in stream.text and "event: done" in stream.text
        assert client.get(f"/api/runs/{run_id}?team=other-team").status_code == 404
        assert client.get(f"/api/runs/{run_id}/events?team=other-team").status_code == 404
        score = client.post(
            f"/api/runs/{run_id}/assessment",
            json={
                "team": "test-team",
                "scores": [5, 4, 3, 4, 5],
                "reflection": "We inspected the INR 600,000 budget gap and held the launch.",
            },
        )
        assert score.status_code == 200
        assert score.json()["weighted_total"] == 84
        md = client.get(f"/api/runs/{run_id}/export?team=test-team&format=md")
        assert md.status_code == 200
        for expected in [
            "PRISM",
            "PULSE",
            "NOVA",
            "ATLAS",
            "LEDGER",
            "JARVIS",
            "600000",
            "Facilitator assessment",
        ]:
            assert expected in md.text
        assert client.get(f"/api/runs/{run_id}/export?team=other-team").status_code == 404
        exported = client.get(f"/api/runs/{run_id}/export?team=test-team&format=json").json()
        assert exported["assessment"]["weighted_total"] == 84
    with TestClient(create_app(tmp_path, Settings())) as client:
        assert client.get(f"/api/runs/{run_id}?team=test-team").json()["status"] == "completed"


def test_notes_blueprint_and_chat_are_persistent_and_team_scoped(tmp_path):
    with TestClient(create_app(tmp_path, Settings())) as client:
        result = client.post(
            "/api/notes",
            json={
                "team": "test-team",
                "title": "Launch owners",
                "text": "The customer research owner is Mira. <script>alert(1)</script>",
            },
        )
        assert result.status_code == 201
        note_id = result.json()["id"]
        assert client.get("/api/bootstrap?team=other-team").json()["notes"] == []
        assert (
            client.put(
                "/api/agents/hr/blueprint",
                json={"team": "test-team", "instructions": "Explain skills coverage clearly."},
            ).status_code
            == 200
        )
        chat = client.post(
            "/api/chat",
            json={
                "team": "test-team",
                "message": "What do the memory notes say about the research owner?",
            },
        )
        assert chat.status_code == 200, chat.text
        assert "Mira" in chat.json()["answer"]
        assert len(client.get("/api/messages?team=test-team").json()) == 2
        assert client.get("/api/messages?team=other-team").json() == []
        client.delete(f"/api/notes/{note_id}?team=other-team")
        assert len(client.get("/api/bootstrap?team=test-team").json()["notes"]) == 1
    with TestClient(create_app(tmp_path, Settings())) as client:
        boot = client.get("/api/bootstrap?team=test-team").json()
        assert (
            next(a for a in boot["agents"] if a["id"] == "hr")["instructions"]
            == "Explain skills coverage clearly."
        )
        assert len(boot["notes"]) == 1
        client.delete(f"/api/notes/{note_id}?team=test-team")
        assert client.get("/api/bootstrap?team=test-team").json()["notes"] == []


def test_input_boundaries_origin_host_and_invalid_scores(tmp_path):
    with TestClient(create_app(tmp_path, Settings())) as client:
        assert client.post("/api/runs", json={"team": "../escape"}).status_code == 422
        assert client.post("/api/runs", json={"domain": "imaginary"}).status_code == 422
        assert (
            client.post(
                "/api/runs", json={}, headers={"Origin": "https://malicious.example"}
            ).status_code
            == 403
        )
        assert client.get("/api/health", headers={"Host": "malicious.example"}).status_code == 400
        assert client.post("/api/notes", content="x" * 200001).status_code == 413
        scenario = Scenario().model_dump()
        scenario["signals"][0]["positive"] = 999999
        assert client.post("/api/scenario/validate", json=scenario).status_code == 400
        scenario = Scenario().model_dump()
        scenario["candidates"][0]["age"] = 25
        assert client.post("/api/scenario/validate", json=scenario).status_code == 422
        health = client.get("/api/health")
        assert "frame-ancestors 'none'" in health.headers["content-security-policy"]
        assert "GEMINI_API_KEY" not in health.text


def test_missing_live_configuration_is_not_simulated(tmp_path, monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    with TestClient(create_app(tmp_path, Settings("gemini", "test-model"))) as client:
        assert not client.get("/api/health").json()["configured"]
        response = client.post("/api/runs", json={})
        assert response.status_code == 400
        assert client.get("/api/runs?team=liba-team-01").json() == []
