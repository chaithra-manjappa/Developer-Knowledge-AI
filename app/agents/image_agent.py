"""Image Agent."""

from __future__ import annotations

from app.clients.pollinations_client import PollinationsClient
from app.models.generated_image import GeneratedImage
from app.tools.save_image_tool import SaveImageTool


class ImageGenerationError(Exception):
    """Raised when image generation fails."""


class ImageAgent:
    """
    Responsible ONLY for generating an image.

    It does NOT decide what image to create.
    It simply executes the prompt.
    """

    def __init__(
        self,
        image_client: PollinationsClient,
        save_image_tool: SaveImageTool,
    ) -> None:

        self._image_client = image_client
        self._save_image_tool = save_image_tool

    def generate(
        self,
        topic: str,
        image_prompt: str,
    ) -> GeneratedImage:

        try:

            output_path = self._save_image_tool.create_file_path(
                topic,
            )

            print("🖼 Generating Image...")

            self._image_client.generate_image(
                prompt=image_prompt,
                output_path=output_path,
            )

            print("✅ Image Generated.\n")

            return GeneratedImage(
                prompt=image_prompt,
                file_path=output_path,
            )

        except Exception as error:

            raise ImageGenerationError(
                "Failed to generate image."
            ) from error