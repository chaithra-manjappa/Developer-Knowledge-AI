"""LinkedIn Writer Agent."""

from __future__ import annotations

from app.clients.groq_client import GroqClient
from app.services.prompt_service import PromptService


class ContentGenerationError(Exception):
    """Raised when content generation fails."""


class LinkedInWriterAgent:
    """
    Generates LinkedIn posts using an LLM.
    """

    def __init__(
        self,
        client: GroqClient,
        prompt_service: PromptService,
    ) -> None:
        self._client = client
        self._prompt_service = prompt_service

    def generate(self, topic: str) -> str:
        """
        Generate a LinkedIn post.

        Args:
            topic: Topic to write about.

        Returns:
            Generated LinkedIn post.
        """

        prompt = self._prompt_service.load(
            "linkedin_post.md",
            topic=topic,
        )

        try:
            return self._client.generate(prompt)

        except Exception as error:
            raise ContentGenerationError(
                "Failed to generate LinkedIn post."
            ) from error