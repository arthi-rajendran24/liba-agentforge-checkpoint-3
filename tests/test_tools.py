import pytest

from agentforge.tools import (
    analytics_conversion,
    finance_break_even,
    hr_skills_gap,
    management_gate,
    marketing_allocation,
    operations_capacity,
)


def test_finance_normal_and_edge():
    result = finance_break_even(120, 65, 240000, 2400000)
    assert result["break_even_units"] == 4364
    with pytest.raises(ValueError):
        finance_break_even(60, 65, 240000, 2400000)


def test_marketing_exact_total_and_invalid_weights():
    result = marketing_allocation(180000, {"organic": 50, "paid": 30, "partner": 20})
    assert sum(result["allocation"].values()) == 180000
    with pytest.raises(ValueError):
        marketing_allocation(180000, {"organic": 70, "paid": 20})


def test_operations_changed_condition():
    result = operations_capacity(30000, 400, 21, 84)
    assert result["status"] == "REVIEW"
    assert result["shortfall_units"] == 4800


def test_analytics_denominator_guard():
    with pytest.raises(ValueError):
        analytics_conversion(0, 0, 5.0)


def test_hr_returns_missing_skills_without_ranking_people():
    result = hr_skills_gap(["Python", "SQL"], ["SQL"], 10)
    assert result["missing_skills"] == ["Python"]
    assert result["human_review"] is True


def test_management_requires_named_owner():
    with pytest.raises(ValueError):
        management_gate("PASS", "PASS", "PASS", "")
