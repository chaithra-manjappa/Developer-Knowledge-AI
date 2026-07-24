"""Generated Image Model."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class GeneratedImage:
    """
    Represents an AI generated image.
    """

    prompt: str

    file_path: Path