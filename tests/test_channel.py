import pytest

from agentforge.channel import handle_text, parse_text_request, word_stream


def test_channel_reuses_injected_service():
    calls = []

    def fake_answer(domain: str, payload: dict, *, live: bool) -> dict:
        calls.append((domain, payload, live))
        return {"mode": "fake", "explanation": "two words"}

    result = handle_text('{"domain":"finance","payload":{"price":120}}', fake_answer, live=True)
    assert result["mode"] == "fake"
    assert calls == [("finance", {"price": 120}, True)]
    assert list(word_stream(result["explanation"])) == ["two ", "words "]


def test_bad_channel_request_is_rejected():
    with pytest.raises(ValueError):
        parse_text_request("not json")
