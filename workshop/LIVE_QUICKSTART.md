# Build AgentForge JARVIS with LIBA

Working independently? Use the [full self-guided handbook](SELF_GUIDED_WORKSHOP.md) for step-by-step explanations, expected results and recovery paths. An [editable Word edition](LIBA_AgentForge_Self_Guided_Handbook.docx) is included.

Use this guide with the **Main Workshop** deck. The primary route uses real Gemini through LangChain. The older QUICKSTART and Dry Run deck are an explicitly selected rehearsal fallback.

## 1. Prepare your laptop

You need Git, uv, an editor, a browser and internet access. Each pair needs approved Gemini API access for its local project. A hosted team access code only signs you into the shared app; it does not configure the Python coding lab.

Check in Terminal (macOS) or PowerShell (Windows):

```sh
git --version
uv --version
```

If missing on macOS, install Git with `xcode-select --install`. Install uv using the approved instructions at https://docs.astral.sh/uv/getting-started/installation/ . The documented installer is:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows, if winget is available:

```powershell
winget install --id Git.Git -e --source winget
winget install --id astral-sh.uv -e
```

Reopen your terminal, then check versions again. Managed laptops may require your institution's installation process. Pair with a ready laptop while resolving this.

## 2. Clone the actual workshop repository

Use the AgentForge workshop repository below. The vibe-jarvis inspiration repository is a different app.

```sh
git clone https://github.com/arthi-rajendran24/agentforge.git agentforge-jarvis
cd agentforge-jarvis
ls
uv sync --frozen
uv run pytest -q
```

The folder must contain **pyproject.toml** and **uv.lock**. If you downloaded a ZIP, open its inner project folder first. The first dependency install needs internet; uv selects Python 3.12. Tests run without making paid model calls.

## 3. Configure your live model

On macOS/Linux:

```sh
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Open `.env` privately in the editor. Keep these settings and replace only the blank key with your own approved Gemini API key:

```dotenv
AGENTFORGE_PROVIDER=gemini
AGENTFORGE_MODEL=gemini-3.1-flash-lite
GEMINI_API_KEY=your-own-key
AGENTFORGE_GEMINI_RPM=12
```

The tested model was available on 3 September 2026. Your project must have access and sufficient quota. Get or inspect approved access in [Google AI Studio](https://aistudio.google.com/api-keys). `.env` is ignored by Git and excluded from the provided package. The facilitator key is not distributed with student clones.

Existing shell environment variables override `.env`. If you used the rehearsal fallback earlier, clear that shell override: `unset AGENTFORGE_PROVIDER` on macOS; `Remove-Item Env:AGENTFORGE_PROVIDER -ErrorAction SilentlyContinue` in PowerShell. Restart the app after configuration changes.

## 4. Prove the connection, then open the app

```sh
uv run agentforge-jarvis doctor
uv run python workshop/first_agent_live.py
uv run agentforge-jarvis web
```

`doctor` checks configuration. The second command makes an actual Gemini request. Look for **EXECUTED TOOL** with cash needed **2400000**, funding gap **0**, then the Gemini explanation. The third command keeps running: open http://127.0.0.1:8787 and leave its terminal open. Use a second terminal for code exercises.

In the browser select your assigned team ID, then **Run launch swarm**. Expect six completed agents, Gemini marked **LIVE VERIFIED**, and **CONDITIONAL GO** for the default scenario. Request pacing can make a full run take a few minutes. Follow the activity stream and wait; do not repeatedly click or launch overlapping command-line tests.

The default request pacer allows 12 model requests per minute in one process. Multiple tools can be requested in one model call. Other processes, laptops, or applications sharing the same Google project also consume that project's quota. Token and daily limits still apply. Follow Arthi's staggered start instructions.

## 5. Complete the coding lab

Open `workshop/first_agent_starter_live.py`. Replace the two `None` values:

```python
cash_needed = UNITS * UNIT_COST + OTHER_LAUNCH_COSTS
funding_gap = max(0, cash_needed - BUDGET)
```

Save and run:

```sh
uv run python workshop/first_agent_starter_live.py
```

Predict the answer before you look. Next set `BUDGET = 1_800_000`, save and run again. Expect cash needed **2400000**, gap **600000**, and **HOLD**. The wording may vary; the executed tool result should not. Restore the budget or save a named experiment. The completed reference is `workshop/first_agent_live.py`.

## 6. Adapt a specialist

Open its blueprint, read its goal/tool/inputs, then save a useful instruction such as: “Begin with three short business findings. Name the largest uncertainty.” Run the specialist and inspect both calculated facts and generated analysis.

For a scenario experiment, select Baseline, open **Edit brief**, change one field, apply, and run. Restore `examples/project-monsoon.json` between independent experiments. Record your prediction and result in `TEAM_WORKBOOK.md`.

## 7. Add image and memory evidence

Open **Memory Vault → Extract image** and select `workshop/assets/monsoon-case.png` (a fictional slide image). Gemini extracts text into the editor. Check ₹24 lakh, 30,000 units, 84 days, ₹120 price and ₹65 unit cost. Correct any error, name the source, then explicitly save. Images must be PNG/JPEG under 2 MB. Raw images are sent to Gemini but are not automatically saved as notes.

Save another note titled **Packaging review**: “Fictional workshop note: The packaging review is owned by Mira. Allergen copy needs review before launch.” Ask Jarvis: “Who owns packaging review? Cite the team note.” Expect Mira and a source citation. Retrieval uses keyword overlap; include the topic words in the question.

Voice input is optional: click the microphone, inspect the transcript and send deliberately. If unsupported, use typed text or the provided transcript activity.

## 8. Connect, challenge and export

Run the baseline, then **Budget −25%**. Expect the final decision to change to **HOLD**, preserving the **₹6 lakh gap**. Compare saved runs in **Run archive**. In **Workshop lab**, inspect checks, enter your human rubric scores and reflection. Export Markdown and JSON and keep them with your workbook.

## 9. Save Day 1 for Day 2

Keep the same project, team ID and local data directory. Save source code separately from your private database. Back up with a new filename:

```sh
uv run agentforge-jarvis backup .agentforge/day1-backup.sqlite3
```

The backup contains team records; keep it private. Do not overwrite it. Day 2 begins by reopening the saved specialist output and source notes.

## If something fails

| Symptom | Action |
|---|---|
| No pyproject.toml | Enter the project folder, then rerun |
| Package/download failure | Check network/proxy and repeat `uv sync --frozen` |
| Missing or rejected key | Check local `.env` and restart; show only the sanitized error |
| Quota / 429 | Pause new calls; check the actual project/model quota in AI Studio |
| Model unavailable | Use an approved model ID available to your project |
| App busy / 429 | Let the active request finish; retry deliberately |
| Port in use | Stop the earlier server or use `web --port 8788` |
| Tool step incomplete | Finish both calculations; inspect the executed tool output |
| Sign-in required | Use the assigned team ID/access code, not an API key |

The application never silently replaces a failed live response with rehearsal. Only switch to the old rehearsal route when Arthi explicitly announces it, and label the resulting evidence accordingly.
