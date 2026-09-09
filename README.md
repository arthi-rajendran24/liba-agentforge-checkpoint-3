# AgentForge / JARVIS

**Six minds. One mission.** A live Gemini command center for the LIBA workshop: six LangChain specialists, a LangChain command assistant, and a LangGraph company-launch workflow.

## Start the live app

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), clone the repository, then run all commands inside the folder containing `pyproject.toml`:

```sh
git clone https://github.com/arthi-rajendran24/agentforge.git agentforge-jarvis
cd agentforge-jarvis
uv sync --frozen
```

Copy `.env.example` to `.env` (`cp` on macOS/Linux, `Copy-Item` in PowerShell). Add your approved Gemini key privately. Keep the tested defaults:

```dotenv
AGENTFORGE_PROVIDER=gemini
AGENTFORGE_MODEL=gemini-3.1-flash-lite
GEMINI_API_KEY=your-own-key
AGENTFORGE_GEMINI_RPM=12
```

Then run:

```sh
uv run agentforge-jarvis doctor
uv run python workshop/first_agent_live.py
uv run agentforge-jarvis web
```

Open **http://127.0.0.1:8787**. Doctor checks configuration; the lab makes a real Gemini call. The UI marks live access verified after a successful provider response. Restart after editing `.env`; existing shell variables take precedence. Python 3.12 is selected automatically. The app needs no Node.js build, GPU or database server.

## Teach the main workshop

**Learning on your own? Start with the [complete self-guided handbook](workshop/SELF_GUIDED_WORKSHOP.md).** Written as Arthi guiding you through each step, it covers setup on Windows/macOS, the first LangChain agent, all six specialist experiments, source review, saved workflows, challenge answers, troubleshooting and the final portfolio. Download the [editable Word handbook](workshop/LIBA_AgentForge_Self_Guided_Handbook.docx) for offline reading and notes.

For the running application, use the [complete illustrated usage manual](workshop/AgentForge_JARVIS_Complete_Usage_Manual.docx). It covers every screen and control, all six agents, built-in and custom scenarios, run comparison, memory, live Gemini image extraction, retrieval chat, voice, exports, governance, assessment, team access, hosting, backup, troubleshooting, eleven experiments and a self-guided dry run. The [captured application screens](workshop/usage-screenshots/) are included for teaching and offline reference.

Before the workshop, share the [student Gemini and Telegram prerequisites](workshop/AgentForge_Student_Prerequisites_Gemini_Telegram.docx). It guides students through creating a Gemini API key and a BotFather Telegram bot while keeping both credentials private; the institute IT team handles the lab software.

The three [cumulative Day 1 checkpoints](workshop/CHECKPOINT_PATH.md) now use this repository's `agentforge_jarvis` package, six canonical domain identifiers and LangChain tool-calling pattern. Checkpoint 1 contains the deterministic teaching tools. Checkpoint 2 adds one real LangChain agent loop and a small FastAPI interface. Checkpoint 3 is the complete repository represented by this branch. The synchronization test prevents the published Checkpoint 3 tree from drifting from this repository.

The **98-slide Main Workshop deck** covers the proposal's two days and eight ninety-minute sessions, with original generated illustrations, editable flow diagrams and full presenter notes.

- [Main PowerPoint](workshop/slides/LIBA_AgentForge_JARVIS_Main_Workshop.pptx)
- [PDF viewing copy](workshop/slides/LIBA_AgentForge_JARVIS_Main_Workshop.pdf)
- [Participant live quickstart](workshop/LIVE_QUICKSTART.md)
- [Full facilitator script and answer key](workshop/MAIN_FACILITATOR_GUIDE.md)
- [Team activities and evidence workbook](workshop/TEAM_WORKBOOK.md)
- [Publish and verify the GitHub clone path](workshop/PUBLISHING.md)

Learners build from working templates: complete a small live LangChain agent, customize specialists, inspect calculations, add reviewed image/voice evidence, connect the swarm and defend a final decision. Day 2 reuses Day 1's code, notes and team workspace. The earlier 72-slide Dry Run deck remains a clearly labelled rehearsal fallback.

## The six agents

| Agent | Proposal specialization | Working tool and output |
|---|---|---|
| **PRISM** | Analytics | `analyze_signals`: channel denominators, weighted sentiment change, descriptive Wilson interval, KPI recommendations |
| **PULSE** | Marketing | `plan_marketing`: trend/sentiment hand-off, exact budget allocation, labelled campaign drafts, trust review |
| **NOVA** | HR | `screen_skills`: anonymous skills coverage, work-sample worksheet, staffing gap and cost; human review throughout |
| **ATLAS** | Operations | `assess_supply`: lead time, production capacity, shortfall, delivery buffer and fallback |
| **LEDGER** | Finance | `model_finances`: upfront cash needs, margin, break-even, downside/base/upside cases constrained by delivery capacity |
| **JARVIS** | General Management | `synthesize_strategy`: reconcile five reports, preserve hold gates, assign owners and produce the executive package |

The additional JARVIS **command interface** is a LangChain agent that can consult specialists, retrieve team notes and read the latest saved run. It is separate from the General Management synthesis agent. Use Mission Control to change scenario values and start saved swarm runs.

## Working features

- Run the complete team or one specialist with its dependencies; inspect live tool events, calculations and model prose.
- Apply budget, supplier, trust or demand shocks; edit/import validated scenario JSON; compare and export saved runs.
- Save source notes and retrieve bounded keyword-matched excerpts with citations. Team/agent conversations and blueprints persist in SQLite.
- Send a selected PNG/JPEG under 2 MB to Gemini for text extraction, review it, then explicitly save the note. Use the fictional `workshop/assets/monsoon-case.png` sample.
- Optional browser voice transcription and read-aloud; review recognized text before sending. Browser support varies.
- Record human scores using the proposal's 25/25/20/15/15 rubric and include the reflection in exports.

## Live verification

Verified locally on **3 September 2026** with Gemini **3.1 Flash-Lite**: all six agents completed baseline and budget-cut runs; Finance preserved the INR 600,000 gap and General Management returned HOLD; memory chat cited Mira's packaging note; a saved blueprint changed the live narrative; image extraction read the fictional case figures correctly. The completed first-agent lab called its real Python tool through Gemini.

Sanitized evidence is in [examples/live-verification.json](examples/live-verification.json) and [examples/live-image-verification.json](examples/live-image-verification.json). [Verification details](docs/VERIFICATION.md) distinguish tested behavior from deployment conditions. Automated tests use controlled rehearsal inputs and do not spend model quota.

## Service controls

Authentication is available for local use and required in production mode. Team access codes are PBKDF2-hashed; random server sessions are hashed and expire after twelve hours. Signed-in requests cannot select another team's records. Production cookies are Secure, HttpOnly and SameSite=Strict. Host allowlists, same-origin checks, input limits and request limits apply.

The server admits one active request per team, two executing saved runs, eight run slots including queued work, and two concurrent chats/image requests. All Gemini model instances share a **12 requests/minute** pacer in this single process. Set `AGENTFORGE_GEMINI_RPM` only against the actual approved project quota. This does not coordinate separate laptops/processes and does not remove token or daily quotas. During preparation an overlapping process hit a reported 15 RPM limit; the app now paces its own calls. [Google's quota documentation](https://ai.google.dev/gemini-api/docs/rate-limits) explains project-wide limits.

Provider requests have timeouts and limited retries. Reports persist after each specialist; restart recovery marks incomplete runs interrupted. Missing required tools receive one correction turn. Errors stay explicit and redacted; there is no silent fallback to simulation. Cancellation takes effect between active calls. Usage fields record reported input/output/total tokens, not invoiced cost.

`/api/health` checks the service; `/api/ready` checks storage and requires a successful live response since this process started. Readiness is observed state, not a continuous provider guarantee.

## Host and operate

Use [deploy/README.md](deploy/README.md) for team provisioning, a non-root Docker/Caddy HTTPS recipe, backup and restore. Local loopback mode leaves authentication optional; team IDs alone are workspace labels in that mode. Hosted mode forces authentication and explicit host validation.

```sh
uv run agentforge-jarvis provision-team liba-team-01 --output .agentforge/team-01-access.txt
uv run agentforge-jarvis backup .agentforge/workshop-backup.sqlite3
```

Both commands create new private files without overwriting. Re-provisioning rotates the team's code and revokes sessions. The database is `.agentforge/agentforge.sqlite3`; keep it and backups private. Run **one app process** against a database. A real cloud host, DNS, TLS and class-scale quota/load must be verified on the selected infrastructure; the supplied Docker recipe has not been built on this Mac.

## Architecture

```text
Local browser HUD + optional speech
          │ same-origin HTTP / SSE
FastAPI + SQLite team workspace
          │
LangGraph workflow (dependency-ordered, sequential)
          PRISM
            ↓
    PULSE → NOVA → ATLAS
            ↓
          LEDGER
            ↓
          JARVIS → executive package + human review
```

PULSE, NOVA and ATLAS all receive PRISM’s report. LEDGER receives Marketing, HR and Operations reports. General Management receives all five specialist reports. Execution is sequential to keep workshop traces and local resource use predictable; the three specialists do not depend on each other. Two saved runs can execute at once; the queue holds at most eight submitted runs. Agent loops have bounded graph steps and tool calls; provider requests have timeouts. Cancellation takes effect between calls after any active model call returns.

Every domain is constructed with **`langchain.agents.create_agent`**, a role prompt, `read_brief`, its domain tool, and `search_memory`. The command assistant uses the LangChain agent-as-tool pattern. Model instances and transcripts are scoped to each invocation; stored conversation history is scoped to team and agent. This is one local Python process, not six computers or VMs.

```text
src/agentforge_jarvis/
  catalog.py      names, capabilities, proposal rubric
  models.py       validated scenarios and report schemas
  business.py     six auditable business calculations
  providers.py    rehearsal / Gemini / Ollama adapters
  engine.py       LangChain agents, LangGraph orchestration, exports
  storage.py      team-scoped SQLite persistence
  app.py          local HTTP API, event stream and input boundaries
  static/        complete responsive HUD, no CDN dependencies
docs/            workshop guide, proposal mapping and verification
examples/        scenario, source note and computed sample packages
tests/           agent, arithmetic, persistence and HTTP tests
```

## Verify and package

```sh
uv run pytest -q
uv run ruff check src tests
uv run agentforge-jarvis demo --challenge budget-cut
uv build
```

`demo` without `--live` intentionally uses the deterministic rehearsal adapter. For a deliberate full live acceptance test (uses quota):

```sh
uv run python scripts/verify_live.py
```

Do not run this in another process while a live browser swarm is active on a low-quota project. The acceptance script writes fictional, sanitized evidence only. Dependencies are pinned in `uv.lock`; the GitHub Actions workflow runs the offline checks after publication.

## Explicit rehearsal fallback

Set `AGENTFORGE_PROVIDER=rehearsal` and restart only when selecting that teaching route. Rehearsal executes the real tools through a scripted LangChain model; it cannot interpret arbitrary instructions. The provider label makes this distinction visible. Live Gemini is the default in this version. An optional tool-capable Ollama adapter remains available but has not been network-tested in this revision.

## Scope and references

Financial scenarios, candidate worksheets and campaign drafts are fictional decision-support exercises. Human review owns launch, hiring, purchasing and publication decisions. Memory is bounded keyword retrieval, not a vector database. This single Python process is not six isolated computers or VMs.

The HUD, command channel and Memory Vault were inspired by [vibe-jarvis](https://github.com/arthi-rajendran24/vibe-jarvis). The implementation uses [LangChain agents](https://docs.langchain.com/oss/python/langchain/agents), [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview), and [Gemini](https://ai.google.dev/gemini-api/docs). See [proposal coverage](docs/PROPOSAL-MAPPING.md) for the six domain outputs and workshop mapping.
