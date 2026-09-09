from __future__ import annotations

import json

import streamlit as st

from agentforge.service import answer

EXAMPLES = {
    "finance": {"price": 120, "unit_cost": 65, "fixed_cost": 240000, "budget": 2400000},
    "marketing": {"budget": 180000, "weights": {"organic": 50, "paid": 30, "partner": 20}},
    "operations": {"units": 30000, "units_per_day": 600, "lead_days": 21, "deadline_days": 84},
    "analytics": {"visits": 1000, "conversions": 48, "prior_rate": 4.2},
    "hr": {"required": ["Python", "SQL"], "covered": ["SQL"], "learning_hours": 10},
    "management": {
        "budget": "PASS",
        "capacity": "REVIEW",
        "evidence": "PASS",
        "owner": "Student lead",
    },
}

st.set_page_config(page_title="AgentForge Checkpoint 2", layout="centered")
st.title("AgentForge Checkpoint 2")
st.caption("Your deterministic tool, one shared service, optional Gemini explanation")
domain = st.selectbox("Specialization", list(EXAMPLES))
payload_text = st.text_area(
    "Fictional input as JSON", json.dumps(EXAMPLES[domain], indent=2), height=220
)
live = st.toggle("Use one live Gemini request", value=False)
if st.button("Run agent"):
    try:
        result = answer(domain, json.loads(payload_text), live=live)
        st.subheader("Executed deterministic tool")
        st.json(result["tool_result"])
        st.subheader("Agent explanation")
        st.write(result["explanation"])
        st.warning("Human review is still required.")
    except (json.JSONDecodeError, TypeError, ValueError, RuntimeError) as exc:
        st.error(str(exc))
