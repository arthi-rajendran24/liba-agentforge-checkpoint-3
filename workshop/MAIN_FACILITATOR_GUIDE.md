# LIBA AgentForge JARVIS — main facilitator guide

Prepared for Arthi Rajendran. Main live workshop, two days, eight ninety-minute sessions. Prepared 3 September 2026.

## How to use this kit

Present **LIBA_AgentForge_JARVIS_Main_Workshop.pptx**. Its 98 slides have full notes in PowerPoint Presenter View. Slides 1–90 teach the main route; 91–98 are facilitator references. The PDF is a slide-only viewing copy. This guide repeats every slide's teaching script so you can rehearse without Presenter View.

This is a build-along from working templates. Learners complete a small real LangChain agent, adapt all six business roles, use multimodal evidence and coordinate a reviewed decision. They do not recreate the entire web server from an empty folder. Advanced pairs can change a tool rule with a meaningful test; beginners change scenario inputs and saved agent instructions.

The main route uses **live Gemini**. The earlier Dry Run deck and QUICKSTART are retained only for an explicitly announced fallback. Gemini generates language and chooses tool calls; Python functions calculate business facts; LangGraph carries the reports between specialists.

## Set up before participants arrive

1. Follow PUBLISHING.md and verify the exact repository URL using a fresh clone. If private, check a participant's access. This source package does not itself create a GitHub repository.
2. Verify Git, uv, editor, browser, power and network on the teaching laptop. Have two terminal windows: one keeps the server running, one runs the coding lab. Keep the project folder, LIVE_QUICKSTART and TEAM_WORKBOOK visible.
3. Choose the classroom access model. Each pair can run a local clone with its own approved Gemini project access. A hosted app keeps the facilitator key on the server and uses team access codes; learners still need a ready local/pair machine for the coding lab. Do not claim that a hosted login configures local Python access.
4. Configure .env privately. Run doctor, then first_agent_live.py, then a full browser swarm. These are separate checks: configuration, live tool use, and complete application behavior.
5. Inspect actual project quotas in AI Studio. During preparation one project reported 15 model requests per minute. The app paces its own process at 12 requests/minute, but separate laptops/processes share project quota if they use the same project. Token and daily limits also apply. Stagger teams and avoid running separate CLI tests during a browser swarm.
6. Use a fresh demonstration team ID. Check a source-note citation, image extraction, baseline/change comparison, rubric save and export. Bring the fictional image sample and scenario file.
7. For a hosted session, complete deploy/README.md on the actual host: HTTPS, team login/isolation, provider quota, backup/restore and representative concurrency. The Docker recipe and class-scale load are not verified by the local build. Use the measured capacity to choose group size.
8. Verify projection readability. Test microphone support only if using it; the image activity supplies the required multimodal exercise if voice is unavailable.

## Facilitate the room

Begin each activity with: “Watch once. Predict the result. Build with your partner. Show the evidence.” Assign a driver who types, a navigator who checks the guide and predicts, and an evidence reviewer when team size allows. Swap the driver after the first agent.

Use green/amber signals at checkpoints. Ask a green pair to explain, not simply click ahead. Give an amber pair one diagnostic step at a time: folder, saved file, exact input, provider state. If installation takes more than five minutes, move the learner to a ready pair while support resolves it. Do not consume the full class's build time on one machine.

Never ask learners to reproduce a model's exact prose. Ask them to show the executed tool, exact scenario, arithmetic, source and limitation. Distinguish what the program computed from what the model suggested.

## The proposal schedule

Each day: 09:00–10:30, break 10:30–10:45, 10:45–12:15, lunch 12:15–13:15, 13:15–14:45, break 14:45–15:00, 15:00–16:30.

| Session | Slides | Ninety-minute facilitation route | Deliverable |
|---|---|---|---|
| D1 S1 Foundations | 1–17 | 15 goals/analogy; 20 loops/tools; 20 state/memory; 20 map a task; 15 share/check | Testable blueprint |
| D1 S2 Design studio | 18–39 | 20 clone/install; 15 live setup; 25 code; 15 experiment; 15 save blueprint | Live tool-calling agent |
| D1 S3 Domain agents | 40–50 | 15 inspect role; 35 controlled experiments; 20 improve prompt/source; 20 peer review | Tested domain improvement |
| D1 S4 Multimodal | 51–57 | 15 source quality; 25 image extraction; 20 voice/transcript; 15 retrieval; 15 handover | Reviewed source and citation |
| D2 S5 Swarm design | 58–65 | 15 resume; 20 dependencies; 20 state/memory; 20 owners/failure; 15 map review | Workflow and decision rights |
| D2 S6 Command center | 66–74 | 15 architecture; 25 live run; 20 inspect tools; 15 compare; 15 export/check | Complete live package |
| D2 S7 Improve/test | 75–82 | 15 governance; 25 red team; 20 cost/limits; 20 one improvement; 10 evidence card | Before/after test evidence |
| D2 S8 Outcome challenge | 83–90 | 10 brief; 30 adapt; 10 verify; 30 selected demos; 10 reflect | Assessed portfolio package |

Preserve A–A, B–B, C–C continuity when repeating this content for the three sections: each section's Day 2 follows its own Day 1 and uses its saved team work. Repeat the same core case and rubric across sections; do not substitute another group's database.

## Demonstration answer key

All figures are fictional teaching assumptions from the supplied default scenario. Restore examples/project-monsoon.json and select Baseline between independent experiments.

| Exercise | Single change | Expected calculated evidence |
|---|---|---|
| Tiny live agent | Budget 2400000 → 1800000 | Cash remains 2400000; gap 600000; HOLD |
| PRISM | signals[0].positive 92 → 60 | 229 positive of 360; 63.6% instead of 72.5% |
| PULSE | marketing_budget 180000 → 90000 | Channel allocations sum to INR 90000 |
| NOVA | required_fte 10 → 12 | Four FTE gap; INR 40000 allowance |
| ATLAS | production_per_day 600 → 400 | 21 + 75 = 96 days; 4800 units short by day 84 |
| LEDGER | price 120 → 90 | Margin 27.8%, below 38% target; HOLD despite no cash gap |
| JARVIS | Default plus Budget −25% | Finance's INR 600000 gap survives into final HOLD |
| Supplier shock | Default plus Supplier +14 days | 600 units miss the window; HOLD |
| Demand shock | Default plus Demand +40% | INR 780000 gap; 4200 units short; HOLD |
| Memory | Save Packaging review note naming Mira | Answer names Mira and cites the note |
| Image | Extract workshop/assets/monsoon-case.png | 24 lakh, 30000, 84 days, price120/unit cost65; human review before save |

A passing calculation is not a market forecast or launch approval. HR uses anonymous skills/work samples; scores do not make hiring decisions. Analytics denominators describe this fictional sample, not population demand. Marketing allocation is a teaching rule, not proven ROI.

## Readiness and issue log

| Check | Evidence to record | Owner/status |
|---|---|---|
| Actual GitHub clone | URL, access and fresh install result | |
| Live provider | Model, tool success, quota check | |
| Full workflow | Baseline and changed run IDs | |
| Source and multimodal | Note citation and image review | |
| Day 2 continuity | Saved code, team ID, notes and backup | |
| Hosted delivery, if used | HTTPS, login/isolation, restore and load evidence | |

| Time/team | Exact sanitized symptom | Layer | Next action/owner | Retest evidence |
|---|---|---|---|---|
| | | | | |

For a provider outage, deliberately announce the fallback and use the old Dry Run guide. Label scripted outputs as rehearsal. For a busy response, wait for current work. For a failed run, inspect the completed reports; rerun deliberately after resolving the cause. Do not repeatedly click to create more work.

## Slide-by-slide teaching script

### 01 · Build your AI business team.

SAY
Welcome. We will build real tool-using agents, test business assumptions and defend a coordinated launch decision. Gemini generates the language; Python tools calculate the facts.

DEMONSTRATE / BUILD TOGETHER
Open the live app, editor and terminal. Explain driver/navigator roles. Every learner keeps their own project or joins an approved hosted team.

ASK THE ROOM
What business task would you delegate if you could inspect every action?

EXPECTED EVIDENCE
One concrete task with a measurable output.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.
- Original generated command-core illustration from the prior AgentForge deck.

### 02 · Leave with a working system you can explain.

SAY
This is a guided build from working templates. You will edit code and inputs, observe real Gemini tool calls, and explain your own evidence.

DEMONSTRATE / BUILD TOGETHER
Show the final portfolio checklist: agent blueprint, domain output, multimodal test, swarm map, red-team card, final package and reflection.

ASK THE ROOM
What would demonstrate understanding beyond clicking Run?

EXPECTED EVIDENCE
A prediction, code or input change, tool result and justified decision.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 03 · Your two-day route.

SAY
Each session is ninety minutes. Coffee is 10:30–10:45, lunch 12:15–13:15, and the afternoon break 14:45–15:00. Each day ends at 16:30.

DEMONSTRATE / BUILD TOGETHER
Show this route. Keep the same files, account and team ID for Day 2.

ASK THE ROOM
Which Day 1 outputs will Day 2 depend on?

EXPECTED EVIDENCE
Saved code, blueprints, notes, scenario and working provider access.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.

### 04 · Understand the agent loop.

SAY
This session has one practical deliverable. Deliverable: a goal, a tool, and a clear success check.

DEMONSTRATE / BUILD TOGETHER
0–15: goals and analogy. 15–35: tools and loops. 35–55: memory and teamwork. 55–75: map a business task. 75–90: share a blueprint and check understanding.

ASK THE ROOM
What will we show before the break?

EXPECTED EVIDENCE
Deliverable: a goal, a tool, and a clear success check.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 05 · Think of agents as a kitchen team.

SAY
A restaurant works because different specialists share an order and use the right equipment. One person does not have to do everything. Our business agents are software roles, not employees with judgment or accountability.

DEMONSTRATE / DO TOGETHER
Use the illustration to point out the order rail, specialists and head chef. Map Finance to checking costs, Operations to timing, and General Management to coordinating the final decision.

ASK THE ROOM
What happens if each chef works from a different order?

EXPECTED EVIDENCE
The outputs conflict. That is why our agents receive shared facts.

IF SOMEONE IS STUCK
Keep the analogy short. A software agent has no human intention, common sense or responsibility.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.
- Original kitchen-team illustration generated with built-in image_gen, 3 September 2026. Asset: workshop/assets/kitchen-team.png.

### 06 · An agent can use a tool before replying.

SAY
A chatbot can explain a formula. An agent workflow can call a calculator-like function, read its result, and then respond. Tool use is an observable action; it is not a magical guarantee of correctness.

DEMONSTRATE / DO TOGETHER
Read each arrow aloud. Use “calculate launch cash” as the concrete example.

ASK THE ROOM
Which path gives us an arithmetic result we can inspect?

EXPECTED EVIDENCE
The tool path. The tool and its inputs must still be checked.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 07 · An agent needs a clear job description.

SAY
Imagine onboarding a new assistant. “Help with business” is vague. “Compare launch cash against the approved budget and show the arithmetic” is testable.

DEMONSTRATE / DO TOGETHER
Ask participants to draft one sentence for a Finance assistant. Keep the output specific: cash needed, gap and human review.

ASK THE ROOM
What is missing from “be a helpful Finance agent”?

EXPECTED EVIDENCE
A clear goal, defined inputs, permitted tools, constraints and success criteria.

IF SOMEONE IS STUCK
Use the completed agent blueprint in the app as a template; do not ask beginners to invent a system from a blank page.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 08 · The loop is: ask, act, observe, reply.

SAY
The live model can decide to call a tool, inspect the result and continue. Our app requires a brief read, domain calculation and memory search before accepting a report.

DEMONSTRATE / BUILD TOGETHER
Trace one request. The activity stream records actions, not hidden thoughts. If a tool is skipped, one correction turn asks Gemini to complete it.

ASK THE ROOM
What is the difference between a model saying it calculated and a recorded tool result?

EXPECTED EVIDENCE
The latter identifies an executed function and result.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 09 · Plan, execute, reflect: a second useful loop.

SAY
Planning is like writing a shopping list. Execution buys the ingredients. Reflection checks whether anything is missing. Not every task needs a separate planning agent.

DEMONSTRATE / BUILD TOGETHER
Ask pairs to map a campaign brief into three steps and define the check after each. Our implemented swarm uses a defined route and human review rather than an unrestricted autonomous planner.

ASK THE ROOM
When should the loop stop?

EXPECTED EVIDENCE
When the requested deliverable meets the check or a clear blocker requires a person.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 10 · LangChain is the agent’s wiring kit.

SAY
Think of LangChain as connectors and wiring, not as the intelligence itself. We provide the model and tools. create_agent assembles them into a runnable agent.

DEMONSTRATE / DO TOGETHER
Explain each word without diving into package internals. The model is the response engine; the adapter is the plug that lets the framework talk to it.

ASK THE ROOM
Where does our business arithmetic live?

EXPECTED EVIDENCE
In Python tools, not inside the LangChain package or a guessed model answer.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 11 · LangGraph gives the team a route map.

SAY
LangChain helps us create an individual agent. LangGraph helps us define what happens next and what information travels between steps. In this app the outer workflow runs agents in a predictable sequence.

DEMONSTRATE / DO TOGETHER
Draw an everyday approval route: analyst → manager → decision. Explain nodes as steps, edges as routes and state as shared information.

ASK THE ROOM
Why should Finance see delivery capacity before estimating sales?

EXPECTED EVIDENCE
It should not count units Operations cannot deliver.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- https://docs.langchain.com/oss/python/langgraph/overview
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 12 · Shared state is the team’s clipboard.

SAY
The clipboard travels with this job. It starts with scenario facts and collects reports. Memory is different: it is a saved filing cabinet that survives a restart.

DEMONSTRATE / DO TOGETHER
Use one example: the current budget goes on the clipboard; a packaging-review note goes in Memory Vault.

ASK THE ROOM
Will the same team ID on two laptops share a clipboard?

EXPECTED EVIDENCE
No. Each local app has its own database. IDs label local workspaces; they do not create network synchronization.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 13 · Six specialists answer six questions.

SAY
These are the six specialization roles in the proposal. JARVIS also names the chat interface, but the command assistant and the General Management synthesis agent are separate agent instances.

DEMONSTRATE / DO TOGETHER
Ask each pair to pick a specialist to explain later. Everyone clones the whole app; they do not need six separate installations.

ASK THE ROOM
Which role should own the final human launch approval?

EXPECTED EVIDENCE
A person. JARVIS proposes a recommendation; it cannot approve spending or launch the company.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 14 · Our shared case is Project Monsoon.

SAY
We are launching a shelf-stable millet snack in Chennai and Bengaluru. Every number is fictional. The point is to learn how different functions reason from the same facts.

DEMONSTRATE / DO TOGETHER
Open the scenario briefly and show the budget, units, price and unit cost. Mention that additional launch costs total ₹4.5 lakh under the default assumptions.

ASK THE ROOM
What could go wrong if Marketing promises more than Operations can produce?

EXPECTED EVIDENCE
The campaign, capacity plan and revenue forecast would contradict each other.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 15 · Before we code, check the cash by hand.

SAY
The initial plan uses the full budget. Other launch costs combine ₹2.5 lakh fixed costs, ₹1.8 lakh marketing and ₹20,000 staffing allowance. No cash headroom is left under these simplified assumptions.

DEMONSTRATE / DO TOGETHER
Ask someone to calculate 30,000 times 65. Then add the other costs. This gives the class an independent expected result before running any code.

ASK THE ROOM
Does “fits the budget” mean “safe to launch”?

EXPECTED EVIDENCE
No. Supply, margin, customer trust and human sign-off still matter.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 16 · Turn a vague prompt into a testable job.

SAY
A useful job description names an observable result. The agent is not accountable for the business; a person is.

DEMONSTRATE / BUILD TOGETHER
Ten minutes: each pair writes goal, inputs, allowed tool, output and failure condition. Swap with a neighboring pair for critique.

ASK THE ROOM
How will you know the agent failed?

EXPECTED EVIDENCE
A missing tool, incorrect arithmetic, absent evidence or unsupported approval.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.

### 17 · Checkpoint: explain it without AI jargon.

SAY
Explain one concept to a partner as if they have never coded. Avoid saying the software thinks like a person.

DEMONSTRATE / BUILD TOGETHER
Let three learners give examples from different specializations. Save the blueprint to workshop/TEAM_WORKBOOK.md.

ASK THE ROOM
Can you explain the tool loop in thirty seconds?

EXPECTED EVIDENCE
An accurate everyday explanation plus a concrete check.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 18 · Build your first live agent.

SAY
This session has one practical deliverable. Deliverable: working Python code that calls Gemini and a real tool.

DEMONSTRATE / BUILD TOGETHER
0–20: clone and install. 20–35: configure Gemini and test access. 35–60: complete the starter. 60–75: experiment. 75–90: save a specialist blueprint.

ASK THE ROOM
What will we show before the break?

EXPECTED EVIDENCE
Deliverable: working Python code that calls Gemini and a real tool.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 19 · Prepare a simple local workstation.

SAY
The live workshop needs model access and internet. GitHub access and Gemini access are different. A paid subscription to a chatbot does not itself prove API quota.

DEMONSTRATE / BUILD TOGETHER
Check Git and uv versions. Use your own approved API key for your local clone, or the facilitator-provided hosted team login.

ASK THE ROOM
Where does the API key belong?

EXPECTED EVIDENCE
In the local server .env, not slides, Memory Vault or a shared repository.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.
- https://ai.google.dev/gemini-api/docs/api-key

### 20 · GitHub is the shared shelf. Clone is a copy.

SAY
Git is the change-tracking tool. GitHub hosts a repository online. Cloning makes a local copy that you can run and edit. Cloning does not change Arthi’s copy.

DEMONSTRATE / DO TOGETHER
Show a repository’s green Code menu and the HTTPS copy option after the final repository is published. If private, confirm each participant has access before the session.

ASK THE ROOM
Do your experimental edits automatically change the shared repository?

EXPECTED EVIDENCE
No. A push or other deliberate sharing action is required.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

### 21 · macOS: install only what is missing.

SAY
Version checks tell us whether installation is needed. Do not reinstall tools that already work. The Git installer may open a macOS dialog; finish that normally.

DEMONSTRATE / DO TOGETHER
Demonstrate the two version checks. For missing Git use the Apple command-line-tools route documented by Git. For uv use the official installer or the institution’s approved package manager.

ASK THE ROOM
What should you do if uv is installed but the terminal cannot find it?

EXPECTED EVIDENCE
Open a fresh terminal and check again.

IF SOMEONE IS STUCK
Do not change system policy to work around managed-device restrictions. Use a prepared partner machine if necessary.

Displayed commands or code:

```text
git --version
uv --version

# If Git is missing:
xcode-select --install

# If uv is missing:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Sources:

- https://git-scm.com/install/mac
- https://docs.astral.sh/uv/getting-started/installation/

### 22 · Windows: use PowerShell for setup.

SAY
PowerShell is the Windows command window used in this deck. The commands begin with the tool name; do not copy a prompt symbol such as a dollar sign from a website.

DEMONSTRATE / DO TOGETHER
Check versions, then install only missing tools. If winget is unavailable, use the official Git and uv installation pages linked in these notes and ask IT for the approved route.

ASK THE ROOM
Why do we open a fresh terminal after installation?

EXPECTED EVIDENCE
The new terminal picks up the updated command search path.

IF SOMEONE IS STUCK
Do not paste macOS shell commands into PowerShell. Use the Windows-specific instructions.

Displayed commands or code:

```text
git --version
uv --version

# Install missing tools:
winget install --id Git.Git -e --source winget
winget install --id astral-sh.uv -e
```

Sources:

- https://git-scm.com/install/windows
- https://docs.astral.sh/uv/getting-started/installation/

### 23 · Clone the link Arthi gives you.

SAY
Clone the actual workshop repository; the inspiration repo is a different application.

DEMONSTRATE / BUILD TOGETHER
Type git clone, paste the tested HTTPS URL, add agentforge-jarvis, then enter that folder. Use workshop/LIVE_QUICKSTART.md for copyable commands.

ASK THE ROOM
Which file identifies the project root?

EXPECTED EVIDENCE
pyproject.toml and uv.lock.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Displayed commands or code:

```text
cd agentforge-jarvis
ls
```

Sources:

- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 24 · Know the few files you will touch.

SAY
A repository can look intimidating. We will use only a few files. The workshop folder is our small coding lab; the main source folder contains the complete app.

DEMONSTRATE / DO TOGETHER
Open the project in the editor. Show the folder tree without reading every file. Explain that .agentforge is created locally when the application stores data and is ignored by Git.

ASK THE ROOM
Which file should we avoid uploading if it contains a key?

EXPECTED EVIDENCE
The local .env file. It is ignored by Git; never put keys into notes or screenshots either.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 25 · uv prepares a separate toolbox for this app.

SAY
Think of .venv as a toolbox reserved for this project. uv reads what the project needs and installs matching versions. The lockfile keeps classmates on the same tested dependency set.

DEMONSTRATE / DO TOGETHER
Explain --frozen as “use the existing lockfile; do not resolve a different set of versions.” Do not describe it as a guarantee that network access is unnecessary.

ASK THE ROOM
Why not install random package versions by hand during the session?

EXPECTED EVIDENCE
Different versions create different behavior and make group debugging harder.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- https://docs.astral.sh/uv/getting-started/installation/
- https://docs.astral.sh/uv/concepts/projects/sync/
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 26 · Install the locked dependencies once.

SAY
The lockfile selects the tested dependency versions. Tests here use controlled inputs, so running pytest does not spend model quota.

DEMONSTRATE / BUILD TOGETHER
Run uv sync --frozen, then uv run pytest -q. Inspect the final summary.

ASK THE ROOM
Does passing offline tests prove Gemini is reachable?

EXPECTED EVIDENCE
No. The next check must make a real provider call.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Displayed commands or code:

```text
uv sync --frozen
uv run pytest -q
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 27 · Connect Gemini on your own laptop.

SAY
This slide contains a placeholder, never the facilitator key. .env is a small local configuration file. The selected model was available during preparation; access and quota can differ by account.

DEMONSTRATE / BUILD TOGETHER
On Mac run cp .env.example .env; on PowerShell use Copy-Item .env.example .env. Open .env privately in the editor and enter your approved key. Ensure old AGENTFORGE_PROVIDER shell overrides are removed.

ASK THE ROOM
Will a GitHub clone include Arthi’s secret?

EXPECTED EVIDENCE
No. Each local clone needs approved access. Hosted participants use their team login and the server holds the model key.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Displayed commands or code:

```text
AGENTFORGE_PROVIDER=gemini
AGENTFORGE_MODEL=gemini-3.1-flash-lite
GEMINI_API_KEY=your-own-key
```

Sources:

- https://ai.google.dev/gemini-api/docs/api-key
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 28 · Check configuration, then test a real response.

SAY
Doctor validates configuration without a provider call. The completed reference then makes a live Gemini request and exposes a small tool. The third command starts the browser app.

DEMONSTRATE / BUILD TOGETHER
Run the reference privately, confirm cash2400000 and gap0 in the answer, and open http://127.0.0.1:8787. Keep that server terminal open.

ASK THE ROOM
What happens if a key is valid but the project has no remaining quota?

EXPECTED EVIDENCE
A quota error. Check AI Studio and follow the facilitator schedule; do not call a simulated answer live.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Displayed commands or code:

```text
uv run agentforge-jarvis doctor
uv run python workshop/first_agent_live.py
uv run agentforge-jarvis web
```

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.
- https://ai.google.dev/gemini-api/docs/api-key

### 29 · Hosted team access uses a different secret.

SAY
If the facilitator provides an HTTPS workshop server, the model key stays on that server. You log into your assigned team. A local clone is still needed for the coding lab unless you pair with a ready machine.

DEMONSTRATE / BUILD TOGETHER
Show the login screen if hosted deployment is in use. Explain twelve-hour sessions and private team codes. On local loopback without authentication, team IDs are only workspace labels.

ASK THE ROOM
Can a signed-in team choose another team ID to read its data?

EXPECTED EVIDENCE
The authenticated server rejects cross-team requests. Verify this on the actual deployment before class.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 30 · Build a small agent you can inspect.

SAY
We provide the imports and adapter so you can focus on a useful tool. You will complete two calculations and run a live agent.

DEMONSTRATE / BUILD TOGETHER
Open workshop/first_agent_starter_live.py. Use a second terminal in the project root.

ASK THE ROOM
Which parts do you expect to find?

EXPECTED EVIDENCE
A model adapter, tool function, role prompt and create_agent.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 31 · Open the starter and find the two blanks.

SAY
The starter has two None values, meaning deliberately empty calculations. Large numbers use underscores for readability.

DEMONSTRATE / BUILD TOGETHER
Find cash_needed and funding_gap. Keep the surrounding indentation.

ASK THE ROOM
What should the completed formula return?

EXPECTED EVIDENCE
Cash needed2400000 and gap0.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Displayed commands or code:

```text
workshop/first_agent_starter_live.py

BUDGET = 2_400_000
UNITS = 30_000
UNIT_COST = 65
OTHER_LAUNCH_COSTS = 450_000
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 32 · Complete the calculator in two lines.

SAY
The first line calculates all the upfront cash. The second reports a gap only if the requirement exceeds the budget. These are ordinary Python calculations.

DEMONSTRATE / DO TOGETHER
Replace only the two None values in the starter and save. Keep the indentation already present. Explain multiplication and subtraction using the earlier handwritten calculation.

ASK THE ROOM
If cash needed is ₹24 lakh and budget is ₹18 lakh, what is funding_gap?

EXPECTED EVIDENCE
₹6 lakh, stored as 600000.

IF SOMEONE IS STUCK
Check spelling, uppercase variable names and indentation. Do not paste smart quotation marks from a messaging app.

Displayed commands or code:

```text
cash_needed = UNITS * UNIT_COST + OTHER_LAUNCH_COSTS

funding_gap = max(0, cash_needed - BUDGET)
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 33 · @tool gives the calculator a clear label.

SAY
The decorator is like attaching a label and instruction card to a machine. LangChain can discover the tool’s name and description. The docstring explains what the tool does.

DEMONSTRATE / DO TOGETHER
Point to @tool, the function name, the description and the arithmetic. Explain dict as a small labelled result, like a form with named fields.

ASK THE ROOM
Does @tool automatically verify our formula?

EXPECTED EVIDENCE
No. It exposes the function as a tool. We still write and test the function correctly.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Displayed commands or code:

```text
@tool
def estimate_launch_cash() -> dict:
    """Calculate launch cash and compare the budget."""
    cash_needed = UNITS * UNIT_COST + OTHER_LAUNCH_COSTS
```

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.
- Local teaching source: workshop/first_agent_starter.py and workshop/first_agent.py.

### 34 · create_agent connects the working parts.

SAY
Read it as a sentence: create an agent with this live model, this permitted tool and this instruction. The adapter is the plug between Gemini and LangChain.

DEMONSTRATE / BUILD TOGETHER
Show workshop/live_model.py. It loads .env and calls the same model factory as the app.

ASK THE ROOM
Where is the cash formula executed?

EXPECTED EVIDENCE
In your Python tool, not in a guessed language-model answer.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Displayed commands or code:

```text
agent = create_agent(
    model=workshop_model(),
    tools=[estimate_launch_cash],
    system_prompt="Use the cash tool. A human decides.",
)
```

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 35 · invoke starts one conversation turn.

SAY
Invoke simply means “run this agent with these inputs.” We send one user message and print the final response after the tool call finishes.

DEMONSTRATE / DO TOGETHER
Read the braces as a labelled input object. Point out role and content. Avoid introducing every Python collection concept at once.

ASK THE ROOM
Which result do we print: the first instruction or the final answer?

EXPECTED EVIDENCE
The final message, selected with -1.

IF SOMEONE IS STUCK
The starter already contains this code. Ask learners to inspect it; do not require manual retyping.

Displayed commands or code:

```text
result = agent.invoke({
    "messages": [{
        "role": "user",
        "content": "Check the launch budget."
    }]
})
print(result["messages"][-1].content)
```

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- Local teaching source: workshop/first_agent.py.

### 36 · Run your first agent and check the result.

SAY
The final wording can vary because Gemini generates it. Verify the tool result, not an exact sentence.

DEMONSTRATE / BUILD TOGETHER
Save the completed file and run the command. Compare to the manual arithmetic. The completed reference is first_agent_live.py.

ASK THE ROOM
What makes this a live test?

EXPECTED EVIDENCE
The configured Gemini API returned a response through LangChain; the cash tool ran in Python.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Displayed commands or code:

```text
uv run python workshop/first_agent_starter_live.py

# Check the numbers in the live answer:
# cash needed: 2400000
# funding gap: 0
# decision: human review required
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 37 · Change one number. Predict before you run.

SAY
Predict first. Changing one number gives a clean experiment. The cash requirement stays fixed while the approved budget shrinks.

DEMONSTRATE / BUILD TOGETHER
Set BUDGET=1_800_000, save and rerun the live starter. Check gap600000 and HOLD. Restore the original or save a named variant.

ASK THE ROOM
Can a persuasive prompt remove the actual cash shortfall?

EXPECTED EVIDENCE
No. The business input or plan must change.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 38 · The tiny lab and the full app are separate.

SAY
We used a miniature to understand the pieces. The full app extends the same pattern with schemas, memory, graph orchestration, persistence and a browser interface.

DEMONSTRATE / DO TOGETHER
Point to the two folders. Make sure nobody expects their starter’s BUDGET edit to change the command center automatically.

ASK THE ROOM
Where do we change the full app’s budget?

EXPECTED EVIDENCE
In Edit brief, or by selecting the budget-cut challenge.

IF SOMEONE IS STUCK
If the app seems unchanged after a starter edit, that is expected. These are separate runnable examples.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 39 · Build the agent blueprint before tuning it.

SAY
The blueprint adds team preferences to the agent’s role. It can change presentation and requested emphasis. It cannot rewrite authoritative calculation tools or remove review gates.

DEMONSTRATE / BUILD TOGETHER
Save: Begin with a three-bullet business summary; name the largest uncertainty. Run the specialist again and compare its narrative with the previous response.

ASK THE ROOM
Which change should stay stable?

EXPECTED EVIDENCE
Calculated metrics remain tied to the same scenario and Python tool.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 40 · Adapt the six specialists.

SAY
This session has one practical deliverable. Deliverable: a domain agent with a tested improvement.

DEMONSTRATE / BUILD TOGETHER
0–15: choose domain and inspect contract. 15–50: run controlled experiments. 50–70: add a useful instruction or source. 70–90: peer review and demonstrate.

ASK THE ROOM
What will we show before the break?

EXPECTED EVIDENCE
Deliverable: a domain agent with a tested improvement.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 41 · Use a fresh baseline for every experiment.

SAY
Scenario changes and challenge chips combine. To understand one effect, choose Baseline, change only the intended field, and restore the default JSON afterward.

DEMONSTRATE / DO TOGETHER
Open Edit brief. Download the scenario template or use examples/project-monsoon.json. Show that Apply validates the structure before accepting it. Click a specialist, open its blueprint and use Run specialist + dependencies.

ASK THE ROOM
Why might a second experiment produce unexpected results?

EXPECTED EVIDENCE
A previous edit or challenge may still be active.

IF SOMEONE IS STUCK
Do not upload real candidate or customer data. Use the fictional scenario file.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 42 · PRISM turns counts into a useful signal.

SAY
PRISM adds positive responses and divides by total responses. It also compares supplied prior rates and reports a descriptive uncertainty interval. We do not need interval mathematics to understand that sample evidence has limits.

DEMONSTRATE / DO TOGETHER
Restore the default JSON, choose Baseline, change the first positive count to 60, and run PRISM. Check 229 positives out of 360 responses.

ASK THE ROOM
Can we say 63.6% of the whole city will buy?

EXPECTED EVIDENCE
No. These are fictional survey responses from a convenience sample, not a representative sales forecast.

IF SOMEONE IS STUCK
The value must not exceed the response count. Validation rejects impossible counts.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 43 · PULSE turns signals into a testable campaign.

SAY
PULSE uses the supplied channel signals to allocate an experimental budget and prepare draft messaging. It does not prove which channel causes sales.

DEMONSTRATE / DO TOGETHER
Inspect the channel rows and add the allocated amounts. Point to the draft label and customer-claim review gate. Restore defaults after the exercise.

ASK THE ROOM
What should we measure before scaling the campaign?

EXPECTED EVIDENCE
Actual conversion with denominators, customer feedback and credible cost information.

IF SOMEONE IS STUCK
Do not treat a survey’s positive count as observed revenue. The tool explicitly labels this as a heuristic.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 44 · NOVA shows capacity and skills for review.

SAY
FTE means full-time-equivalent capacity: two half-time contributions can count as one FTE. NOVA also shows a worksheet using job skills and work samples. Excluding demographic fields does not establish fairness.

DEMONSTRATE / DO TOGETHER
Change required_fte to 12. Show the four-FTE gap and the simple one-time allowance of ₹10,000 per gap FTE. It is not a salary estimate. Read the human-review label for every candidate.

ASK THE ROOM
Can we automatically reject the lowest worksheet score?

EXPECTED EVIDENCE
No. The workflow requires contextual human review, calibration and accessibility checks.

IF SOMEONE IS STUCK
Do not add age, gender or other protected attributes. The scenario schema rejects unrecognized candidate fields.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 45 · ATLAS checks whether the promise fits time.

SAY
At 400 units per day, producing 30,000 units takes 75 days. With 21 supplier days, completion takes 96 days. Only 63 production days fit inside the 84-day launch window, giving 25,200 units.

DEMONSTRATE / DO TOGETHER
Ask learners to calculate 84 minus 21, then multiply by 400. Show the 4,800-unit difference and the fallback action.

ASK THE ROOM
Should Marketing still promise all 30,000 units by day 84?

EXPECTED EVIDENCE
No. Adjust scope, time or credible capacity before making the promise.

IF SOMEONE IS STUCK
We assume constant capacity and sequential supply/production phases. Real delivery plans need more detail.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 46 · LEDGER checks more than cash availability.

SAY
Gross margin is the share of selling price left after unit production cost. With price 90 and cost 65, the difference is 25; 25 divided by 90 is about 27.8%. The target is 38%.

DEMONSTRATE / DO TOGETHER
Show cash and margin side by side. The price edit does not change upfront production cost, but it weakens unit economics.

ASK THE ROOM
Why can LEDGER return HOLD with no funding gap?

EXPECTED EVIDENCE
Because a different financial gate, the margin target, failed.

IF SOMEONE IS STUCK
This is a fictional business exercise, not investment advice or a complete accounting model.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 47 · JARVIS carries blockers into the final decision.

SAY
General Management does not average away a serious blocker. It identifies the conflict and names what must be resolved. The current tool cannot override a failed specialist gate with an optimistic paragraph.

DEMONSTRATE / DO TOGETHER
Use one held scenario from the previous exercises and run the full swarm. Show which specialist caused the executive hold and who owns the next action.

ASK THE ROOM
Is JARVIS the chief executive who can approve launch?

EXPECTED EVIDENCE
No. It is a synthesis agent. A human remains accountable.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 48 · Find the implementation behind each role.

SAY
A professional workflow connects behavior to a specific file. The UI is an entry point, not the whole system.

DEMONSTRATE / BUILD TOGETHER
Open catalog.py and trace one domain tool name into engine.py and business.py. Advanced pairs can propose a tool-rule change with a test; beginners use scenario and prompt edits.

ASK THE ROOM
Which file should change if the company changes its margin target field?

EXPECTED EVIDENCE
Usually the scenario input; code changes only if the business rule or schema itself changes.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 49 · Test three cases before you call it done.

SAY
A single success is not enough. Use a normal case, an invalid case and a meaningful changed business condition.

DEMONSTRATE / BUILD TOGETHER
Use TEAM_WORKBOOK.md to record all three cases. Do not broaden into real candidate or customer data.

ASK THE ROOM
What happens to an impossible survey count?

EXPECTED EVIDENCE
Validation rejects positive responses above total responses before a report is accepted.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 50 · Checkpoint 3: explain your specialist’s change.

SAY
Each pair will now explain one specialist in plain English. You do not need to describe every class or library. Show one input, one calculation and one consequence.

DEMONSTRATE / DO TOGETHER
Give pairs two minutes to prepare and invite several brief reports. Ensure all six roles are covered across the room; rotate which pair speaks.

ASK THE ROOM
Can your partner explain the result without reading the code?

EXPECTED EVIDENCE
The explanation names a concrete change, evidence and business implication.

IF SOMEONE IS STUCK
If a pair changed several values, restore the example JSON and rerun with only one edit.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 51 · Give your agents richer evidence.

SAY
This session has one practical deliverable. Deliverable: one documented multimodal test and saved evidence.

DEMONSTRATE / BUILD TOGETHER
0–15: modality and source quality. 15–40: image extraction and review. 40–60: voice or transcript workflow. 60–75: connect evidence to a question. 75–90: save Day 1 handover.

ASK THE ROOM
What will we show before the break?

EXPECTED EVIDENCE
Deliverable: one documented multimodal test and saved evidence.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 52 · Multimodal means more than typed words.

SAY
Modalities are forms of information: written text, pictures, sound and video. More input types do not automatically make an answer more reliable.

DEMONSTRATE / BUILD TOGETHER
Use a fictional packaging label or a whiteboard image. Explain what can be checked directly and what requires outside knowledge.

ASK THE ROOM
If an image is blurry, should the model fill in missing numbers?

EXPECTED EVIDENCE
No. It should mark uncertainty and request a clearer source.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 53 · Let Gemini read an image, then inspect it.

SAY
The app sends the selected image to Gemini through LangChain. It places extracted text in the editor for review; it does not save automatically.

DEMONSTRATE / BUILD TOGETHER
Use workshop/assets/command-core.png or a fictional product-label image. The decorative image should be described without fabricated business figures. For legible text, use a screenshot of the fictional scenario.

ASK THE ROOM
What evidence do you save?

EXPECTED EVIDENCE
Image filename, extraction, corrections and uncertainty. Do not claim that a visual description verifies a real business fact.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 54 · Voice is another input route, not another truth.

SAY
Speech recognition turns audio into text. A wrong transcript becomes a wrong input unless you inspect it. Browser speech recognition may contact the browser vendor.

DEMONSTRATE / BUILD TOGETHER
Try a short question about launch cash. Correct any transcription error before sending. If recognition is unsupported, import a prepared .txt transcript and continue the same evidence activity.

ASK THE ROOM
Does reading an answer aloud make it more trustworthy?

EXPECTED EVIDENCE
No. Check its sources and calculations exactly as with text.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 55 · An extraction is not a verified business fact.

SAY
Source extraction and factual verification are different jobs. Keep the original context and flag ambiguity.

DEMONSTRATE / BUILD TOGETHER
Ask pairs to find one possible extraction error and one outside claim the image cannot prove.

ASK THE ROOM
What should the source note include?

EXPECTED EVIDENCE
Source name, relevant date or context if provided, extracted text and uncertainty.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 56 · Give Jarvis one note it can cite.

SAY
Ask a grounded question about your saved note. Live Gemini can understand paraphrases, but the retrieval tool uses keyword matching, so topic words improve the search.

DEMONSTRATE / BUILD TOGETHER
Save Packaging review with fictional owner Mira and the allergen-review note. Ask who owns packaging review and request a source citation.

ASK THE ROOM
What should the answer cite?

EXPECTED EVIDENCE
The saved Packaging review note. If retrieval finds nothing, the model should say so rather than inventing an owner.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Displayed commands or code:

```text
Title: Packaging review

Fictional workshop note:
The packaging review is owned by Mira.
Allergen copy needs review before launch.

Ask: What do the memory notes say about
the packaging review owner?
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 57 · Day 1 handover: preserve your working state.

SAY
Day 2 starts from what you built today. A clone alone does not contain your private notes or local database.

DEMONSTRATE / BUILD TOGETHER
Save files and export evidence. Demonstrate uv run agentforge-jarvis backup .agentforge/day1-backup.sqlite3 using a new destination. Keep backups private.

ASK THE ROOM
What does Git preserve, and what stays in the database?

EXPECTED EVIDENCE
Source code is versioned. Runs, notes, conversations, saved blueprints and credentials are stored in the local database.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 58 · Design the company launch swarm.

SAY
This session has one practical deliverable. Deliverable: a workflow map with owners and decision rights.

DEMONSTRATE / BUILD TOGETHER
0–15: restore Day 1 and form mixed teams. 15–35: dependency map. 35–55: shared state and memory. 55–75: roles and failure design. 75–90: review the map.

ASK THE ROOM
What will we show before the break?

EXPECTED EVIDENCE
Deliverable: a workflow map with owners and decision rights.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 59 · Reconnect to yesterday’s work.

SAY
We will now connect the specialists. Keep the same section’s Day 1 and Day 2 outputs together.

DEMONSTRATE / BUILD TOGETHER
Ask each member to explain their agent’s inputs, output and biggest limitation in one minute.

ASK THE ROOM
What information does another function need from you?

EXPECTED EVIDENCE
A concrete report field or decision constraint.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 60 · The swarm follows a dependency map.

SAY
Arrows mean “needs information from,” not “these agents are chatting freely.” PRISM feeds the three specialists. Finance consumes Marketing, HR and Operations. General Management receives all five reports.

DEMONSTRATE / DO TOGETHER
Trace a supplier risk into Operations, then Finance’s deliverable-sales cap, then General Management. Explain that the app runs this dependency order sequentially even though some roles are conceptually independent.

ASK THE ROOM
Why do we not run General Management first?

EXPECTED EVIDENCE
It would lack the specialist evidence needed to synthesize a decision.

IF SOMEONE IS STUCK
Do not claim six autonomous computers or independent VMs. The app runs in one local Python process.

Sources:

- https://docs.langchain.com/oss/python/langgraph/overview
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 61 · Three kinds of information stay separate.

SAY
These stores have different jobs. Current state coordinates this run; notes provide source evidence; conversation history carries recent discussion. A label does not create an authenticated user account.

DEMONSTRATE / DO TOGETHER
Reload the page to show saved notes and runs survive. Explain that opening an archived run restores its saved scenario snapshot; a new run uses the current selected inputs.

ASK THE ROOM
Would deleting a source note erase all earlier report citations?

EXPECTED EVIDENCE
No. Earlier reports and conversations can retain snapshots.

IF SOMEONE IS STUCK
Keep only fictional content during the workshop. The local team-ID boundary is not production multi-user security.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 62 · Memory is a filing cabinet, not a mind.

SAY
Memory is saved evidence, not human recollection. The app searches topic words in a bounded set of team notes and returns excerpts.

DEMONSTRATE / BUILD TOGETHER
Inspect a successful note match and a query with no matching evidence.

ASK THE ROOM
What is the risk of keeping a stale note?

EXPECTED EVIDENCE
A future answer may cite outdated information. Update sources and review existing snapshots separately.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 63 · Every hand-off needs an explicit contract.

SAY
A hand-off is a delivery with a required payload. Do not send only a confident summary if the next step needs quantities or constraints.

DEMONSTRATE / BUILD TOGETHER
Ask teams to draw arrows and label the exact fields that travel.

ASK THE ROOM
What would break if Finance counted all target units despite a supply shortfall?

EXPECTED EVIDENCE
It would overstate sales capacity and weaken the decision.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 64 · Assign people to the decisions.

SAY
The software can propose owners in an action plan; actual accountability belongs to people who accept the work.

DEMONSTRATE / BUILD TOGETHER
Assign roles within the mixed team and write them on the workflow map.

ASK THE ROOM
Who can authorize spending in this classroom exercise?

EXPECTED EVIDENCE
No real spending is performed. The team identifies who would need to approve in a real organization.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 65 · Plan what happens when a step fails.

SAY
The app persists each specialist report. Failed or interrupted runs remain visible, but exports require a completed run. A retry is a new provider request and may cost tokens.

DEMONSTRATE / BUILD TOGETHER
Ask teams to choose one failure: bad input, quota, timeout or missing evidence. Write the expected response and owner.

ASK THE ROOM
Should the system invent a missing specialist report to keep the screen green?

EXPECTED EVIDENCE
No. A failure should remain explicit.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 66 · Run the live command center.

SAY
This session has one practical deliverable. Deliverable: a complete live swarm and inspectable decision package.

DEMONSTRATE / BUILD TOGETHER
0–15: architecture and setup. 15–40: baseline live run. 40–60: evidence and tool trace. 60–75: compare a change. 75–90: export and peer check.

ASK THE ROOM
What will we show before the break?

EXPECTED EVIDENCE
Deliverable: a complete live swarm and inspectable decision package.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 67 · From your browser to a reviewed answer.

SAY
The browser sends a request to our Python server. The server calls Gemini and the permitted tools, stores the results and streams activity back.

DEMONSTRATE / BUILD TOGETHER
Locate app.py, engine.py and storage.py. Explain API as a service counter and SQLite as the local filing system.

ASK THE ROOM
Why should the key stay on the server?

EXPECTED EVIDENCE
It grants provider access and does not need to be sent to the browser.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 68 · Run the baseline before changing anything.

SAY
A baseline gives us something fair to compare against. If we change three settings first, we cannot tell what caused a difference.

DEMONSTRATE / DO TOGETHER
Click Baseline launch and Run launch swarm. Allow the paced live run to finish; inspect the saved reports and event list afterward. Show 6/6 complete and the final recommendation.

ASK THE ROOM
Why does the baseline say conditional rather than approved?

EXPECTED EVIDENCE
It is decision support. Supply, people, customer claims and human authorization still need review.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 69 · Read the activity log like a delivery receipt.

SAY
Live models may group calls, repeat them or need one correction. Count completed tools separately from started events.

DEMONSTRATE / BUILD TOGETHER
Show read_brief, the domain tool and search_memory. An accepted report must include all three.

ASK THE ROOM
Does the trace reveal hidden reasoning?

EXPECTED EVIDENCE
No. It shows observable calls and completion events.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 70 · A useful report separates facts from judgment.

SAY
A confident paragraph is hard to audit. A report with evidence and explicit assumptions is easier to question. The narrative is displayed separately from calculated facts.

DEMONSTRATE / DO TOGETHER
Open LEDGER’s report. Show cash required, funding gap, source arithmetic, assumptions and the named Finance action.

ASK THE ROOM
Which assumption would matter in a real launch?

EXPECTED EVIDENCE
Examples include delayed customer payments, returns, taxes or supplier downtime. Those are not modelled in the default exercise.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 71 · Finance must price the plan that can happen.

SAY
Finance cannot make a coherent plan from budget alone. It needs the campaign spend, staffing allowance and actual deliverable units. These reports become tool inputs.

DEMONSTRATE / DO TOGETHER
Inspect source evidence in LEDGER: campaign allowance, staffing and the Operations delivery cap. Explain why a large demand number cannot automatically become revenue.

ASK THE ROOM
Which is the upper bound for sales in these scenarios: demand or deliverable units?

EXPECTED EVIDENCE
Sales cannot exceed either. The simplified model caps sold units at deliverable capacity.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 72 · Compare the decision, not just the screen.

SAY
The important change is not the colour of the badge. It is a mismatch between approved cash and planned spending that leads to a different recommendation.

DEMONSTRATE / DO TOGETHER
Open Run Archive, select the baseline and budget-cut checkboxes, and read the comparison. Confirm both runs use the default base inputs.

ASK THE ROOM
What must change to resolve the hold?

EXPECTED EVIDENCE
A credible revision to launch scope, cost, funding or timing that passes the relevant gates; a more optimistic prompt is not enough.

IF SOMEONE IS STUCK
If no comparison appears, select exactly two completed runs, not a failed run or three checkboxes.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 73 · Export a package someone else can inspect.

SAY
A screenshot can hide the inputs. The exported package includes the scenario and specialist detail so someone else can understand how the result was produced.

DEMONSTRATE / DO TOGETHER
Use Export brief for Markdown and JSON for structured data. Save both with a meaningful team-and-challenge filename. Read one exported section before calling the activity complete.

ASK THE ROOM
What makes this stronger evidence than a screenshot of HOLD?

EXPECTED EVIDENCE
The reviewer can see the input snapshot and the arithmetic that caused the hold.

IF SOMEONE IS STUCK
Only completed runs have executive exports. If a run failed, fix the cause and rerun instead of presenting it as a completed package.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 74 · Checkpoint: make your evidence easy to follow.

SAY
Swap exported packages with another team. They should understand the conclusion without watching your demonstration.

DEMONSTRATE / BUILD TOGETHER
Allow ten minutes to inspect each other’s evidence and ask one clarification.

ASK THE ROOM
Which missing field would make the package difficult to trust?

EXPECTED EVIDENCE
Inputs, tool arithmetic, sources, assumptions or decision owner.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 75 · Test, improve and govern the system.

SAY
This session has one practical deliverable. Deliverable: a before-and-after improvement with a test.

DEMONSTRATE / BUILD TOGETHER
0–20: reliability and limits. 20–40: adversarial tests. 40–60: fix the highest-priority issue. 60–75: speed and cost review. 75–90: evidence card.

ASK THE ROOM
What will we show before the break?

EXPECTED EVIDENCE
Deliverable: a before-and-after improvement with a test.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 76 · A human review is part of the system.

SAY
Human review is not a decorative disclaimer at the end. It is a decision step with a person who checks the evidence and owns the action.

DEMONSTRATE / DO TOGETHER
Show the accountable actions in a report. Ask who will sign off on spending, people decisions and product claims in the fictional case.

ASK THE ROOM
What would be a bad use of the candidate score?

EXPECTED EVIDENCE
Treating it as an automatic hiring decision. The system deliberately provides a review worksheet, not an employment decision.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.
- Original evidence-review illustration generated with built-in image_gen, 3 September 2026. Asset: workshop/assets/evidence-review.png.

### 77 · Try to break the workflow on purpose.

SAY
Test one failure mode deliberately, with fictional data. The model may quote malicious source text, but must not treat it as authority. Deterministic metrics and HOLD gates should remain intact.

DEMONSTRATE / BUILD TOGETHER
Run invalid survey data, an absent evidence query, and an untrusted note that says ignore the budget. Check narrative separately from tool facts.

ASK THE ROOM
Does protecting one field prove the system is fair and secure?

EXPECTED EVIDENCE
No. Record the exact behavior tested and the limits of that test.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 78 · A checkmark means one check passed.

SAY
A test has a specific claim. “Source evidence present” means the report names evidence; it is not a guarantee that the input data represents reality. A narrow honest test is more useful than an inflated safety score.

DEMONSTRATE / DO TOGETHER
Open Workshop Lab and read one check name and detail. Ask learners to explain its boundary.

ASK THE ROOM
What extra evidence would we need before real organizational use?

EXPECTED EVIDENCE
Domain review, real-data validation, live-model evaluation, security/authentication and operational testing appropriate to the use case.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 79 · Measure cost before you scale a classroom.

SAY
A token is a small piece of text processed by the model. Tools and previous reports can add input tokens. Six agents do not mean six API calls.

DEMONSTRATE / BUILD TOGETHER
Open the JSON export and inspect each report usage. Compare duration and call count. Check the actual API project quota before running many pairs together.

ASK THE ROOM
Why can repeated clicks make a classroom slower and more expensive?

EXPECTED EVIDENCE
They submit additional provider work. The app restricts concurrent requests and duplicate work within a team.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 80 · Quota errors need a service check.

SAY
A valid credential can still hit a per-minute or daily quota. Provider limits differ by project and model.

DEMONSTRATE / BUILD TOGETHER
Explain rate errors, timeout errors and invalid credentials using the troubleshooting table. Stagger groups, shorten unnecessary prompts and use approved model access.

ASK THE ROOM
Will adding “please answer” fix exhausted quota?

EXPECTED EVIDENCE
No. Resolve the service limit or wait for the allowed reset. Do not promise a reset time you have not checked.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

PROVIDER PACING: The app shares a twelve-request-per-minute limiter across Gemini agents in one process. Separate laptops or processes do not share that limiter. Use independent approved project access or stagger calls. Token and daily quotas still apply.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.
- https://ai.google.dev/gemini-api/docs/rate-limits

### 81 · Optimize the workflow without hiding uncertainty.

SAY
Optimization should preserve correctness. Caching requires careful invalidation when sources or scenarios change; this app does not claim a production response cache.

DEMONSTRATE / BUILD TOGETHER
Choose one improvement and rerun the same saved test cases. Compare output quality, latency and token usage.

ASK THE ROOM
What is a poor optimization?

EXPECTED EVIDENCE
Skipping a required specialist or reusing stale evidence to make a run look faster.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 82 · Record the evidence for your improvement.

SAY
A good evidence card tells a reviewer what changed and why it matters. It does not claim complete safety from one passing test.

DEMONSTRATE / BUILD TOGETHER
Use the template in TEAM_WORKBOOK.md. Select one team to demonstrate the before-and-after record.

ASK THE ROOM
Could another person reproduce your test?

EXPECTED EVIDENCE
Yes, using the saved input, steps and expected outcome.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 83 · Defend your launch decision.

SAY
This session has one practical deliverable. Deliverable: an assessed capstone package and individual reflection.

DEMONSTRATE / BUILD TOGETHER
0–10: brief and assign roles. 10–40: adapt the swarm. 40–50: verify evidence. 50–80: selected five-minute demos. 80–90: peer review and reflection.

ASK THE ROOM
What will we show before the break?

EXPECTED EVIDENCE
Deliverable: an assessed capstone package and individual reflection.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 84 · Your outcome challenge starts here.

SAY
This is the independent outcome check. Teams should work from their own notes and ask for help only on blocking issues.

DEMONSTRATE / BUILD TOGETHER
Give each team a challenge from the next slides. All teams submit a package; select or rotate demos to fit thirty minutes.

ASK THE ROOM
What is due before the demonstration?

EXPECTED EVIDENCE
Scenario, reports, workflow map, evidence checks and the final recommendation.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 85 · Inject a shock. Keep the base facts visible.

SAY
A challenge chip transforms the base scenario once. The underlying launch plan still needs ₹24 lakh, so the budget cut creates a ₹6 lakh gap.

DEMONSTRATE / DO TOGETHER
Restore default JSON, choose Budget −25%, run the swarm and inspect Finance. Ask learners to verify the base and effective budgets rather than assuming the chip edited the original file.

ASK THE ROOM
If we already reduced the base budget and then apply this chip, what happens?

EXPECTED EVIDENCE
The chip reduces the already edited budget again. Restore defaults for this comparison.

IF SOMEONE IS STUCK
Do not compare experiments that changed multiple inputs unless you explicitly describe all those changes.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 86 · Different shocks reveal different weak points.

SAY
Not every risk is financial. A customer-trust concern can stop promotion even when cash and capacity appear sufficient. A demand increase can expose both cash and capacity limits.

DEMONSTRATE / DO TOGETHER
Assign a different shock to each group. Have them name the first specialist whose result changes and then inspect the executive gate.

ASK THE ROOM
Which shock cannot be resolved by only increasing the budget?

EXPECTED EVIDENCE
Examples include an unresolved labelling review or an impossible delivery window without credible capacity changes.

IF SOMEONE IS STUCK
Use the default scenario for expected numbers. User-edited inputs will produce different results.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 87 · Use the proposal’s rubric to assess the work.

SAY
We are assessing learning and evidence, not awarding points for jargon. Each criterion is scored by a person. The app only calculates the weighted total.

DEMONSTRATE / DO TOGETHER
Open Workshop Lab after selecting a completed run. Explain total = sum(score/5 × criterion weight). Ask learners to include one concrete improvement in the reflection, then save.

ASK THE ROOM
Would a high score prove the app is production-ready?

EXPECTED EVIDENCE
No. This is a workshop outcome rubric, not certification.

IF SOMEONE IS STUCK
If no run is selected, open a completed run from Run Archive first.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.
- Local proposal: output/pdf/LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, Assessment Rubric.

### 88 · Tell the business story in five minutes.

SAY
A strong demonstration explains the business consequence. The audience should not need to understand every Python import.

DEMONSTRATE / BUILD TOGETHER
Ask teams to show a before-and-after metric, the relevant hand-off, and a human decision gate. Keep the timer visible.

ASK THE ROOM
What claim should you avoid?

EXPECTED EVIDENCE
That one classroom prototype autonomously ran a real company or passed a full production audit.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 89 · Turn the work into honest portfolio evidence.

SAY
Use concrete career language grounded in what you built. Avoid claims such as fully autonomous enterprise deployment unless you actually did that work.

DEMONSTRATE / BUILD TOGETHER
Example: Built a LangChain/Gemini workflow coordinating six business roles; validated cash and capacity scenarios and documented tool evidence and human review gates. Personalize it to your contribution.

ASK THE ROOM
What can you defend in an interview?

EXPECTED EVIDENCE
Your actual code change, test, decision and limitation.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 90 · Build. Test. Explain.

SAY
You now have a small agent you built and a complete workflow you can inspect. The most valuable habit is to predict, run, verify and explain.

DEMONSTRATE / DO TOGETHER
Ask each participant to write one sentence: “I changed ___; the tool showed ___; we should ___; we still need to verify ___.” Save their outputs for the next workshop session.

ASK THE ROOM
What will you be able to demonstrate without help next time?

EXPECTED EVIDENCE
A clone-and-run path, one tool calculation and a source-backed before/after decision.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 91 · When setup breaks, diagnose the layer.

SAY
Treat errors like clues. Do not respond to every problem by reinstalling everything. The error’s layer tells us the smallest useful check.

DEMONSTRATE / DO TOGETHER
Ask the learner to show the exact error and the current folder. Use the table to choose one action, then verify the expected result.

ASK THE ROOM
If the browser cannot connect, will changing a model key help?

EXPECTED EVIDENCE
No. First check that the local server is running and the address is correct.

IF SOMEONE IS STUCK
Keep a prepared offline-capable machine or pair for continuity while one person resolves network or installation issues.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 92 · Live setup: diagnose the right layer.

SAY
Keep keys out of screenshots when diagnosing setup. Model listing, configuration and successful generation are separate checks.

DEMONSTRATE / BUILD TOGETHER
Ask for the sanitized error, model name and step. Do not ask learners to post keys into a shared classroom channel.

ASK THE ROOM
When do you call live setup verified?

EXPECTED EVIDENCE
After a real response and required tool calls succeed.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 93 · Stop safely and preserve today’s work.

SAY
The database holds notes, runs, blueprints and conversations. The source files are not the whole working state. You can restart and return to the same local team.

DEMONSTRATE / DO TOGETHER
Show how to stop the server with Control+C, then restart. Explain that a backup of the data directory should be taken with the app stopped. Do not add this local data to the shared GitHub repository.

ASK THE ROOM
Which folder preserves saved runs on this machine?

EXPECTED EVIDENCE
.agentforge, unless AGENTFORGE_DATA_DIR was deliberately changed.

IF SOMEONE IS STUCK
Closing the browser is not the same as stopping the server. Stopping the server does not erase the stored data.

Displayed commands or code:

```text
# Stop the running server in its terminal:
Ctrl+C

# Restart later from the project folder:
uv run agentforge-jarvis web
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 94 · Arthi: publish the prepared project folder.

SAY
The clone link must point to a real, tested repository. The project folder is the repository root; do not accidentally upload the entire parent folder containing proposals or other applications.

DEMONSTRATE / DO TOGETHER
Follow the included publishing handout. Review staged files and ensure .env, .venv and .agentforge are excluded. Create the GitHub repository with the intended visibility and grant participants access. Use the actual remote URL shown by GitHub.

ASK THE ROOM
What must happen before sharing the clone command with the team?

EXPECTED EVIDENCE
A push succeeds and a fresh clone can install, pass tests and launch.

IF SOMEONE IS STUCK
If the remote already has commits, do not force-push. Use a fresh empty repository or integrate changes deliberately. No remote repository was published as part of creating this deck.

Sources:

- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 95 · Test the same path the team will use.

SAY
A working folder on the facilitator’s machine can hide missing files or dependencies. A fresh clone is the meaningful test of the instructions we are giving the team.

DEMONSTRATE / DO TOGETHER
Use a different empty folder. Clone the actual published URL, run these checks, and visit the localhost page. Verify the workshop folder and deck/handouts are present in the repository if you intend to share them there.

ASK THE ROOM
What does a successful local commit prove about participant access?

EXPECTED EVIDENCE
Nothing about remote access. The push and participant clone must be verified separately.

IF SOMEONE IS STUCK
Do not ask learners to clone an unverified guessed URL. Share the repository’s actual HTTPS clone link.

Displayed commands or code:

```text
# After cloning the published repository:
cd agentforge-jarvis
uv sync --frozen
uv run pytest -q
# Configure .env using LIVE_QUICKSTART.md first.
uv run agentforge-jarvis doctor
uv run python workshop/first_agent_live.py
uv run agentforge-jarvis web
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 96 · An explicit fallback keeps the lesson honest.

SAY
The main workshop uses live Gemini. If a provider outage blocks learning, you may deliberately switch to the already prepared rehearsal route. Explain that generated behavior is now scripted.

DEMONSTRATE / BUILD TOGETHER
Use the previous dry-run deck only for a declared fallback activity. Existing dependency installation still matters offline.

ASK THE ROOM
What must remain different in the evidence?

EXPECTED EVIDENCE
Provider labels and the claim being verified. Rehearsal is not evidence of live model performance.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Displayed commands or code:

```text
# macOS shell, only if Arthi switches the exercise:
export AGENTFORGE_PROVIDER=rehearsal
uv run agentforge-jarvis web

# Windows PowerShell:
$env:AGENTFORGE_PROVIDER="rehearsal"
```

Sources:

- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

### 97 · Translate the jargon into everyday language.

SAY
Use this as a quick reference if terms start to crowd out understanding. Plain language should remain accurate: software helpers are not people and a memory store is not a human mind.

DEMONSTRATE / DO TOGETHER
Ask a learner to explain one term to a partner using the example column. Add an example from their own specialization only if the required facts are available.

ASK THE ROOM
Can you explain orchestration without using the word orchestration?

EXPECTED EVIDENCE
A planned order of work that passes the right information to the next step.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- https://docs.langchain.com/oss/python/langgraph/overview
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Live workshop implementation; consult the acceptance record for verified calls.

### 98 · Your workshop files and source references.

SAY
The code and saved acceptance result define what was verified. Model quotas and deployment conditions must be checked for the actual workshop date.

DEMONSTRATE / BUILD TOGETHER
Keep the participant guide and workbook open beside the presentation. The facilitator guide contains this entire script.

ASK THE ROOM
Where do you find exact copyable commands?

EXPECTED EVIDENCE
LIVE_QUICKSTART.md and the project README.

IF STUCK
Check the current folder, saved file and exact input. Pair with a ready team while resolving setup.

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- https://ai.google.dev/gemini-api/docs/api-key
- Source: LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, sessions 1–8 and outcome rubric.
- Source: agentforge-jarvis/src/agentforge_jarvis/ and workshop/ live lab; inspected 3 September 2026.

