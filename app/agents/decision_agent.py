"""Decision Agent."""

from __future__ import annotations

from app.clients.groq_client import GroqClient
from app.models.decision import Decision
from app.parsers.json_parser import JsonParser
from app.services.prompt_service import PromptService


class DecisionAgent:
    """
    Analyses the user's request and decides what
    actions should happen before generating a post.
    """

    def __init__(
        self,
        groq_client: GroqClient,
        prompt_service: PromptService,
    ) -> None:

        self._groq_client = groq_client
        self._prompt_service = prompt_service

    def analyse(self, user_request: str) -> Decision:

        prompt = self._prompt_service.load(
            "decision_prompt.txt",
            user_request=user_request,
        )

        response = self._groq_client.generate(prompt)

        data = JsonParser.parse(response)

        return Decision(
            needs_web_search=data["needs_web_search"],
            needs_image=data["needs_image"],
            needs_review=data["needs_review"],
            topic=data["topic"],
            reason=data["reason"],
        )