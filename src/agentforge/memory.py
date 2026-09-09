from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

BLOCKED = ("GEMINI_API_KEY", "TELEGRAM_BOT_TOKEN", "AIza")


def save_approved(path: Path, summary: str, source: str, uncertainty: str, approved: bool) -> dict:
    if not approved:
        raise PermissionError("Human approval is required")
    if any(token in summary for token in BLOCKED):
        raise ValueError("Possible credential in memory")
    if not summary.strip() or not source.strip():
        raise ValueError("Summary and source are required")
    record = {
        "summary": summary.strip(),
        "source": source.strip(),
        "uncertainty": uncertainty.strip(),
        "approved": True,
        "saved_at": datetime.now(UTC).isoformat(),
    }
    existing = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    existing.append(record)
    path.write_text(json.dumps(existing, indent=2), encoding="utf-8")
    return record
