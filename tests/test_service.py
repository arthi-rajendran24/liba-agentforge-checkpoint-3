from agentforge.service import live_answer, rehearsal_answer

PAYLOAD = {"price": 120, "unit_cost": 65, "fixed_cost": 240000, "budget": 2400000}


def test_rehearsal_is_explicitly_unverified_live():
    result = rehearsal_answer("finance", PAYLOAD)
    assert result["mode"] == "rehearsal"
    assert "not been checked" in result["explanation"]


def test_live_boundary_is_tested_with_fake_not_network():
    calls = []

    def fake_explainer(contract: str, result: dict) -> str:
        calls.append((contract, result))
        return "Fake explanation for an offline test"

    response = live_answer("finance", PAYLOAD, fake_explainer)
    assert response["mode"] == "live"
    assert response["explanation"].startswith("Fake")
    assert calls[0][1]["break_even_units"] == 4364
