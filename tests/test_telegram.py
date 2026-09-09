from agentforge_jarvis.telegram import text_response


class FakeEngine:
    def chat(self, request):
        return {"answer": f"reviewed: {request.message}"}


def test_telegram_text_reuses_the_complete_chat_service():
    assert text_response(FakeEngine(), "team-a", "Check the budget") == "reviewed: Check the budget"
