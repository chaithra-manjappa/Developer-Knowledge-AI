"""JSON response parser."""

from __future__ import annotations

import json


class JsonParserError(Exception):
    """Raised when JSON parsing fails."""


class JsonParser:
    """
    Converts LLM JSON responses into Python dictionaries.
    """

    @staticmethod
    def parse(response: str) -> dict:
        """
        Parse JSON returned by the LLM.

        Supports responses like:

        {
            ...
        }

        OR

        ```json
        {
            ...
        }
        ```
        """

        cleaned = response.strip()

        # Remove markdown opening fence
        if cleaned.startswith("```json"):
            cleaned = cleaned.removeprefix("```json").strip()

        elif cleaned.startswith("```"):
            cleaned = cleaned.removeprefix("```").strip()

        # Remove markdown closing fence
        if cleaned.endswith("```"):
            cleaned = cleaned.removesuffix("```").strip()

        try:
            return json.loads(cleaned)

        except json.JSONDecodeError as error:
            raise JsonParserError(
                f"Invalid JSON returned by the LLM.\n\n{response}"
            ) from error