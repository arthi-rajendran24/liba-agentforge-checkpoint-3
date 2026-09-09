from fastapi.testclient import TestClient

from agentforge_jarvis.checkpoint_agent import role_contract, run_checkpoint_agent
from agentforge_jarvis.checkpoint_app import app


def test_langchain_agent_executes_the_catalogued_tool():
    result = run_checkpoint_agent(
        "finance", {"price": 120, "unit_cost": 65, "fixed_cost": 240000, "budget": 2400000}
    )
    assert result["tool_name"] == "model_finances"
    assert result["tool_result"]["break_even_units"] == 4364
    assert result["human_review_required"] is True
    assert "Commercial Scenario Analyst" in role_contract("finance")


def test_fastapi_interface_calls_the_same_agent_service():
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
