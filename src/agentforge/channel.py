from __future__ import annotations

import json
from collections.abc import Callable, Iterator

Responder = Callable[..., dict]


def parse_text_request(text: str) -> tuple[str, dict]:
    try:
        request = json.loads(text)
        domain = request["domain"]
        payload = request["payload"]
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        raise ValueError('Send JSON with "domain" and "payload"') from exc
    if not isinstance(domain, str) or not isinstance(payload, dict):
        raise TypeError('"domain" must be text and "payload" must be an object')
    return domain, payload


def handle_text(text: str, responder: Responder, *, live: bool = False) -> dict:
    domain, payload = parse_text_request(text)
    return responder(domain, payload, live=live)


def word_stream(text: str) -> Iterator[str]:
    for word in text.split():
        yield f"{word} "
