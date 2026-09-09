# LIBA AgentForge JARVIS — facilitator guide

A guided rehearsal with Arthi Rajendran. Prepared 3 September 2026.

## What this session builds

Learners clone a complete six-agent application, complete and run a small LangChain agent, adapt each specialist through controlled fictional scenario experiments, and produce a reviewed executive package. This is a build-along from working templates; recreating the entire web application from an empty folder is outside the three-hour route.

The PPTX is editable. Open it in PowerPoint Presenter View to see the full **Say → Demonstrate → Ask → Expected evidence → If stuck** notes. The PDF is a slide-only viewing copy. Slides 1–63 form the main sequence; 64–72 are facilitator appendices. All commands run in the folder containing `pyproject.toml`.

## Before the room arrives

1. Follow [PUBLISHING.md](PUBLISHING.md), push the project, then test the actual clone URL. If private, verify participant access. The prepared package itself does not publish a repository.
2. Open [QUICKSTART.md](QUICKSTART.md) and install Git/uv on the teaching machines using approved routes. A fresh installation needs package network access. Prepare a working pair machine for setup delays.
3. In the app project root, run `uv sync --frozen`, explicitly select rehearsal, then run `uv run pytest -q` and `uv run agentforge-jarvis doctor`.
4. Start `uv run agentforge-jarvis web`. Check `http://127.0.0.1:8787` and a complete baseline. Pick a fresh team ID such as `liba-rehearsal` for demonstration. Team IDs scope local records; they are not credentials or cross-laptop collaboration.
5. Keep PowerPoint Presenter View, a browser, an editor, and two terminal windows available. One terminal runs the server; the second runs the lab.
6. Check projection readability and audio only if you plan to use optional browser speech. Voice is not required for any checkpoint.
7. Pair learners as driver (types) and navigator (checks). Swap after the first-agent lab. Ask for green/amber signals at checkpoints.

## Three-hour route

| Time | Activity | Evidence |
|---|---|---|
| 00–15 | Concepts and common case | Explain model/tool/rehearsal simply |
| 15–40 | Clone, install, doctor, launch | Six visible agents and baseline |
| 40–65 | Complete the first-agent starter | ₹24 lakh cash; changed budget → ₹6 lakh gap |
| 65–100 | Adapt the six specializations | One changed input and expected metric |
| 100–110 | Break | Keep files and server open |
| 110–135 | Memory and hand-offs | A cited note and dependency explanation |
| 135–165 | Shock, compare, review, export | Baseline versus budget cut; saved package |
| 165–180 | Short demos and readiness | Business story, limitation, issue owner |

## Ninety-minute fast path

Assumes Git and uv are installed and package access is ready. Use slides: **1, 2, 3, 4, 7, 9, 13, 14, 16, 20, 23, 24, 25, 26, 27, 30, 32, 34, 36, 37, 40, 47, 49, 51, 53, 54, 56, 59, 61, 62**.

Allocate 10 minutes to purpose/concepts, 20 to clone and launch, 10 to the tiny-agent build, 20 to one specialization plus the swarm, 20 to memory/challenge/export, and 10 to demos/sign-off. The slides remain in their teaching order; keep each explanation short. For the coding lab, show the exact starter filename and two blanks from the quickstart even when skipping slide 31. Use the six domain pages as reference material rather than presenting every one.

## Checkpoints and expected results

| Checkpoint | Ask participants to show | Expected default evidence |
|---|---|---|
| 1 · Local readiness | Doctor + browser + baseline | Rehearsal configured; 6/6 reports; CONDITIONAL GO |
| 2 · One agent | Completed starter and budget experiment | cash 2400000; gap 0, then gap 600000 and HOLD |
| 3 · Specialist | Original value, changed value, report | Only the intended field changed; result explained |
| 4 · Final package | Two runs, note citation and export | Budget cut → ₹6 lakh gap and HOLD; source note named |

## Domain experiment answer key

Restore `examples/project-monsoon.json` and select Baseline between experiments. Edit the JSON inside Mission Control → Edit brief, apply, then run the specialist with dependencies.

| Specialist | Single edit from defaults | Expected result |
|---|---|---|
| PRISM · Analytics | `signals[0].positive`: 92 → 60 | Overall positive rate 229/360 = 63.6% |
| PULSE · Marketing | `marketing_budget`: 180000 → 90000 | Channel allocations sum to ₹90,000 |
| NOVA · HR | `required_fte`: 10 → 12 | 4 FTE gap and ₹40,000 staffing allowance |
| ATLAS · Operations | `production_per_day`: 600 → 400 | 96 days needed; 4,800 units short by day 84 |
| LEDGER · Finance | `price`: 120 → 90 | 27.8% margin; fails 38% target; HOLD |
| JARVIS · Management | Default scenario + Budget −25% chip | ₹6 lakh funding gap survives into final HOLD |

These are fictional, simplified teaching calculations. An agent blueprint saves narrative instructions, but the rehearsal model follows a fixed script. Change inputs or Python tools to change calculated behavior today. Testing a live model is a separate exercise.

## Team submission template

- Team and specialist:
- Business question:
- Original input → changed input:
- Prediction before running:
- Actual tool result and source:
- Executive decision and review owner:
- One assumption or limitation:
- Paths to exported Markdown and JSON:
- One next improvement:

## Rehearsal issue log

| Time / team | OS and step | Exact symptom | Impact | Owner | Next action | Retest evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

Choose Ready, Ready with conditions, or Not ready for the intended classroom setup. A local test does not establish participant GitHub access, Windows execution, microphone capture, live inference or 200-user hosting.

## Full slide-by-slide facilitation notes

### 01 · Build your AI business team.

**90-minute route**

SAY
Today we will assemble a working AI-agent workflow from a prepared repository. We will use simple business examples and check what actually happened.

DEMONSTRATE / DO TOGETHER
Open Presenter View so these notes remain private. Keep the app and a terminal ready in separate windows. Share the actual GitHub repository link only after publishing and testing it.

ASK THE ROOM
Who has used a chatbot? Who has opened a terminal?

EXPECTED EVIDENCE
A show of hands tells you which pairs need setup support.

IF SOMEONE IS STUCK
Pair a confident terminal user with someone new. This is a rehearsal, not a coding-speed competition.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.
- Original illustration generated with the built-in image_gen tool, 3 September 2026. Asset: workshop/assets/command-core.png.

### 02 · By the end, your laptop runs the team.

**90-minute route**

SAY
A successful session ends with something you can show, not just a list of AI words. We will use templates, complete a small piece of code, and then inspect a six-agent system.

DEMONSTRATE / DO TOGETHER
Point to the four outcomes. Tell participants they should keep their terminal output, one changed report and one export.

ASK THE ROOM
What would count as proof that your agent worked?

EXPECTED EVIDENCE
They name a tool result or a saved package, not just an attractive screen.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 03 · Today is a flight simulator for agents.

**90-minute route**

SAY
A flight simulator uses a real control system with a simulated flight. Our rehearsal adapter follows a fixed script; the tools still run and produce real calculations. It does not understand arbitrary language like a live model.

DEMONSTRATE / DO TOGETHER
Show the REHEARSAL MODE badge. Mention that initial installation still needs internet; offline operation comes after dependencies are installed.

ASK THE ROOM
If I rewrite a blueprint prompt, will the rehearsal answer become more creative?

EXPECTED EVIDENCE
No. Rehearsal wording is scripted. Input changes affect calculations; live models can interpret narrative preferences.

IF SOMEONE IS STUCK
Repeat this distinction whenever someone expects a creative response. Never present the rehearsal as a verified live Gemini call.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 04 · We will learn by doing one small loop.

**90-minute route**

SAY
I will demonstrate one small action, then everyone repeats it. Please avoid racing through later steps: the checkpoint is how we know the room is ready.

DEMONSTRATE / DO TOGETHER
Assign driver and navigator in each pair. Driver types; navigator reads the instruction and checks the output. Ask pairs to signal green when ready, amber when blocked.

ASK THE ROOM
What should the navigator check before we run a command?

EXPECTED EVIDENCE
Correct folder, exact command, and the expected output.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 05 · Use the route that fits your session.

SAY
This deck supports a three-hour build-along. If today is only ninety minutes, use the fast-path slide list in the facilitator guide and assume Git and uv are already installed.

DEMONSTRATE / DO TOGETHER
Choose the route before teaching. Keep technical appendices for troubleshooting rather than reading every slide aloud.

ASK THE ROOM
Can we agree to stop and check at each checkpoint?

EXPECTED EVIDENCE
The room understands the cadence.

IF SOMEONE IS STUCK
If installation consumes the first block, pair affected learners or use the prepared ZIP. Do not promise that a first-time dependency installation works offline.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 06 · Think of agents as a kitchen team.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.
- Original kitchen-team illustration generated with built-in image_gen, 3 September 2026. Asset: workshop/assets/kitchen-team.png.

### 07 · An agent can use a tool before replying.

**90-minute route**

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
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 08 · An agent needs a clear job description.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 09 · The loop is: ask, act, observe, reply.

**90-minute route**

SAY
The model requests an action. LangChain executes the permitted tool and returns its output. The agent can then continue or finish. The rehearsal adapter chooses the next action using fixed rules.

DEMONSTRATE / DO TOGETHER
Trace one Finance request from a user message to model_finances to the final report. Explain that the activity log is visible behavior, not hidden model reasoning.

ASK THE ROOM
Does seeing a tool call mean the answer is automatically trustworthy?

EXPECTED EVIDENCE
No. We need valid inputs, correct tools and a reviewable final claim.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

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
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

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
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 13 · Six specialists answer six questions.

**90-minute route**

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 14 · Our shared case is Project Monsoon.

**90-minute route**

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 16 · Prepare a simple local workstation.

**90-minute route**

SAY
We need a small local development setup. An editor can be VS Code or another editor you already have. Rehearsal needs no model API key, paid subscription, GPU or Docker.

DEMONSTRATE / DO TOGETHER
Check Git and uv versions first. Ask the room to keep a terminal open and connect power. Use the existing workshop device baseline: recent laptop, around 8 GB RAM minimum for this lab.

ASK THE ROOM
Which step may still need internet even though today’s model is offline?

EXPECTED EVIDENCE
Downloading Python and packages during setup.

IF SOMEONE IS STUCK
Use institution-approved installation methods. If software installation is blocked, pair the learner with a ready machine; do not bypass IT controls.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 17 · GitHub is the shared shelf. Clone is a copy.

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

### 18 · macOS: install only what is missing.

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

Displayed code / text:

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

### 19 · Windows: use PowerShell for setup.

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

Displayed code / text:

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

### 20 · Clone the link Arthi gives you.

**90-minute route**

SAY
We have not assumed a public repository URL. I will share the tested HTTPS URL. Build one command containing git clone, that URL and the destination folder name agentforge-jarvis.

DEMONSTRATE / DO TOGETHER
Type git clone followed by a space, paste the real URL, add a space and agentforge-jarvis, then press Enter. Next run cd agentforge-jarvis and list the files. PowerShell also supports ls.

ASK THE ROOM
What file confirms we are in the project root?

EXPECTED EVIDENCE
pyproject.toml. uv.lock, README.md and src should also be visible.

IF SOMEONE IS STUCK
If the directory already exists, use it only if it is the intended clone; otherwise choose a fresh folder. A 404 for a private repository may be an access problem.

Displayed code / text:

```text
cd agentforge-jarvis
ls
```

Sources:

- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 21 · Know the few files you will touch.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 22 · uv prepares a separate toolbox for this app.

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
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 23 · Install the locked dependencies once.

**90-minute route**

SAY
Run these commands from the folder containing pyproject.toml. The first may download Python and packages. The second runs the app’s existing automated checks.

DEMONSTRATE / DO TOGETHER
Wait for sync to finish. Then run pytest. The prepared app currently reports 19 tests; if we later add a test, the count may grow. Success means tests pass, not that the count must stay fixed forever.

ASK THE ROOM
What does a green test suite prove, and what does it not prove?

EXPECTED EVIDENCE
It checks the defined rehearsal behavior. It does not prove live Gemini access, microphone support or production readiness.

IF SOMEONE IS STUCK
A “no pyproject.toml found” error means the terminal is in the wrong folder. Stop and use cd; do not reinstall Python.

Displayed code / text:

```text
uv sync --frozen
uv run pytest -q
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 24 · Force rehearsal mode before the health check.

**90-minute route**

SAY
The app defaults to rehearsal, but an old environment setting could select a different provider. We explicitly choose rehearsal in the terminal that will start the server.

DEMONSTRATE / DO TOGETHER
Use the command for the operating system, then run doctor. Explain that live_verified remains false because a configuration check is not a live provider call.

ASK THE ROOM
Should we enter a Gemini key to complete today’s rehearsal?

EXPECTED EVIDENCE
No. We do not need one.

IF SOMEONE IS STUCK
If doctor reports Gemini, verify the environment variable in the same terminal. Editing .env does not override a provider variable already set in the shell.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 25 · Launch the app and keep this terminal open.

**90-minute route**

SAY
The terminal is now running the local web server. The URL belongs in the browser address bar, not in the terminal. Keep the server running while you use the app.

DEMONSTRATE / DO TOGETHER
Start the server, wait for the Uvicorn startup line, then open the URL. Explain localhost as “this computer” and port 8787 as its application door number.

ASK THE ROOM
Can another laptop use your 127.0.0.1 address to reach this app?

EXPECTED EVIDENCE
No. On their laptop it refers to their own computer.

IF SOMEONE IS STUCK
If the port is busy, start with --port 8788 and open that port in the browser. Do not assume a browser reload can restart a stopped server.

Displayed code / text:

```text
uv run agentforge-jarvis web

http://127.0.0.1:8787
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 26 · Checkpoint 1: everyone can see six agents.

**90-minute route**

SAY
Before we build further, we need the whole room at the same starting line. “It installed” is not enough; the app must open.

DEMONSTRATE / DO TOGETHER
Ask pairs to show their page or signal green. Resolve amber pairs now. Set a simple local team ID such as liba-team-01; choose a different ID if useful on a shared machine.

ASK THE ROOM
Does using the same team ID connect different laptops?

EXPECTED EVIDENCE
No. This is local workspace separation, not shared networking.

IF SOMEONE IS STUCK
Use the setup-rescue appendix. If a pair cannot install today, let them drive the facilitator’s demo or work with a ready partner.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 27 · Run the baseline before changing anything.

**90-minute route**

SAY
A baseline gives us something fair to compare against. If we change three settings first, we cannot tell what caused a difference.

DEMONSTRATE / DO TOGETHER
Click Baseline launch and Run launch swarm. Rehearsal is fast; use the saved reports and event list to inspect afterward. Show 6/6 complete and the final recommendation.

ASK THE ROOM
Why does the baseline say conditional rather than approved?

EXPECTED EVIDENCE
It is decision support. Supply, people, customer claims and human authorization still need review.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 28 · Read the activity log like a delivery receipt.

SAY
The trace tells us which functions executed. It does not show private thoughts or prove every statement is true. Started and completed events are separate; do not confuse event count with tool-completion count.

DEMONSTRATE / DO TOGETHER
Open the telemetry and point to read_brief, the domain tool and search_memory for one specialist. The full run has 18 tool completions but additional start/end events.

ASK THE ROOM
Where do we look for the actual arithmetic?

EXPECTED EVIDENCE
The agent’s report under source evidence and calculated metrics.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 29 · A useful report separates facts from judgment.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 30 · Now build one small agent yourself.

**90-minute route**

SAY
The full application is already assembled from working templates. Now we will create a smaller agent so you can recognize its parts without reading the whole application.

DEMONSTRATE / DO TOGETHER
Keep the app open. In the editor, open workshop/first_agent_starter.py. Use a second terminal in the project root for the lab.

ASK THE ROOM
What are the three pieces we expect to see?

EXPECTED EVIDENCE
A model, a tool, and create_agent connecting them.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 31 · Open the starter and find the two blanks.

SAY
The starter has two incomplete calculation lines. The rest of the framework code is provided. You do not need to type every import or understand the model adapter internals today.

DEMONSTRATE / DO TOGETHER
Open the file in an editor. Locate cash_needed = None and funding_gap = None. Explain None as a deliberately empty value. Do not run this incomplete starter as a successful agent.

ASK THE ROOM
Which inputs should produce the same ₹24 lakh baseline we checked earlier?

EXPECTED EVIDENCE
30,000 units at ₹65 plus ₹4.5 lakh other costs.

IF SOMEONE IS STUCK
The completed reference is workshop/first_agent.py. Let learners compare it after making their own attempt.

Displayed code / text:

```text
workshop/first_agent_starter.py

BUDGET = 2_400_000
UNITS = 30_000
UNIT_COST = 65
OTHER_LAUNCH_COSTS = 450_000
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 32 · Complete the calculator in two lines.

**90-minute route**

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

Displayed code / text:

```text
cash_needed = UNITS * UNIT_COST + OTHER_LAUNCH_COSTS

funding_gap = max(0, cash_needed - BUDGET)
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

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

Displayed code / text:

```text
@tool
def estimate_launch_cash() -> dict:
    """Calculate launch cash and compare the budget."""
    cash_needed = UNITS * UNIT_COST + OTHER_LAUNCH_COSTS
```

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.
- Local teaching source: workshop/first_agent_starter.py and workshop/first_agent.py.

### 34 · create_agent connects the working parts.

**90-minute route**

SAY
Read the code as a sentence: create an agent using this rehearsal model, allowing this cash tool, and giving it a role instruction. Square brackets mean a list of allowed tools.

DEMONSTRATE / DO TOGETHER
Point out that WorkshopModel is a supplied helper in workshop/rehearsal_model.py. Its fixed action is to call estimate_launch_cash. This simple lab is separate from the app’s richer RehearsalModel.

ASK THE ROOM
What happens if we remove the tool from the allowed tool list?

EXPECTED EVIDENCE
The model cannot successfully execute that named capability through this agent.

IF SOMEONE IS STUCK
Do not spend the session reading the model class. Keep attention on the model/tool/prompt interface.

Displayed code / text:

```text
agent = create_agent(
    model=WorkshopModel(),
    tools=[estimate_launch_cash],
    system_prompt="Use the cash tool. A human decides.",
)
```

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- Local teaching source: workshop/first_agent.py; workshop/rehearsal_model.py.

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

Displayed code / text:

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

**90-minute route**

SAY
A working result should agree with our manual calculation. This proves that your tool ran through LangChain’s agent loop. It does not prove open-ended reasoning.

DEMONSTRATE / DO TOGETHER
Run the completed starter in the second terminal. Ask each pair to show the three output fields. The reference file can be run with uv run python workshop/first_agent.py if needed.

ASK THE ROOM
Why is the recommendation still a human review even with zero funding gap?

EXPECTED EVIDENCE
The tool only checked cash; it cannot authorize a business decision.

IF SOMEONE IS STUCK
If the response mentions an unfinished build step, one None remains. If import fails, verify that uv sync completed and the command runs from the project root.

Displayed code / text:

```text
uv run python workshop/first_agent_starter.py

# Expected result after completing the blanks:
"cash_needed_inr": 2400000
"funding_gap_inr": 0
"recommendation": "REVIEW WITH A HUMAN"
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 37 · Change one number. Predict before you run.

**90-minute route**

SAY
This is the scientific habit we want: make a prediction, change one input, run the system, and compare actual evidence.

DEMONSTRATE / DO TOGETHER
Have learners change BUDGET from 2_400_000 to 1_800_000 in their starter. Ask them to say the expected gap before executing. Then restore the starter budget or keep a named copy of the experiment.

ASK THE ROOM
Did the model invent the ₹6 lakh gap?

EXPECTED EVIDENCE
No. Python calculated it. The rehearsal model returned the tool’s result.

IF SOMEONE IS STUCK
Remember that editing this small lab does not change the web app’s scenario. The next activity modifies the application separately.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 39 · Build the agent blueprint before tuning it.

SAY
A blueprint is the agent’s contract: goal, inputs, tools, dependencies and constraints. The app lets each local team save extra instructions. In rehearsal those instructions do not alter the scripted wording or arithmetic.

DEMONSTRATE / DO TOGETHER
Open PRISM’s blueprint, read the goal and dependencies, and save a simple instruction such as “Explain the biggest limitation in one sentence.” Explain that its narrative effect needs a live model later.

ASK THE ROOM
How can we change behavior today in a measurable way?

EXPECTED EVIDENCE
Change scenario inputs, or edit and test an underlying Python tool.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 40 · Use a fresh baseline for every experiment.

**90-minute route**

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 41 · PRISM turns counts into a useful signal.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 42 · PULSE turns signals into a testable campaign.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 43 · NOVA shows capacity and skills for review.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 44 · ATLAS checks whether the promise fits time.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 45 · LEDGER checks more than cash availability.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 46 · JARVIS carries blockers into the final decision.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 47 · Checkpoint 3: explain your specialist’s change.

**90-minute route**

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 48 · Memory is a filing cabinet, not a mind.

SAY
The vault stores text so agents can retrieve it later. Retrieval is a way to supply evidence, not proof that the source is true. Our implementation uses keyword overlap and bounded excerpts.

DEMONSTRATE / DO TOGETHER
Explain RAG in simple terms: find relevant material, then give it to the answering system. Avoid claiming this app uses embeddings or semantic vector search.

ASK THE ROOM
Can a saved note be wrong?

EXPECTED EVIDENCE
Yes. We still need to inspect its origin and treat it as evidence, not authority.

IF SOMEONE IS STUCK
Pause for one pair to show the checkpoint before continuing.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 49 · Give Jarvis one note it can cite.

**90-minute route**

SAY
We will ask a question whose answer is in our own evidence. The owner is fictional and is deliberately included in the note.

DEMONSTRATE / DO TOGETHER
Open Memory Vault, enter the title and text, and save. Then ask the exact question in the JARVIS command channel. It includes “memory notes” so rehearsal’s simple routing chooses search_memory.

ASK THE ROOM
What source should appear with the answer?

EXPECTED EVIDENCE
Packaging review, with an excerpt naming Mira.

IF SOMEONE IS STUCK
An unrelated prompt may route differently in rehearsal. Use a memory keyword and the same topic words. Never describe this as unrestricted natural-language understanding.

Displayed code / text:

```text
Title: Packaging review

Fictional workshop note:
The packaging review is owned by Mira.
Allergen copy needs review before launch.

Ask: What do the memory notes say about
the packaging review owner?
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 50 · Three kinds of information stay separate.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 51 · The swarm follows a dependency map.

**90-minute route**

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
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 52 · Finance must price the plan that can happen.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 53 · Inject a shock. Keep the base facts visible.

**90-minute route**

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 54 · Compare the decision, not just the screen.

**90-minute route**

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 55 · Different shocks reveal different weak points.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 56 · A human review is part of the system.

**90-minute route**

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.
- Original evidence-review illustration generated with built-in image_gen, 3 September 2026. Asset: workshop/assets/evidence-review.png.

### 57 · Try to break the workflow on purpose.

SAY
Red-teaming means deliberately testing failure modes. It is not about proving the system is perfectly safe. The deterministic tool gates protect specific behavior; live model prose can still require further checks.

DEMONSTRATE / DO TOGETHER
Give each pair one test. Record input, expected output, actual evidence and a fix or limitation. For prompt injection, treat the note as untrusted source text; do not act on its instruction.

ASK THE ROOM
Does refusing an age field prove the entire HR workflow is fair?

EXPECTED EVIDENCE
No. Work samples and skills can still be biased or inaccessible.

IF SOMEONE IS STUCK
If testing a live model later, evaluate its narrative separately. Rehearsal does not establish resistance of a different model.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 58 · A checkmark means one check passed.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 59 · Export a package someone else can inspect.

**90-minute route**

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 60 · Use the proposal’s rubric to assess the work.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.
- Local proposal: output/pdf/LIBA_AgentForgeWorkshop_Proposal_Revised_2-Day.pdf, Assessment Rubric.

### 61 · Tell the story in three minutes.

**90-minute route**

SAY
A clear demo is a small story. We started with this goal, changed this input, observed this evidence and reached this conditional conclusion. Avoid a tour of every button.

DEMONSTRATE / DO TOGETHER
Give each pair thirty seconds for the goal, forty-five for the change, sixty for evidence and forty-five for the decision and limitation. Choose several representative teams to present.

ASK THE ROOM
Could a business colleague understand your explanation without knowing Python?

EXPECTED EVIDENCE
Yes. They should understand the decision, the evidence and the remaining uncertainty.

IF SOMEONE IS STUCK
If time is short, ask every pair to submit its package and select two live demos.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 62 · Decide what is ready for the real workshop.

**90-minute route**

SAY
Today’s rehearsal is also a test of our teaching flow. A technical success on my laptop is not enough if the room cannot follow it.

DEMONSTRATE / DO TOGETHER
Collect a short issue log: symptom, machine/OS, exact step, effect, owner and next action. Decide Ready, Ready with conditions, or Not ready for the planned classroom setup.

ASK THE ROOM
What is the highest-priority issue to fix before students arrive?

EXPECTED EVIDENCE
A concrete issue tied to participation or correctness, with an owner.

IF SOMEONE IS STUCK
Do not claim GitHub access, Windows execution, microphone support or live inference was verified unless the team actually exercised it.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 63 · Keep the evidence. Carry the learning forward.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 64 · Appendix: the 90-minute route.

SAY
This is the abbreviated route. Use the FAST PATH markers and the exact slide list in the guide. Do not read the setup appendix if everyone is already prepared.

DEMONSTRATE / DO TOGETHER
Allocate 10 minutes to purpose/concepts, 20 to clone and launch, 10 to the tiny-agent build, 20 to one domain plus the swarm, 20 to challenge/memory/export, and 10 to demos/sign-off.

ASK THE ROOM
What can we defer if the room is behind?

EXPECTED EVIDENCE
Detailed individual domain walkthroughs and optional voice; keep the first successful run, one real code change, a challenge and exported evidence.

IF SOMEONE IS STUCK
If setup is not complete, ninety minutes may not fit the coding lab. Say what was deferred rather than claiming the whole build was completed.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 65 · When setup breaks, diagnose the layer.

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

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 66 · Use offline mode only after preparing it.

SAY
Offline-first does not mean a fresh laptop can conjure its dependencies without a download. The first install needs cached packages or an approved network. The app then runs rehearsal locally.

DEMONSTRATE / DO TOGETHER
Distinguish source ZIP, installed .venv and uv’s package cache. A source ZIP is a fallback for Git access; it is not a replacement for dependency installation.

ASK THE ROOM
What should we prepare before entering an unreliable-network classroom?

EXPECTED EVIDENCE
Install and test on the teaching devices or ready paired machines; keep the source and verified examples accessible.

IF SOMEONE IS STUCK
Do not copy a macOS .venv to Windows and assume it is portable. Install on each target platform.

Displayed code / text:

```text
# First installation: needs package access
uv sync --frozen

# Later, with the required cache already present:
uv sync --frozen --offline
uv run --offline agentforge-jarvis web
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 67 · Stop safely and preserve today’s work.

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

Displayed code / text:

```text
# Stop the running server in its terminal:
Ctrl+C

# Restart later from the project folder:
uv run agentforge-jarvis web
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 68 · Arthi: publish the prepared project folder.

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
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 69 · Test the same path the team will use.

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

Displayed code / text:

```text
# After cloning the published repository:
cd agentforge-jarvis
uv sync --frozen
uv run pytest -q
uv run agentforge-jarvis doctor
uv run agentforge-jarvis web
```

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 70 · Live AI is a later, separate experiment.

SAY
Moving from a scripted adapter to a live model changes the behavior we must test. Provider availability, quota, privacy and tool support need a separate check. Keep today’s rehearsal key-free.

DEMONSTRATE / DO TOGETHER
Point to the README’s Gemini and Ollama sections. Explain that live model IDs must be available in the chosen account or installed locally. Never paste keys into the deck, chat or Memory Vault.

ASK THE ROOM
Which results need retesting with a live model?

EXPECTED EVIDENCE
Tool use, source grounding, narrative quality, failure handling, latency and relevant safety boundaries.

IF SOMEONE IS STUCK
A configured flag is not a successful inference. Use demo --live only when a model is actually configured and you intend to make the call.

Sources:

- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 71 · Translate the jargon into everyday language.

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
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

### 72 · Keep the source instructions close at hand.

SAY
All application claims in this deck are grounded in the local implementation. External sources are official documentation, cited in the relevant speaker notes. Generated illustrations are visual analogies, not factual diagrams.

DEMONSTRATE / DO TOGETHER
Keep the quickstart and publishing handout available beside the deck. Use the source code and verified outputs when a question depends on exact behavior.

ASK THE ROOM
Where should we look if the slide summary and current code ever diverge?

EXPECTED EVIDENCE
Inspect and verify the current code and its tests, then update the deck.

IF SOMEONE IS STUCK
Before a future session, rerun the setup and baseline checks. Dependency availability and provider behavior can change.

Sources:

- https://docs.langchain.com/oss/python/langchain/agents
- https://docs.langchain.com/oss/python/langgraph/overview
- https://docs.astral.sh/uv/getting-started/installation/
- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
- https://git-scm.com/install/mac
- https://git-scm.com/install/windows
- Local source: agentforge-jarvis/src/agentforge_jarvis/engine.py; business.py; models.py; providers.py; app.py. Rehearsal behavior verified locally on 3 September 2026.

