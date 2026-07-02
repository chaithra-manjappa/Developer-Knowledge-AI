"""Prompt template service."""

from __future__ import annotations

from pathlib import Path


class PromptTemplateError(Exception):
    """Raised when a prompt template cannot be loaded."""


class PromptService:
    """
    Loads prompt templates and replaces placeholders.
    """

    def __init__(self, prompts_directory: Path) -> None:
        self._prompts_directory = prompts_directory

    def load(self, template_name: str, **variables: str) -> str:
        """
        Load a prompt template and replace placeholders.
        """

        template_path = self._prompts_directory / template_name

        if not template_path.exists():
            raise PromptTemplateError(
                f"Prompt template '{template_name}' was not found."
            )

        prompt = template_path.read_text(encoding="utf-8")

        for key, value in variables.items():
            prompt = prompt.replace(f"{{{{{key}}}}}", value)

        return prompt