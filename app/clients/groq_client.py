"""Groq API client."""

from __future__ import annotations

from groq import Groq
from groq import APIError


class GroqClientError(Exception):
    """Raised when the Groq client fails."""


class GroqClient:
    """
    Wrapper around the Groq SDK.

    Responsible only for communicating with the Groq API.
    """

    def __init__(self, api_key: str, model: str) -> None:
        """
        Initialize the Groq client.

        Args:
            api_key: Groq API key.
            model: LLM model name.
        """
        self._model = model
        self._client = Groq(api_key=api_key)

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to Groq and return the generated response.

        Args:
            prompt: Prompt to send to the LLM.

        Returns:
            Generated response text.

        Raises:
            GroqClientError: If the API request fails.
        """
        try:
            response = self._client.chat.completions.create(
                model=self._model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                temperature=0.7,
            )

            return response.choices[0].message.content.strip()

        except APIError as error:
            raise GroqClientError(
                "Failed to generate response from Groq."
            ) from error