"""Save Image Tool."""

from __future__ import annotations

from pathlib import Path


class SaveImageTool:
    """
    Responsible for creating the image output folder
    and generating a valid image file path.
    """

    def __init__(
        self,
        output_directory: Path = Path("generated_images"),
    ) -> None:

        self._output_directory = output_directory

        self._output_directory.mkdir(
            exist_ok=True,
        )

    def create_file_path(
        self,
        topic: str,
    ) -> Path:
        """
        Create a file path for the generated image.
        """

        filename = (
            topic.lower()
            .replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
        )

        return self._output_directory / f"{filename}.png"