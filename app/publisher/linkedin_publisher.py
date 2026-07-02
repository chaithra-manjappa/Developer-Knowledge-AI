"""LinkedIn Publisher."""

from __future__ import annotations

from pathlib import Path

from playwright.sync_api import Page
from playwright.sync_api import TimeoutError

from app.browser.browser_manager import BrowserManager


class LinkedInPublisher:
    """
    Responsible for publishing posts to LinkedIn.
    """

    def __init__(self) -> None:
        self._browser = BrowserManager(
            storage_state=Path("sessions/linkedin.json"),
        )

    def publish(self, content: str) -> None:
        """
        Publish a LinkedIn post.

        Args:
            content: LinkedIn post content.
        """

        self._browser.start()

        try:
            page = self._browser.new_page()

            self._open_feed(page)

            self._open_post_dialog(page)

            self._enter_content(
                page=page,
                content=content,
            )

            #self._publish_post(page)

            print("\n✅ LinkedIn post has been prepared.")
            print("👉 Please review it in the browser and click 'Post' manually.")

            input("\nPress Enter after you're done posting...")

        finally:
            self._browser.stop()

    def _open_feed(
        self,
        page: Page,
    ) -> None:
        """
        Open LinkedIn feed.
        """

        print("➡️ Opening LinkedIn feed...")

        page.goto(
            "https://www.linkedin.com/feed/",
            wait_until="domcontentloaded",
        )

        print("✅ Feed page opened.")

        page.wait_for_timeout(5000)

        print("📄 Current URL:", page.url)

    def _open_post_dialog(
        self,
        page: Page,
    ) -> None:
        """
        Opens the LinkedIn post creation dialog.
        """

        print("➡️ Looking for 'Start a post' button...")

        start_post = page.get_by_role(
            "link",
            name="Start a post",
        )

        start_post.wait_for(
        state="visible",
        timeout=15000,
        )

        start_post.click()

        print("✅ Post dialog opened.")

    def _enter_content(
        self,
        page: Page,
        content: str,
    ) -> None:
        """
        Enter LinkedIn post content.
        """

        editor = page.locator(
            "div[role='textbox']"
        )

        editor.wait_for(
            state="visible",
            timeout=10000,
        )

        editor.click()

        editor.fill(content)

    def _publish_post(
        self,
        page: Page,
    ) -> None:
        """
        Click the Post button.
        """

        try:
            input(
                "\nReview the post and press Enter to publish..."
            )

            post_button = page.get_by_role(
                "button",
                name="Post",
            )

            post_button.wait_for(
                state="visible",
                timeout=10000,
            )

            post_button.click()

            print("✅ Post published.")

        except TimeoutError as error:
            raise RuntimeError(
                "Unable to find the 'Post' button."
            ) from error