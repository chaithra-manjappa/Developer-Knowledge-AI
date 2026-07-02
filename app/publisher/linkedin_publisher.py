"""LinkedIn Publisher."""

from __future__ import annotations


class LinkedInPublisher:
    """
    Responsible for publishing content to LinkedIn.
    """

    def publish(self, content: str) -> None:
        """
        Publish a LinkedIn post.

        Args:
            content: The LinkedIn post.
        """

        print("\nPublishing to LinkedIn...\n")
        print(content)