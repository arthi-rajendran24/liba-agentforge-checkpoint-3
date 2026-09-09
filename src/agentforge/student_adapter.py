from __future__ import annotations

from collections.abc import Callable

from .tools import (
    analytics_conversion,
    finance_break_even,
    hr_skills_gap,
    management_gate,
    marketing_allocation,
    operations_capacity,
)

Tool = Callable[..., dict]

TOOL_REGISTRY: dict[str, Tool] = {
    "finance": finance_break_even,
    "marketing": marketing_allocation,
    "operations": operations_capacity,
    "analytics": analytics_conversion,
    "hr": hr_skills_gap,
    "management": management_gate,
}


def run_student_tool(domain: str, payload: dict) -> dict:
    """The only compatibility seam Antigravity should adapt for a student's Checkpoint 1."""
    try:
        tool = TOOL_REGISTRY[domain]
    except KeyError as exc:
        raise ValueError(f"Unsupported domain: {domain}") from exc
    result = tool(**payload)
    if not isinstance(result, dict):
        raise TypeError("A student tool must return a dictionary")
    return result
