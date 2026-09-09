# Proposal coverage

Source reviewed: `output/pdf/LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf` in the parent project, especially Sessions 2–8, the six domain descriptions and the outcome rubric. The two-day, eight-session structure remains the workshop contract.

| Proposal item | This implementation | Evidence to inspect |
|---|---|---|
| Marketing trend and sentiment | Weighted survey change, channel evidence, draft messaging and experiment budget | PRISM → PULSE reports and worksheets |
| Finance scenario analysis | Downside/base/upside sales cases, cash, margin, break-even and delivery-constrained revenue | LEDGER worksheet and arithmetic evidence |
| Fairness-aware HR screening | Anonymous IDs, allowlisted skills and work samples, explainable worksheet and explicit human review | NOVA details and HR input validation tests |
| Operations supply-chain risk | Supplier delay, production capacity, shortfall, fallback and launch buffer | ATLAS baseline vs supplier-delay runs |
| Analytics insight generation | Denominators, weighted trend, descriptive interval and actionable KPI definitions | PRISM metrics and assumptions |
| General Management strategic synthesis | Uses all five reports, names conflicts, preserves HOLD gates and assigns owners | JARVIS executive package |
| Agent Blueprint | Per-team agent instructions plus goal, tools, inputs and constraints in the inspector | Agent blueprint tab; SQLite persistence |
| Multimodal or real-time extension | Live Gemini image extraction with review-before-save; optional browser voice input/read-aloud; transcript/text import; observable event stream | Command channel and Memory Vault; microphone activation requires a user click |
| Company Launch Swarm | Six `create_agent` agents orchestrated in a LangGraph dependency order | `engine.py`, domain tools, live six-agent baseline and budget-cut acceptance; required brief/domain/memory tools |
| Shared command center | Jarvis HUD, agent statuses, hand-offs, traces, reports and saved run comparisons | Browser workflow |
| Governance/red team | Protected-field rejection, unknown-source behavior, no silent provider fallback, required tool evidence and hold propagation | Tests and workshop red-team worksheet |
| Timed scenario change | Budget cut, supply delay, trust concern or demand surge | Mission Control change chips |
| Final portfolio package | Markdown and JSON exports with source scenario, all domain worksheets and human assessment | Export brief / JSON |
| Rubric | Business 25, orchestration 25, evidence 20, responsible AI 15, communication 15 | Workshop lab; manual 0–5 score per criterion |

The input scaffold retains Project Monsoon, fictional Aster Foods, INR 2,400,000 launch budget, 30,000 units, 21-day supplier lead time and eight available FTE from the earlier workshop app. Price, unit cost, fixed costs, staffing allowance, production rate, surveys and anonymous candidate work samples are **new fictional teaching assumptions**, not proposal facts or market data.

Framework choice is intentionally LangChain + LangGraph as requested. CrewAI and OpenAI Agents SDK are not needed to run this version. Original generated illustrations are supplied in the deck. The app extracts image evidence; it does not generate videos or publish external business actions. A Docker/Caddy hosting recipe is supplied; remote deployment and classroom-scale load are unverified.
