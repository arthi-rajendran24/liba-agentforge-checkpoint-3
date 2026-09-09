from __future__ import annotations

import json
import os
from collections.abc import Callable

from .contracts import contract_for
from .student_adapter import run_student_tool

Explainer = Callable[[str, dict], str]


def rehearsal_answer(domain: str, payload: dict) -> dict:
    tool_result = run_student_tool(domain, payload)
    return {
        "mode": "rehearsal",
        "domain": domain,
        "tool_result": tool_result,
        "explanation": "Offline result verified. A live model explanation has not been checked.",
        "human_review_required": True,
    }


def _gemini_explainer(contract: str, tool_result: dict) -> str:
    key = os.getenv("GEMINI_API_KEY", "")
    if not key:
        raise RuntimeError("GEMINI_API_KEY is not configured")
    model = os.getenv("AGENTFORGE_MODEL", "gemini-3.1-flash-lite")
    from langchain_google_genai import ChatGoogleGenerativeAI

    llm = ChatGoogleGenerativeAI(model=model, google_api_key=key, temperature=0)
    message = llm.invoke(f"{contract}\nTool result:\n{json.dumps(tool_result)}")
    return str(message.content)


def live_answer(domain: str, payload: dict, explainer: Explainer | None = None) -> dict:
    tool_result = run_student_tool(domain, payload)
    explanation = (explainer or _gemini_explainer)(contract_for(domain), tool_result)
    return {
        "mode": "live",
        "domain": domain,
        "tool_result": tool_result,
        "explanation": explanation,
        "human_review_required": True,
    }


def answer(
    domain: str, payload: dict, *, live: bool = False, explainer: Explainer | None = None
) -> dict:
    return live_answer(domain, payload, explainer) if live else rehearsal_answer(domain, payload)
