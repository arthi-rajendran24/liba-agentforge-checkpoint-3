"""A tiny scripted model for the first-agent lab. No AI service is contacted."""

from uuid import uuid4

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.outputs import ChatGeneration, ChatResult


class WorkshopModel(BaseChatModel):
    @property
    def _llm_type(self):
        return "workshop-scripted-model"

    def bind_tools(self, tools, **kwargs):
        return self

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        if isinstance(messages[-1], ToolMessage):
            answer = AIMessage(content="REHEARSAL TOOL RESULT\n" + str(messages[-1].content))
        else:
            answer = AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": "estimate_launch_cash",
                        "args": {},
                        "id": uuid4().hex,
                        "type": "tool_call",
                    }
                ],
            )
        return ChatResult(generations=[ChatGeneration(message=answer)])
