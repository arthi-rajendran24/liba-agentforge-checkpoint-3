import pytest

from agentforge.student_adapter import run_student_tool


def test_adapter_preserves_student_tool_result():
    result = run_student_tool(
        "finance", {"price": 120, "unit_cost": 65, "fixed_cost": 240000, "budget": 2400000}
    )
    assert result["break_even_units"] == 4364


def test_adapter_rejects_unknown_domain():
    with pytest.raises(ValueError):
        run_student_tool("unknown", {})
