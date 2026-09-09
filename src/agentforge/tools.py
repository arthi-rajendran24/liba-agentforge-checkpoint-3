from __future__ import annotations

import math


def finance_break_even(price: float, unit_cost: float, fixed_cost: float, budget: float) -> dict:
    values = [price, unit_cost, fixed_cost, budget]
    if any(value < 0 for value in values):
        raise ValueError("Values cannot be negative")
    contribution = price - unit_cost
    if contribution <= 0:
        raise ValueError("Price must exceed unit cost")
    units = math.ceil(fixed_cost / contribution)
    required_cash = fixed_cost + units * unit_cost
    return {
        "contribution_per_unit": contribution,
        "break_even_units": units,
        "required_cash": required_cash,
        "funding_gap": max(0.0, required_cash - budget),
    }


def marketing_allocation(budget: float, weights: dict[str, float]) -> dict:
    if budget < 0 or not weights:
        raise ValueError("Budget and weights must be valid")
    if any(weight < 0 for weight in weights.values()) or abs(sum(weights.values()) - 100) > 1e-9:
        raise ValueError("Weights must be non-negative and total 100")
    allocation = {name: round(budget * weight / 100, 2) for name, weight in weights.items()}
    allocation[next(iter(allocation))] += round(budget - sum(allocation.values()), 2)
    return {"budget": budget, "allocation": allocation}


def operations_capacity(units: int, units_per_day: int, lead_days: int, deadline_days: int) -> dict:
    if units < 0 or lead_days < 0 or deadline_days < 0 or units_per_day <= 0:
        raise ValueError("Capacity inputs are invalid")
    production_days = math.ceil(units / units_per_day)
    total_days = lead_days + production_days
    producible = max(0, deadline_days - lead_days) * units_per_day
    return {
        "production_days": production_days,
        "total_days": total_days,
        "shortfall_units": max(0, units - producible),
        "status": "PASS" if total_days <= deadline_days else "REVIEW",
    }


def analytics_conversion(visits: int, conversions: int, prior_rate: float) -> dict:
    if visits <= 0 or conversions < 0 or conversions > visits:
        raise ValueError("Analytics counts are invalid")
    rate = conversions / visits * 100
    return {
        "conversion_rate": round(rate, 2),
        "change_points": round(rate - prior_rate, 2),
        "sample_visits": visits,
    }


def hr_skills_gap(required: list[str], covered: list[str], learning_hours: int) -> dict:
    if learning_hours < 0 or not required:
        raise ValueError("HR inputs are invalid")
    missing = sorted(set(required) - set(covered))
    return {
        "required_count": len(set(required)),
        "missing_skills": missing,
        "learning_hours": learning_hours,
        "human_review": True,
    }


def management_gate(budget: str, capacity: str, evidence: str, owner: str) -> dict:
    values = {"budget": budget, "capacity": capacity, "evidence": evidence}
    statuses = {value.upper() for value in values.values()}
    if statuses - {"PASS", "REVIEW", "FAIL"} or not owner.strip():
        raise ValueError("Gate inputs or owner are invalid")
    blockers = [name for name, value in values.items() if value.upper() != "PASS"]
    return {
        "recommendation": "PROCEED" if not blockers else "REVIEW",
        "blockers": blockers,
        "decision_owner": owner,
        "human_approval_required": True,
    }
