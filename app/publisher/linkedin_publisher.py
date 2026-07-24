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

    def publish(
        self,
        content: str,
        image_path: str | None = None,
    ) -> None:
        """
        Publish a LinkedIn post.
        """

        self._browser.start()

        try:
            page = self._browser.new_page()

            self._open_feed(page)
            self._open_post_dialog(page)

            # Upload image first
            if image_path:
                self._upload_image(
                    page=page,
                    image_path=image_path,
                )

            # Always enter the content
            self._enter_content(
                page=page,
                content=content,
            )

            # self._publish_post(page)

            print("\n✅ LinkedIn post has been prepared.")
            print("👉 Please review it in the browser and click 'Post' manually.")

            input("\nPress Enter after you're done posting...")

        finally:
            self._browser.stop()

    def _open_feed(
        self,
        page: Page,
    ) -> None:

        print("➡️ Opening LinkedIn feed...")

        page.goto(
            "https://www.linkedin.com/feed/",
            wait_until="domcontentloaded",
        )

        page.wait_for_timeout(5000)

        print("✅ Feed page opened.")

    def _open_post_dialog(
        self,
        page: Page,
    ) -> None:

        print("➡️ Looking for 'Start a post' button...")

        start_post = page.get_by_text(
            "Start a post",
            exact=True,
        )

        start_post.wait_for(
            state="visible",
            timeout=15000,
        )

        start_post.click()

        page.wait_for_timeout(2000)

        print("✅ Post dialog opened.")

    def _enter_content(
        self,
        page: Page,
        content: str,
    ) -> None:

        selectors = [
            "div[contenteditable='true'][role='textbox']",
            ".ql-editor",
            "div[contenteditable='true']",
        ]

        editor = None

        for selector in selectors:

            try:

                locator = page.locator(selector).first

                locator.wait_for(
                    state="visible",
                    timeout=3000,
                )

                editor = locator

                print(f"✅ Editor found: {selector}")

                break

            except TimeoutError:
                continue

        if editor is None:
            raise RuntimeError(
                "Unable to locate LinkedIn editor."
            )

        editor.click()

        page.keyboard.type(
            content,
            delay=5,
        )

        print("✅ Content entered.")
    def _upload_image(
        self,
        page: Page,
        image_path: str,
    ) -> None:
        """
        Upload image to LinkedIn post.
        """

        print("➡️ Uploading image...")

        image_button = page.locator(
            "button.share-promoted-detour-button[aria-label='Add media']"
        )

        image_button.wait_for(
            state="visible",
            timeout=10000,
        )

        with page.expect_file_chooser() as fc:
            image_button.click()

        file_chooser = fc.value
        file_chooser.set_files(image_path)

        print("✅ Image selected.")

        page.wait_for_timeout(8000)

        print("✅ Image uploaded.")
           

    def _publish_post(
        self,
        page: Page,
    ) -> None:

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