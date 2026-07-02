"""LinkedIn login setup."""

from pathlib import Path

from app.browser.browser_manager import BrowserManager


def main() -> None:
    browser = BrowserManager(
        storage_state=Path("sessions/linkedin.json"),
    )

    browser.start()

    page = browser.new_page()

    page.goto("https://www.linkedin.com/login")

    print("Please log in to LinkedIn.")
    input("After logging in successfully, press Enter...")

    browser.save_storage_state()

    browser.stop()

    print("✅ LinkedIn session saved successfully.")


if __name__ == "__main__":
    main()