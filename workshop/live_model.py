"""Load the live LangChain Gemini adapter from the learner's local .env."""

from pathlib import Path

from dotenv import load_dotenv

from agentforge_jarvis.engine import final_text
from agentforge_jarvis.providers import Settings, make_model, public_error


def workshop_model():
    load_dotenv(Path.cwd() / ".env", override=False)
    settings = Settings.from_env()
    if settings.provider != "gemini":
        raise ValueError(
            "Select AGENTFORGE_PROVIDER=gemini in your local .env for the live workshop."
        )
    return make_model(settings, "finance")


def run_lab(agent):
    """Show executed evidence and an approachable, redacted provider error."""
    import sys

    from langchain_core.messages import ToolMessage

    try:
        result = agent.invoke(
            {"messages": [{"role": "user", "content": "Check the launch budget."}]},
            {"recursion_limit": 12},
        )
        evidence = [m for m in result["messages"] if isinstance(m, ToolMessage)]
        if not evidence or any(m.status == "error" for m in evidence):
            print("LAB INCOMPLETE: check both calculations and confirm the cash tool succeeded.")
            sys.exit(1)
        for message in evidence:
            print("EXECUTED TOOL:", message.name, message.content)
        print("GEMINI RESPONSE:", final_text(result["messages"][-1]))
    except Exception as error:
        print("LIVE REQUEST FAILED:", public_error(error))
        sys.exit(1)
