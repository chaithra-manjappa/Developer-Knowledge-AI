"""LinkedIn Writer Agent."""

from __future__ import annotations

from app.clients.groq_client import GroqClient
from app.models.search_result import SearchResult
from app.services.prompt_service import PromptService


class ContentGenerationError(Exception):
    """Raised when content generation fails."""


class LinkedInWriterAgent:
    """
    Generates LinkedIn posts using the LLM.
    """

    def __init__(
        self,
        client: GroqClient,
        prompt_service: PromptService,
    ) -> None:

        self._client = client
        self._prompt_service = prompt_service

    def generate(
        self,
        topic: str,
        search_results: list[SearchResult] | None = None,
    ) -> str:
        """
        Generate a LinkedIn post.

        Args:
            topic: User topic.
            search_results: Optional search results from SearchAgent.

        Returns:
            Generated LinkedIn post.
        """

        context = self._build_context(search_results)

        prompt = self._prompt_service.load(
            "linkedin_post.md",
            topic=topic,
            context=context,
        )

        try:
            return self._client.generate(prompt)

        except Exception as error:
            raise ContentGenerationError(
                "Failed to generate LinkedIn post."
            ) from error

    def _build_context(
        self,
        search_results: list[SearchResult] | None,
    ) -> str:
        """
        Convert search results into prompt context.
        """

        if not search_results:
            return ""

        context_parts = []

        for index, result in enumerate(search_results, start=1):

            context_parts.append(
                f"""
Article {index}

Title:
{result.title}

Summary:
{result.content}

Source:
{result.url}
"""
            )

        return "\n".join(context_parts)