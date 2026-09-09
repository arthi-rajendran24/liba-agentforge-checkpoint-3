# LIBA AgentForge Checkpoint 3

Clone this repository for the complete Day 1 reference, or open it beside a student's existing project in Google Antigravity. It contains all earlier layers plus reviewed image evidence, approved memory, local streaming and optional Telegram.

## Checkpoint 3: end-to-end reviewed agent

This branch inherits Checkpoints 1 and 2. It adds image validation and extraction, explicit human approval before memory, local response streaming, and an optional Telegram channel. The interface and Telegram both reuse the Checkpoint 2 service.

```sh
git clone https://github.com/arthi-rajendran24/liba-agentforge-checkpoint-3.git
cd liba-agentforge-checkpoint-3
uv sync
uv run pytest -q
uv run streamlit run app.py
```

Use `patches/checkpoint-1-to-3.patch` when the student has Checkpoint 1. Use `patches/checkpoint-2-to-3.patch` when Checkpoint 2 already passes. Preserve earlier student work and merge only missing layers.

Earlier checkpoints:

- https://github.com/arthi-rajendran24/liba-agentforge-checkpoint-1
- https://github.com/arthi-rajendran24/liba-agentforge-checkpoint-2
