"""Browser manager."""

from __future__ import annotations

from pathlib import Path

from playwright.sync_api import Browser
from playwright.sync_api import BrowserContext
from playwright.sync_api import Page
from playwright.sync_api import Playwright
from playwright.sync_api import sync_playwright


class BrowserManager:
    """
    Responsible for managing browser lifecycle.
    """

    def __init__(
        self,
        storage_state: Path | None = None,
    ) -> None:
        self._storage_state = storage_state

        self._playwright: Playwright | None = None
        self._browser: Browser | None = None
        self._context: BrowserContext | None = None

    def start(self) -> None:
        """
        Launch Chromium.
        """

        self._playwright = sync_playwright().start()

        self._browser = self._playwright.chromium.launch(
            headless=False,
        )

        if (
            self._storage_state
            and self._storage_state.exists()
        ):
            self._context = self._browser.new_context(
                storage_state=str(self._storage_state),
            )
        else:
            self._context = self._browser.new_context()

    def new_page(self) -> Page:
        """
        Create a browser tab.
        """

        if self._context is None:
            raise RuntimeError(
                "BrowserManager.start() must be called first."
            )

        return self._context.new_page()

    def save_storage_state(self) -> None:
        """
        Save cookies and local storage.
        """

        if (
            self._context is None
            or self._storage_state is None
        ):
            return

        self._context.storage_state(
            path=str(self._storage_state),
        )

    def stop(self) -> None:
        """
        Close browser resources.
        """

        if self._context:
            self._context.close()

        if self._browser:
            self._browser.close()

        if self._playwright:
            self._playwright.stop()