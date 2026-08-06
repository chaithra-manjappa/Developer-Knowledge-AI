from __future__ import annotations

from app.clients.groq_client import GroqClient
from app.services.prompt_service import PromptService


class HashtagAgent:

    def __init__(
        self,
        client: GroqClient,
        prompt_service: PromptService,
    ):

        self._client = client
        self._prompt_service = prompt_service

    def generate(
        self,
        topic: str,
        content: str,
    ) -> str:

        prompt = self._prompt_service.load(
            "hashtag_prompt.md",
            topic=topic,
            content=content,
        )

        print("\n🏷️ Generating hashtags...\n")

        return self._client.generate(
            prompt,
        ).strip()