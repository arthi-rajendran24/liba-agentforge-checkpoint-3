import threading
import time

import pytest
from langchain_core.language_models.fake_chat_models import FakeListChatModel
from pydantic import ValidationError

from agentforge_jarvis.business import analyze
from agentforge_jarvis.catalog import AGENTS
from agentforge_jarvis.engine import Cancelled, Engine, validate_package
from agentforge_jarvis.models import ChatRequest, RunRequest, Scenario, apply_challenge
from agentforge_jarvis.providers import Settings, make_model
from agentforge_jarvis.storage import Store


@pytest.fixture
def engine(tmp_path):
    value = Engine(Store(tmp_path), Settings())
    yield value
    value.close()


def graph(engine, challenge="baseline", **kwargs):
    events = []
    reports = engine.graph(
        RunRequest(challenge=challenge, **kwargs),
        lambda kind, **payload: events.append({"kind": kind, **payload}),
        threading.Event(),
    )
    return reports, events


@pytest.mark.parametrize(
    "challenge, decision",
    [
        ("baseline", "CONDITIONAL GO"),
        ("budget-cut", "HOLD"),
        ("supply-delay", "HOLD"),
        ("sentiment-shift", "HOLD"),
        ("demand-surge", "HOLD"),
    ],
)
def test_six_real_langchain_agents_and_challenge_gates(engine, challenge, decision):
    reports, events = graph(engine, challenge)
    assert set(reports) == set(AGENTS)
    assert reports["general-management"].metrics["decision"] == decision
    assert all(x["passed"] for x in validate_package(reports))
    for domain, r in reports.items():
        assert r.tools_called == ["read_brief", AGENTS[domain]["tool"], "search_memory"]
        assert r.narrative and r.evidence and r.assumptions
    starts = [e["domain"] for e in events if e["kind"] == "agent_started"]
    assert starts.index("finance") > starts.index("hr")
    assert starts[-1] == "general-management"
    assert len([e for e in events if e["kind"] == "tool_completed"]) == 18


def test_budget_cut_arithmetic_and_nonmutation(engine):
    source = Scenario()
    reduced = apply_challenge(source, "budget-cut")
    assert source.budget == 2400000
    assert reduced.budget == 1800000
    reports, _ = graph(engine, "budget-cut", scenario=source)
    finance = reports["finance"].metrics
    assert finance["cash_required_inr"] == 2400000
    assert finance["funding_gap_inr"] == 600000
    assert finance["gross_margin_pct"] == 45.83
    assert finance["break_even_units"] == 8182


def test_supplier_delay_limits_finance_revenue(engine):
    reports, _ = graph(engine, "supply-delay")
    assert reports["operations"].metrics["shortfall_units"] == 600
    base = reports["finance"].details[1]
    assert base["sold_units"] == 29400
    assert base["revenue_inr"] == 3528000


def test_specialist_runs_include_dependencies(engine):
    reports, _ = graph(engine, domain="marketing")
    assert set(reports) == {"analytics", "marketing"}
    assert any("analytics hand-off" in e for e in reports["marketing"].evidence)


def test_hr_review_uses_skills_only_and_handles_empty_skills():
    report = analyze("hr", Scenario(), {})
    assert report.details[0]["candidate_id"] == "C-101"
    assert all(x["decision"] == "Human review required" for x in report.details)
    assert "does not establish fairness" in " ".join(report.risks)
    no_skills = analyze("hr", Scenario(required_skills=[]), {})
    assert any("No required skills" in risk for risk in no_skills.risks)
    bad = Scenario().model_dump()
    bad["candidates"][0]["gender"] = "must not be ingested"
    with pytest.raises(ValidationError):
        Scenario.model_validate(bad)


def test_invalid_inputs_and_zero_contribution():
    with pytest.raises(ValidationError):
        Scenario(budget=float("nan"))
    s = Scenario()
    s.signals[0].positive = 9999
    with pytest.raises(ValueError, match="Positive responses"):
        apply_challenge(s, "baseline")
    result = analyze("finance", Scenario(price=65), {})
    assert result.metrics["break_even_units"] == "Not achievable"
    assert result.status == "hold"


def test_team_memory_and_agent_conversation_isolation(engine):
    engine.store.add_note(
        "alpha",
        "Packaging decisions",
        "The pack colour is teal. The fictional allergen review belongs to Mei.",
    )
    engine.store.add_note("beta", "Packaging decisions", "Private beta note")
    result = engine.chat(
        ChatRequest(team="alpha", message="What do our memory notes say about the pack colour?")
    )
    assert "teal" in result["answer"]
    assert "Private beta" not in result["answer"]
    assert engine.store.messages("beta", "supervisor") == []
    assert len(engine.store.messages("alpha", "supervisor")) == 2
    assert engine.store.messages("alpha", "finance") == []
    engine.chat(ChatRequest(team="alpha", domain="hr", message="Review staffing"))
    second = engine.chat(
        ChatRequest(team="alpha", domain="hr", message="Show the work sample evidence")
    )
    assert (
        len([e for e in second["events"] if e["kind"] == "agent_started" and e["domain"] == "hr"])
        == 1
    )
    assert len(engine.store.messages("alpha", "hr")) == 4


def test_no_live_fallback_when_configuration_missing(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    with pytest.raises(ValueError, match="GEMINI_API_KEY"):
        make_model(Settings("gemini", "example-model"), "finance")


def test_agent_without_required_tool_cannot_publish(engine, monkeypatch):
    class NoToolsModel(FakeListChatModel):
        def bind_tools(self, tools, **kwargs):
            return self

    monkeypatch.setattr(
        "agentforge_jarvis.engine.make_model",
        lambda *args: NoToolsModel(responses=["Invented approval"]),
    )
    with pytest.raises(RuntimeError, match="required evidence tool"):
        graph(engine)


def test_cancelled_graph_stops_before_agent_execution(engine):
    flag = threading.Event()
    flag.set()
    with pytest.raises(Cancelled):
        engine.graph(RunRequest(), lambda *a, **kw: None, flag)


def test_persisted_failure_is_explicit_and_redacted(engine, monkeypatch):
    def fail(*args, **kwargs):
        raise RuntimeError("example-api-secret-should-never-leak")

    monkeypatch.setattr(engine, "graph", fail)
    run = engine.start_run(RunRequest(team="failure-test"))
    for _ in range(100):
        saved = engine.store.get_run(run["id"], "failure-test")
        if saved["status"] == "failed":
            break
        time.sleep(0.01)
    assert saved["status"] == "failed"
    assert saved["reports"] == {}
    assert "example-api-secret" not in saved["error"]
    assert "No automatic fallback" in saved["error"]
