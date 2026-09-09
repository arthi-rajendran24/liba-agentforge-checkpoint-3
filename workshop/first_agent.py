"""Completed first-agent lab: run with uv run python workshop/first_agent.py."""

from langchain.agents import create_agent
from langchain_core.tools import tool
from rehearsal_model import WorkshopModel

# Fictional inputs. Change one value at a time.
BUDGET = 2_400_000
UNITS = 30_000
UNIT_COST = 65
OTHER_LAUNCH_COSTS = 450_000


@tool
def estimate_launch_cash() -> dict:
    """Calculate cash needed for the fictional launch and compare it with the budget."""
    cash_needed = UNITS * UNIT_COST + OTHER_LAUNCH_COSTS
    funding_gap = max(0, cash_needed - BUDGET)
    return {
        "cash_needed_inr": cash_needed,
        "funding_gap_inr": funding_gap,
        "recommendation": "HOLD" if funding_gap > 0 else "REVIEW WITH A HUMAN",
    }


agent = create_agent(
    model=WorkshopModel(),
    tools=[estimate_launch_cash],
    system_prompt="You are a finance assistant. Use the cash tool. A human decides.",
)

if __name__ == "__main__":
    result = agent.invoke({"messages": [{"role": "user", "content": "Check the launch budget."}]})
    print(result["messages"][-1].content)
