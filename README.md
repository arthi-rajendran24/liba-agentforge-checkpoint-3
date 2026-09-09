# AgentForge composable checkpoint recovery

This repository is a recovery reference, not the student's submitted project. Its Git history contains three cumulative checkpoints. A student may clone a complete checkpoint, or open this repository beside their existing project in Google Antigravity and merge only the missing layers.

## Checkpoint 1: tested domain tool

The current branch contains deterministic tools for all six workshop specializations and offline tests. It makes no model or network call.

```sh
uv sync
uv run pytest -q
```

See `RECOVERY_MATRIX.md` before combining this reference with student work.
