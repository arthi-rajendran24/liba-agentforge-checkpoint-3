"""Explicit live acceptance run with fictional data; saves only sanitized results."""

import json
import threading
import time
from pathlib import Path
from tempfile import TemporaryDirectory

from dotenv import load_dotenv

from agentforge_jarvis.engine import Engine, validate_package
from agentforge_jarvis.models import ChatRequest, RunRequest
from agentforge_jarvis.providers import Settings, public_error
from agentforge_jarvis.storage import Store

load_dotenv(Path.cwd() / ".env", override=False)
settings = Settings.from_env()
if settings.provider == "rehearsal":
    raise SystemExit("Configure a live provider before this explicit acceptance test.")
output = Path("examples/live-verification.json")
results = {"provider": settings.provider, "model": settings.model, "runs": []}
with TemporaryDirectory() as tmp:
    engine = Engine(Store(Path(tmp)), settings)
    try:
        for challenge in ("baseline", "budget-cut"):
            start = time.monotonic()
            print("Starting live", challenge, flush=True)

            def emit(kind, **event):
                if kind in ("agent_started", "agent_completed"):
                    print(kind, event.get("domain"), flush=True)

            reports = engine.graph(RunRequest(challenge=challenge), emit, threading.Event())
            checks = validate_package(reports)
            assert all(c["passed"] for c in checks)
            assert reports["finance"].metrics["funding_gap_inr"] == (
                0 if challenge == "baseline" else 600000
            )
            assert reports["general-management"].metrics["decision"] == (
                "CONDITIONAL GO" if challenge == "baseline" else "HOLD"
            )
            results["runs"].append(
                {
                    "challenge": challenge,
                    "seconds": round(time.monotonic() - start, 2),
                    "checks": checks,
                    "reports": {k: v.model_dump() for k, v in reports.items()},
                }
            )
            output.write_text(json.dumps(results, indent=2))
            print("PASS", challenge, flush=True)
        engine.store.add_note(
            "live-check",
            "Packaging review",
            "The fictional packaging review owner is Mira. Allergen copy must be checked before launch.",
        )
        chat = engine.chat(
            ChatRequest(
                team="live-check", message="Who owns the packaging review? Cite the team note."
            )
        )
        assert "Mira" in chat["answer"]
        assert any(e.get("tool") == "search_memory" for e in chat["events"])
        results["memory_chat"] = chat
        engine.store.set_blueprint(
            "live-check",
            "analytics",
            "Begin the final answer with the exact heading: PRISM WORKSHOP BRIEF. Explain the findings in three short bullet points.",
        )
        chat = engine.chat(
            ChatRequest(
                team="live-check",
                domain="analytics",
                message="Analyze this launch using all required tools. Follow the saved output-format preference.",
            )
        )
        assert "PRISM WORKSHOP BRIEF" in chat["answer"]
        results["blueprint_chat"] = chat
        results["verified_at"] = engine.live_verified_at
        output.write_text(json.dumps(results, indent=2))
        print("PASS live memory citation and blueprint instruction", flush=True)
    except Exception as error:
        results["failure"] = public_error(error)
        output.write_text(json.dumps(results, indent=2))
        print(results["failure"], flush=True)
        raise SystemExit(1) from None
    finally:
        engine.close()
