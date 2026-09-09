from __future__ import annotations

import json
from pathlib import Path

import streamlit as st

from agentforge.channel import word_stream
from agentforge.evidence import extract_image, reviewed_evidence, validate_image
from agentforge.memory import save_approved
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

st.set_page_config(page_title="AgentForge Checkpoint 3", layout="centered")
st.title("AgentForge Checkpoint 3")
st.caption("Shared agent service, reviewed evidence, approved memory and optional channels")
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
        st.write_stream(word_stream(result["explanation"]))
        st.warning("Human review is still required.")
    except (json.JSONDecodeError, TypeError, ValueError, RuntimeError) as exc:
        st.error(str(exc))

st.divider()
st.subheader("Review image evidence")
upload = st.file_uploader("Fictional PNG or JPEG under 2 MB", type=["png", "jpg", "jpeg"])
if upload is not None:
    data = upload.getvalue()
    content_type = upload.type or ""
    try:
        validate_image(content_type, len(data))
        st.image(data, caption=upload.name)
        if st.button("Extract visible text with Gemini"):
            st.session_state["extracted"] = extract_image(data, content_type)
        extracted = st.text_area("Initial extraction", st.session_state.get("extracted", ""))
        corrected = st.text_area("Corrected text")
        uncertainty = st.text_input("Uncertainty or unclear fields")
        approved = st.checkbox("I reviewed this evidence and approve saving it")
        if st.button("Save approved evidence"):
            record = reviewed_evidence(upload.name, extracted, corrected, uncertainty, approved)
            save_approved(
                path=Path("memory.json"),
                summary=record["text"],
                source=record["source"],
                uncertainty=record["uncertainty"],
                approved=record["approved"],
            )
            st.success("Approved evidence saved locally.")
    except (PermissionError, TypeError, ValueError, RuntimeError) as exc:
        st.error(str(exc))
