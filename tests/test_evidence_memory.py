import pytest

from agentforge.evidence import extract_image, reviewed_evidence, validate_image
from agentforge.memory import save_approved


def test_image_validation_and_fake_extraction_are_offline():
    validate_image("image/png", 3)
    text = extract_image(b"png", "image/png", extractor=lambda _data, _type: "Visible: 42")
    assert text == "Visible: 42"
    with pytest.raises(ValueError):
        validate_image("application/pdf", 3)


def test_review_required_before_evidence_or_memory(tmp_path):
    with pytest.raises(PermissionError):
        reviewed_evidence("source.png", "Visible", "", "", False)
    with pytest.raises(PermissionError):
        save_approved(tmp_path / "memory.json", "Visible", "source.png", "", False)


def test_corrected_approved_evidence_is_saved(tmp_path):
    evidence = reviewed_evidence("source.png", "Vsible 42", "Visible 42", "none", True)
    record = save_approved(
        tmp_path / "memory.json",
        evidence["text"],
        evidence["source"],
        evidence["uncertainty"],
        evidence["approved"],
    )
    assert record["summary"] == "Visible 42"


def test_probable_credential_is_rejected(tmp_path):
    with pytest.raises(ValueError):
        save_approved(tmp_path / "memory.json", "GEMINI_API_KEY=secret", "chat", "", True)
