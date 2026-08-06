"""Application configuration."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """
    Stores all application configuration in one place.
    """

    llm_provider: str
    llm_api_key: str
    llm_model: str

    tavily_api_key: str

    log_level: str
    gemini_api_key: str
    gemini_model: str

    @classmethod
    def from_environment(cls) -> "Settings":
        """
        Creates a Settings object by reading environment variables.
        """

        return cls(
            llm_provider=os.getenv("LLM_PROVIDER", "groq"),
            llm_api_key=os.getenv("GROQ_API_KEY", ""),
            llm_model=os.getenv("LLM_MODEL", "llama-3.3-70b-versatile"),

            tavily_api_key=os.getenv("TAVILY_API_KEY", ""),

            log_level=os.getenv("LOG_LEVEL", "INFO"),
            gemini_api_key=os.getenv("GEMINI_API_KEY", ""),
            gemini_model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash-image"),
        )