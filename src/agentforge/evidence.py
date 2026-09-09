from __future__ import annotations

import os
from collections.abc import Callable

ALLOWED_TYPES = {"image/png", "image/jpeg"}
MAX_BYTES = 2 * 1024 * 1024
Extractor = Callable[[bytes, str], str]


def validate_image(content_type: str, size: int) -> None:
    if content_type not in ALLOWED_TYPES:
        raise ValueError("Only PNG and JPEG are allowed")
    if size <= 0 or size > MAX_BYTES:
        raise ValueError("Image must be between 1 byte and 2 MB")


def _gemini_extract(data: bytes, content_type: str) -> str:
    key = os.getenv("GEMINI_API_KEY", "")
    if not key:
        raise RuntimeError("GEMINI_API_KEY is not configured")
    model = os.getenv("AGENTFORGE_MODEL", "gemini-3.1-flash-lite")
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model=model,
        contents=[
            "Transcribe only facts visibly present in this fictional workshop image. Mark unclear text as [uncertain]. Do not infer missing values.",
            types.Part.from_bytes(data=data, mime_type=content_type),
        ],
    )
    return response.text or ""


def extract_image(data: bytes, content_type: str, *, extractor: Extractor | None = None) -> str:
    validate_image(content_type, len(data))
    text = (extractor or _gemini_extract)(data, content_type).strip()
    if not text:
        raise ValueError("No visible text was extracted")
    return text


def reviewed_evidence(
    filename: str, extracted: str, corrected: str, uncertainty: str, approved: bool
) -> dict:
    if not approved:
        raise PermissionError("Review and approval are required")
    text = corrected.strip() or extracted.strip()
    if not text:
        raise ValueError("Approved evidence cannot be empty")
    return {
        "source": filename,
        "text": text,
        "uncertainty": uncertainty.strip(),
        "approved": True,
    }
