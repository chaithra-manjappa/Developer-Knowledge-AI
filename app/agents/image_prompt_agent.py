"""Image Prompt Agent."""

from __future__ import annotations

from app.clients.groq_client import GroqClient
from app.models.search_result import SearchResult
from app.services.prompt_service import PromptService


class ImagePromptGenerationError(Exception):
    """Raised when image prompt generation fails."""


class ImagePromptAgent:
    """
    Responsible ONLY for creating an image prompt.

    Does NOT generate images.
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
        search_results: list[SearchResult],
    ) -> str:

        context = self._build_context(
            search_results,
        )

        prompt = self._prompt_service.load(
            "image_prompt.md",
            topic=topic,
            context=context,
        )

        try:

            print("\n🎨 Creating Image Prompt...")

            image_prompt = self._client.generate(
                prompt,
            )

            print("✅ Image Prompt Ready\n")

            return image_prompt.strip()

        except Exception as error:

            raise ImagePromptGenerationError(
                "Failed to generate image prompt."
            ) from error

    def _build_context(
        self,
        search_results: list[SearchResult],
    ) -> str:

        if not search_results:
            return ""

        context = []

        for index, result in enumerate(
            search_results,
            start=1,
        ):

            context.append(
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

        return "\n".join(context)