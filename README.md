# AgentForge composable checkpoint recovery

This repository is a recovery reference, not the student's submitted project. Its Git history contains three cumulative checkpoints. A student may clone a complete checkpoint, or open this repository beside their existing project in Google Antigravity and merge only the missing layers.

## Checkpoint 2: live-capable domain agent

This branch inherits Checkpoint 1 and adds a single compatibility seam, shared service and local Streamlit interface. Rehearsal mode makes no model or network call. Live mode makes one Gemini request only after the deterministic tool succeeds.

```sh
uv sync
uv run pytest -q
uv run streamlit run app.py
```

When merging with a student's Checkpoint 1, preserve their `tools.py` and tests. Adapt only `src/agentforge/student_adapter.py` to call their function.
