"""Pollinations Image Client."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import quote

import requests


class PollinationsClientError(Exception):
    """Raised when Pollinations image generation fails."""


class PollinationsClient:
    """
    Client for generating images using Pollinations AI.
    """

    BASE_URL = "https://image.pollinations.ai/prompt/"

    def generate_image(
        self,
        prompt: str,
        output_path: Path,
    ) -> Path:

        try:

            url = self.BASE_URL + quote(prompt)

            response = requests.get(
                url,
                timeout=120,
            )

            response.raise_for_status()

            output_path.write_bytes(
                response.content,
            )

            return output_path

        except Exception as error:

            raise PollinationsClientError(
                "Failed to generate image."
            ) from error