import pytest
from fastapi.testclient import TestClient

from agentforge_jarvis.catalog import AGENTS
from agentforge_jarvis.checkpoint_agent import role_contract, run_checkpoint_agent
from agentforge_jarvis.checkpoint_app import app
from agentforge_jarvis.checkpoint_tools import CHECKPOINT_TOOLS, run_checkpoint_tool


def test_checkpoint_domains_and_tool_names_match_complete_application():
    assert set(CHECKPOINT_TOOLS) == set(AGENTS)
    assert "general-management" in CHECKPOINT_TOOLS
    assert "management" not in CHECKPOINT_TOOLS
    for domain, function in CHECKPOINT_TOOLS.items():
        assert function.__name__ == AGENTS[domain]["tool"]


def test_checkpoint_finance_tool_and_edge_case():
    result = run_checkpoint_tool(
        "finance", {"price": 120, "unit_cost": 65, "fixed_cost": 240000, "budget": 2400000}
    )
    assert result["break_even_units"] == 4364
    with pytest.raises(ValueError):
        run_checkpoint_tool(
            "finance", {"price": 60, "unit_cost": 65, "fixed_cost": 240000, "budget": 2400000}
        )


def test_checkpoint_agent_executes_the_required_langchain_tool():
    result = run_checkpoint_agent(
        "finance", {"price": 120, "unit_cost": 65, "fixed_cost": 240000, "budget": 2400000}
    )
    assert result["tool_name"] == "model_finances"
    assert result["tool_result"]["break_even_units"] == 4364
    assert result["human_review_required"] is True
    assert "human" in result["explanation"].lower()
    assert "Commercial Scenario Analyst" in role_contract("finance")


def test_checkpoint_interface_uses_the_same_agent_service():
    client = TestClient(app)
    assert client.get("/api/health").json() == {"status": "ok", "checkpoint": 2}
    response = client.post(
        "/api/checkpoint",
        json={
            "domain": "general-management",
            "payload": {
                "budget": "PASS",
                "capacity": "REVIEW",
                "evidence": "PASS",
                "owner": "Student lead",
            },
        },
    )
    assert response.status_code == 200
    assert response.json()["tool_name"] == "synthesize_strategy"
