"""Decision Agent."""

from __future__ import annotations

from app.clients.groq_client import GroqClient
from app.models.decision import Decision
from app.parsers.json_parser import JsonParser
from app.services.prompt_service import PromptService


class DecisionAgent:
    """
    Analyses the user's request and decides how the
    content generation pipeline should execute.

    It does NOT generate content.
    It only decides what capabilities are required.
    """

    def __init__(
        self,
        groq_client: GroqClient,
        prompt_service: PromptService,
    ) -> None:

        self._groq_client = groq_client
        self._prompt_service = prompt_service

    def analyse(
        self,
        user_request: str,
    ) -> Decision:

        prompt = self._prompt_service.load(
            "decision_prompt.txt",
            user_request=user_request,
        )

        response = self._groq_client.generate(
            prompt,
        )

        data = JsonParser.parse(
            response,
        )

        return Decision(

            topic=data["topic"],

            content_type=data["content_type"],

            needs_web_search=data["needs_web_search"],

            needs_examples=data["needs_examples"],

            needs_source_links=data["needs_source_links"],

            difficulty=data["difficulty"],

            target_audience=data["target_audience"],

            reason=data["reason"],
        )