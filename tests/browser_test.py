"""Temporary BrowserManager test."""

from app.browser.browser_manager import BrowserManager


def main() -> None:
    browser = BrowserManager()

    browser.start()

    page = browser.new_page()

    page.goto("https://www.google.com")

    input("Press Enter to close...")

    browser.stop()


if __name__ == "__main__":
    main()