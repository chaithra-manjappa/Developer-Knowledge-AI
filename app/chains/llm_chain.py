"""Reusable LLM Chain."""

from __future__ import annotations

from app.clients.groq_client import GroqClient
from app.parsers.json_parser import JsonParser
from app.services.prompt_service import PromptService


class LLMChain:
    """
    Executes a prompt through the LLM
    and parses the response.

    Similar to LangChain's LLMChain.
    """

    def __init__(
        self,
        client: GroqClient,
        prompt_service: PromptService,
    ) -> None:

        self._client = client
        self._prompt_service = prompt_service

    def run(
        self,
        template: str,
        **variables,
    ) -> dict:

        prompt = self._prompt_service.load(
            template,
            **variables,
        )

        response = self._client.generate(prompt)

        return JsonParser.parse(response)