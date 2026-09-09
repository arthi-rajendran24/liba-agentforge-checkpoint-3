# Build AgentForge JARVIS with Arthi

Use this beside the LIBA rehearsal slides. Work in pairs: one driver types, one navigator checks. Use fictional data throughout. Today uses scripted rehearsal responses with real LangChain tools, calculations and saved outputs; no model key is required.

## 1. Get the tools

Check `git --version` and `uv --version`. Install only missing tools.

macOS Terminal:

```sh
# Git, if missing:
xcode-select --install
# uv, if missing:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows PowerShell:

```powershell
winget install --id Git.Git -e --source winget
winget install --id astral-sh.uv -e
```

Reopen the terminal after installation and check versions again. Use your institution's approved installation route. Have an editor available. Initial dependency installation needs internet or an already prepared package cache.

Official instructions: [uv](https://docs.astral.sh/uv/getting-started/installation/), [Git for macOS](https://git-scm.com/install/mac), [Git for Windows](https://git-scm.com/install/windows).

## 2. Clone Arthi's actual repository

Arthi supplies the tested HTTPS repository URL. Do not use the inspiration repository as a substitute for this project. The workshop repository has not been published by creating these files.

The following prompts let you paste the real URL without editing a placeholder command.

macOS Terminal:

```sh
printf 'Paste the HTTPS repository URL, then press Enter: '
read REPO_URL
git clone "$REPO_URL" agentforge-jarvis
cd agentforge-jarvis
ls
```

Windows PowerShell:

```powershell
$repoUrl = Read-Host "Paste the HTTPS repository URL"
git clone $repoUrl agentforge-jarvis
cd agentforge-jarvis
ls
```

You must see `pyproject.toml`, `uv.lock`, `src` and `workshop`. If the destination exists, use the intended existing clone or select a fresh destination; do not overwrite unrelated work. If using the source ZIP, extract it and enter its `agentforge-jarvis` folder instead.

## 3. Install and verify

From that project folder:

```sh
uv sync --frozen
uv run pytest -q
```

Expected at this revision: **19 passed**. `uv` prepares the matching Python environment in `.venv`. The first install may download Python and packages.

Select rehearsal explicitly in macOS Terminal:

```sh
export AGENTFORGE_PROVIDER=rehearsal
uv run agentforge-jarvis doctor
uv run agentforge-jarvis web
```

Or in Windows PowerShell:

```powershell
$env:AGENTFORGE_PROVIDER="rehearsal"
uv run agentforge-jarvis doctor
uv run agentforge-jarvis web
```

Doctor should report `provider: rehearsal` and `configured: true`. Open **http://127.0.0.1:8787** and leave the server terminal open. If the port is occupied, use `uv run agentforge-jarvis web --port 8788` and open the matching port.

**Checkpoint 1:** six specialists visible. Select Baseline launch, run the launch swarm, see six completed reports and CONDITIONAL GO. Review is still required.

## 4. Build your first small agent

Open `workshop/first_agent_starter.py` in your editor. In `estimate_launch_cash`, replace only the two `None` values:

```python
cash_needed = UNITS * UNIT_COST + OTHER_LAUNCH_COSTS
funding_gap = max(0, cash_needed - BUDGET)
```

Save. In a second terminal, still inside the project root, run:

```sh
uv run python workshop/first_agent_starter.py
```

Expect `cash_needed_inr: 2400000`, `funding_gap_inr: 0`, and `REVIEW WITH A HUMAN`. Now set `BUDGET = 1_800_000`, save and rerun. Predict the answer first: the gap is **600000** and recommendation **HOLD**. Restore the budget when finished.

`workshop/first_agent.py` is the completed reference; run it with `uv run python workshop/first_agent.py`. The adapter in `workshop/rehearsal_model.py` intentionally follows a fixed script and calls the cash tool through LangChain. Editing this tiny lab does not change the browser app.

**Checkpoint 2:** show the code and both calculated results. Explain `@tool` as a labelled capability and `create_agent` as the connector between model, prompt and tools.

## 5. Adapt your specialist

In the app, select Baseline, then Edit brief. Restore `examples/project-monsoon.json` between experiments. Change one field, Apply scenario, open the specialist blueprint, then Run specialist + dependencies.

| Agent | Change from defaults | Expected evidence |
|---|---|---|
| PRISM | `signals[0].positive` 92 → 60 | Overall positive rate 63.6% |
| PULSE | `marketing_budget` 180000 → 90000 | Channel budgets total ₹90,000 |
| NOVA | `required_fte` 10 → 12 | 4 FTE gap; ₹40,000 allowance |
| ATLAS | `production_per_day` 600 → 400 | 4,800 units short; 96 days needed |
| LEDGER | `price` 120 → 90 | 27.8% margin, below 38% target; HOLD |
| JARVIS | Defaults plus Budget −25% | Preserve the ₹6 lakh gap and HOLD |

Blueprint instructions are saved, but rehearsal responses stay scripted. Input edits and Python tool changes affect real calculations. The workflow executes sequentially: Analytics, Marketing, HR, Operations, Finance, General Management. Marketing/HR/Operations each receive Analytics, Finance consumes their reports, and General Management receives all five.

**Checkpoint 3:** show your original value, prediction, changed value, actual metric and one limitation.

## 6. Add memory and test a shock

In Memory Vault, save a note titled **Packaging review**:

```text
Fictional workshop note:
The packaging review is owned by Mira.
Allergen copy needs review before launch.
```

Ask Jarvis: **What do the memory notes say about the packaging review owner?** The rehearsal router uses memory/topic keywords; expect a Packaging review citation and the excerpt naming Mira.

Restore the default scenario. Run Baseline launch. Then choose Budget −25% and run again. In Run Archive select exactly these two completed runs. Expect budget ₹24 lakh → ₹18 lakh, unchanged cash need ₹24 lakh, gap ₹0 → ₹6 lakh, and CONDITIONAL GO → HOLD.

## 7. Review, export and explain

Read metrics, evidence, assumptions, risks and actions. Save a human rubric assessment in Workshop Lab if requested. Export both Markdown brief and JSON. Give a three-minute explanation: goal → single change → evidence → decision and limitation.

Keep the same local team ID and `.agentforge` data directory for your next session. Stop the app with Ctrl+C; stopping does not erase saved data. Team IDs are local workspace labels, not login accounts or cloud sharing. Keep personal notes, keys and database files out of GitHub.

## If stuck

| Symptom | First useful check |
|---|---|
| `uv` missing | Reopen terminal; check approved installation |
| No `pyproject.toml` | Enter the correct project folder |
| Downloads fail | Resolve network access or pair with a ready device |
| Starter says incomplete | Replace both `None` values and save |
| Browser cannot connect | Keep server running; match its port |
| Unexpected metrics | Restore default JSON and select Baseline |
| No memory match | Save note in same team; use memory and topic words |

A ZIP has the source, not every dependency. Once installed and cached, `uv sync --frozen --offline` and `uv run --offline agentforge-jarvis web` can use the prepared local environment. Windows installation commands are sourced from official documentation; Windows execution must be verified on the team's Windows devices.
