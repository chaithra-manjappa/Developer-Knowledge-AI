"""Factory for creating LLM clients."""

from __future__ import annotations

from app.clients.groq_client import GroqClient
from app.config.settings import Settings


class LLMClientFactoryError(Exception):
    """Raised when an unsupported LLM provider is configured."""


class LLMClientFactory:
    """
    Creates the appropriate LLM client based on application settings.
    """

    def create(self, settings: Settings):
        """
        Create an LLM client.

        Args:
            settings: Application configuration.

        Returns:
            An initialized LLM client.

        Raises:
            LLMClientFactoryError
        """

        if settings.llm_provider == "groq":
            return GroqClient(
                api_key=settings.llm_api_key,
                model=settings.llm_model,
            )

        raise LLMClientFactoryError(
            f"Unsupported LLM provider: {settings.llm_provider}"
        )