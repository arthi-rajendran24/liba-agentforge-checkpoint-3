"""Run the packaged Checkpoint 2 browser interface from the workshop folder."""

from agentforge_jarvis.checkpoint_app import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8787)
