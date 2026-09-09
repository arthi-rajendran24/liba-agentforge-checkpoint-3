# AgentForge composable checkpoint recovery

This repository is a recovery reference, not the student's submitted project. Its Git history contains three cumulative checkpoints. A student may clone a complete checkpoint, or open this repository beside their existing project in Google Antigravity and merge only the missing layers.

## Checkpoint 3: end-to-end reviewed agent

This branch inherits Checkpoints 1 and 2. It adds image validation and extraction, explicit human approval before memory, local response streaming, and an optional Telegram channel. The interface and Telegram both reuse the Checkpoint 2 service.

```sh
uv sync
uv run pytest -q
uv run streamlit run app.py
```

Live Gemini and Telegram paths are optional. Every checkpoint remains demonstrable in rehearsal mode. When merging, preserve any passing earlier student layer and apply only the missing Git delta shown in `RECOVERY_MATRIX.md`.
