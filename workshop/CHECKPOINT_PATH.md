# AgentForge cumulative checkpoint path

The three standalone checkpoint repositories form a cumulative route into this complete repository. They share the same Python package name, domain identifiers, tool names, dependency lock and safety boundaries.

## Checkpoint 1

Students run and explain one deterministic tool from `agentforge_jarvis.checkpoint_tools`. The six available identifiers are `analytics`, `marketing`, `hr`, `operations`, `finance` and `general-management`. Their function names match the complete application catalog.

```sh
uv sync --frozen
uv run pytest -q
```

## Checkpoint 2

Checkpoint 2 retains Checkpoint 1 and adds `agentforge_jarvis.checkpoint_agent`. It constructs a real LangChain agent with `create_agent`, requires the named domain tool to execute and rejects a response without successful tool evidence. Its local browser interface uses FastAPI, matching the final application's server stack.

```sh
uv sync --frozen
uv run pytest -q
uv run python workshop/checkpoint_app.py
```

Open `http://127.0.0.1:8787`. Rehearsal mode uses a scripted chat model but still traverses LangChain's tool loop. Live mode requires a private `GEMINI_API_KEY` and uses the model named by `AGENTFORGE_MODEL`.

## Checkpoint 3

Checkpoint 3 is a complete snapshot of this repository, including the command center, all six agents, LangGraph workflow, persistence, reviewed evidence, workshop documents and deployment guidance.

```sh
uv sync --frozen
uv run pytest -q
uv run agentforge-jarvis doctor
uv run agentforge-jarvis web
```

Open `http://127.0.0.1:8787`. Use `AGENTFORGE_PROVIDER=rehearsal` for an offline classroom run. A deliberate live Gemini acceptance check remains separate because it consumes quota.

## Synchronization contract

The Checkpoint 3 repository must match the canonical AgentForge repository tree at its recorded upstream commit. Only `.git` metadata may differ. The release validation compares every tracked path and SHA-256 digest before publishing the three repositories or rebuilding the classroom ZIPs.
