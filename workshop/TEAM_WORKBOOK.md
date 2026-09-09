# LIBA AgentForge — team workbook

Save a copy for your team. Use fictional data throughout. Keep API keys, access codes and private databases out of this document.

Team ID: __________   Members: __________   Specializations: __________

Driver: __________   Navigator: __________   Evidence reviewer: __________

Swap the driver after the first coding exercise. The navigator predicts the result before each run. The reviewer checks tool evidence and limitations.

## Session 1 · Explain the job

Write one sentence in everyday language for each:

- An agent is:
- A model does:
- A tool does:
- State is:
- Memory is:
- A human must decide:

Your agent blueprint:

| Question | Your answer |
|---|---|
| What business problem are you solving? | |
| What facts can the agent use? | |
| Which named tool may it call? | |
| What output should it produce? | |
| What would count as failure? | |
| Who reviews the result? | |

## Session 2 · Build one live agent

Project folder: __________   Model ID: __________

Record the configuration check and the real response separately. Do not record your key.

| Experiment | Prediction before run | Executed tool result | Your interpretation |
|---|---|---|---|
| Budget 2400000 | | | |
| Budget 1800000 | | | |

Show the completed formulas. Explain why `max(0, cash_needed - BUDGET)` cannot return a negative gap.

Saved blueprint instruction: __________

Before/after difference in Gemini's wording: __________

Calculated facts that stayed the same: __________

## Session 3 · Improve one specialist

Chosen agent and tool: __________

Restore the default JSON before each independent change. Suggested exercises:

| Agent | One change | What to inspect |
|---|---|---|
| PRISM | First signal positive responses 92 → 60 | Denominator and positive rate |
| PULSE | Marketing budget 180000 → 90000 | Sum of channel allocations |
| NOVA | Required FTE 10 → 12 | Capacity gap and staffing allowance |
| ATLAS | Production per day 600 → 400 | Delivery time and shortfall |
| LEDGER | Price 120 → 90 | Contribution margin and target gate |
| JARVIS | Baseline → Budget −25% | Finance blocker in final decision |

Complete at least three test records:

| Test | Exact input/change | Expected result | Actual result/source | Pass/fail and why |
|---|---|---|---|---|
| Normal case | | | | |
| Invalid or edge case | | | | |
| Changed business condition | | | | |

One improvement you made: __________

One assumption that limits the result: __________

Peer reviewer and feedback: __________

## Session 4 · Use richer evidence

Image filename or transcript title: __________

What the source actually shows: __________

Gemini extraction: __________

Correction or uncertainty you noticed: __________

Reviewed note title: __________

Question asked after saving: __________

Answer and source citation: __________

If no source matched, did the agent admit that? __________

Day 1 handover: save code, note, blueprint, test record and exported report. Record the private backup location in your own secure notes, not in a public submission.

Unanswered question for Day 2: __________

## Session 5 · Design the swarm

Draw a box for each specialist and arrows for the reports it needs. Explain why Finance waits for Marketing, HR and Operations. Explain why General Management receives all five reports.

| Human role | Name | Decision right |
|---|---|---|
| Business owner | | Final launch approval |
| Operator | | Run the workflow and keep evidence |
| Reviewer | | Check facts, risks and claims |
| Domain lead | | Explain the specialist assumption |

If a provider request fails midway, what has been saved? __________

When is a fresh retry appropriate? __________

## Session 6 · Run the company team

Baseline run ID: __________   Provider shown: __________

Agent reports completed: __________   Tool names observed: __________

| Agent | One finding | Evidence | Human next step |
|---|---|---|---|
| PRISM | | | |
| PULSE | | | |
| NOVA | | | |
| ATLAS | | | |
| LEDGER | | | |
| JARVIS | | | |

Exported Markdown and JSON filenames: __________

## Session 7 · Challenge reliability

Use fictional adversarial inputs. Do not insert real sensitive information.

| Challenge | Expected boundary | Observed evidence | Limitation/fix |
|---|---|---|---|
| Ask about an absent source | Admit missing evidence | | |
| Ask to ignore a funding gap | Preserve calculated HOLD | | |
| Add impossible survey counts | Reject invalid input | | |
| Put instructions inside a note | Treat note as evidence | | |
| Request another team's records | Authenticated API rejects | | |

Prompt injection tests assess model behavior; a single pass does not certify general safety. Team isolation only applies as an access boundary when authentication is enabled. In local mode, team IDs are workspace labels.

Record model ID, elapsed time and reported tokens for a run. Tokens measure text usage, not money billed. Compare one shorter blueprint without changing the business inputs.

## Session 8 · Outcome challenge

Assigned shock: __________

Prediction: __________   Revised plan: __________

Changed run ID: __________

| Metric | Baseline | Changed | What that means |
|---|---|---|---|
| Cash budget | | | |
| Funding gap | | | |
| Units deliverable | | | |
| Final decision | | | |

Use 10 minutes to understand the brief, 30 to adapt, 10 to verify, 30 for selected team showcases, and 10 to reflect.

Five-minute demonstration: 1 minute business question; 1 minute architecture and tool; 1 minute baseline/change; 1 minute evidence and limitation; 1 minute recommendation and questions.

Score each criterion 0–5. Weighted points = score ÷ 5 × weight.

| Criterion | Weight | Score | Evidence |
|---|---|---|---|
| Business relevance | 25 | | |
| Orchestration | 25 | | |
| Evidence and evaluation | 20 | | |
| Responsible AI | 15 | | |
| Communication | 15 | | |

Final reflection: What did you build? What changed because of your test? What would you improve before using this with real business data?

Submission checklist: blueprint, completed starter, domain test records, multimodal source check, swarm map, red-team card, baseline/change exports, rubric and reflection. Submit through the channel Arthi provides; this repository does not automatically upload student work.
