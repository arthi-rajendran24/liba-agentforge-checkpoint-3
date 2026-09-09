import pytest

from agentforge_jarvis.catalog import AGENTS
from agentforge_jarvis.checkpoint_tools import CHECKPOINT_TOOLS, run_checkpoint_tool


def test_domains_and_tool_names_match_complete_agentforge():
    assert set(CHECKPOINT_TOOLS) == set(AGENTS)
    assert "general-management" in CHECKPOINT_TOOLS
    assert "management" not in CHECKPOINT_TOOLS
    for domain, function in CHECKPOINT_TOOLS.items():
        assert function.__name__ == AGENTS[domain]["tool"]


def test_finance_tool_and_edge_case():
    result = run_checkpoint_tool(
        "finance", {"price": 120, "unit_cost": 65, "fixed_cost": 240000, "budget": 2400000}
    )
    assert result["break_even_units"] == 4364
    with pytest.raises(ValueError):
        run_checkpoint_tool(
            "finance", {"price": 60, "unit_cost": 65, "fixed_cost": 240000, "budget": 2400000}
        )


def test_management_uses_the_canonical_identifier():
    result = run_checkpoint_tool(
        "general-management",
        {"budget": "PASS", "capacity": "REVIEW", "evidence": "PASS", "owner": "Lead"},
    )
    assert result["blockers"] == ["capacity"]
    assert result["human_approval_required"] is True
