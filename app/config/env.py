"""Environment variable loader."""

from __future__ import annotations

import os
from pathlib import Path


class EnvLoader:
    """
    Loads environment variables from a .env file into os.environ.
    """

    def __init__(self, env_file: Path) -> None:
        self._env_file = env_file

    def load(self) -> None:
        """
        Read the .env file and populate os.environ.
        """
        if not self._env_file.exists():
            return

        for line in self._env_file.read_text().splitlines():
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())