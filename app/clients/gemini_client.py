"""Gemini Image Client."""

from __future__ import annotations

import base64
from pathlib import Path

from google import genai
from google.genai import types


class GeminiClientError(Exception):
    """Raised when Gemini fails."""


class GeminiClient:

    def __init__(
        self,
        api_key: str,
        model: str,
    ) -> None:

        self._model = model

        self._client = genai.Client(
            api_key=api_key,
        )

    def generate_image(
        self,
        prompt: str,
        output_path: Path,
    ) -> Path:
        """
        Generate an image using Gemini.
        """

        try:

            response = self._client.models.generate_content(
                model=self._model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["TEXT", "IMAGE"],
                ),
            )

            for part in response.candidates[0].content.parts:

                if part.inline_data:

                    image_bytes = base64.b64decode(
                        part.inline_data.data
                    )

                    output_path.write_bytes(
                        image_bytes
                    )

                    return output_path

            raise GeminiClientError(
                "No image returned."
            )

        except Exception as error:

            raise GeminiClientError(
                "Failed to generate image."
            ) from error