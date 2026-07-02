"""Application entry point."""

from pathlib import Path

from app.agents.linkedin_writer_agent import LinkedInWriterAgent
from app.clients.groq_client import GroqClient
from app.config.env import EnvLoader
from app.config.settings import Settings
from app.services.prompt_service import PromptService
from app.publishers.linkedin_publisher import LinkedInPublisher

def main() -> None:
    """Start the application."""

    print("🚀 Welcome to Personal Brand AI!\n")

    # Load environment variables
    EnvLoader(Path(".env")).load()

    # Read configuration
    settings = Settings.from_environment()

    # Ask the user for a topic
    topic = input("📝 Enter a LinkedIn topic: ").strip()

    if not topic:
        print("❌ Topic cannot be empty.")
        return

    # Create the Groq client
    client = GroqClient(
        api_key=settings.llm_api_key,
        model=settings.llm_model,
    )

    # Create the prompt service
    prompt_service = PromptService(
        prompts_directory=Path("app/prompts"),
    )

    # Create the LinkedIn agent
    agent = LinkedInWriterAgent(
        client=client,
        prompt_service=prompt_service,
    )

    # Generate the post
    post = agent.generate(topic)

    print("\n" + "=" * 80)
    print("✨ Generated LinkedIn Post")
    print("=" * 80)
    print(post)
    print("=" * 80)

    choice = input(
    "\nPublish this post? (y/n): "
).strip().lower()

if choice == "y":
    publisher = LinkedInPublisher()
    publisher.publish(post)
else:
    print("Publishing cancelled.")


if __name__ == "__main__":
    main()