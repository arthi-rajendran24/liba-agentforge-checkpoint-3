"""Build-along starter. Complete the two marked lines using the slide deck.

Run: uv run python workshop/first_agent_starter.py
Compare with: workshop/first_agent.py
"""

from langchain.agents import create_agent
from langchain_core.tools import tool
from rehearsal_model import WorkshopModel

BUDGET = 2_400_000
UNITS = 30_000
UNIT_COST = 65
OTHER_LAUNCH_COSTS = 450_000


@tool
def estimate_launch_cash() -> dict:
    """Calculate cash needed for the fictional launch and compare it with the budget."""
    # BUILD STEP 1: replace None with UNITS * UNIT_COST + OTHER_LAUNCH_COSTS
    cash_needed = None
    if cash_needed is None:
        raise ValueError("Finish build step 1: calculate cash_needed.")
    # BUILD STEP 2: replace None with max(0, cash_needed - BUDGET)
    funding_gap = None
    if funding_gap is None:
        raise ValueError("Finish build step 2: calculate funding_gap.")
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
