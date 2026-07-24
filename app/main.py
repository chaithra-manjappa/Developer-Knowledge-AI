"""Application entry point."""

from pathlib import Path

from app.agents.decision_agent import DecisionAgent
from app.agents.image_agent import ImageAgent
from app.agents.linkedin_writer_agent import LinkedInWriterAgent
from app.agents.search_agent import SearchAgent

from app.clients.gemini_client import GeminiClient
from app.clients.groq_client import GroqClient

from app.config.env import EnvLoader
from app.config.settings import Settings

from app.publisher.linkedin_publisher import LinkedInPublisher

from app.services.prompt_service import PromptService

from app.tools.save_image_tool import SaveImageTool
from app.tools.tavily_search_tool import TavilySearchTool
from app.clients.pollinations_client import PollinationsClient
from app.agents.image_prompt_agent import ImagePromptAgent

def main() -> None:
    """Start the application."""

    print("🚀 Welcome to Personal Brand AI!\n")

    # ----------------------------------------------------
    # Load Environment
    # ----------------------------------------------------

    EnvLoader(Path(".env")).load()

    settings = Settings.from_environment()

    # ----------------------------------------------------
    # User Input
    # ----------------------------------------------------

    topic = input("📝 Enter a LinkedIn topic: ").strip()

    if not topic:
        print("❌ Topic cannot be empty.")
        return

    # ----------------------------------------------------
    # Shared Services
    # ----------------------------------------------------

    groq_client = GroqClient(
        api_key=settings.llm_api_key,
        model=settings.llm_model,
    )

    pollinations_client = PollinationsClient()

    prompt_service = PromptService(
        prompts_directory=Path("app/prompts"),
    )

    save_image_tool = SaveImageTool()

    # ----------------------------------------------------
    # Decision Agent
    # ----------------------------------------------------

    decision_agent = DecisionAgent(
        groq_client=groq_client,
        prompt_service=prompt_service,
    )

    decision = decision_agent.analyse(topic)

    print("\n🧠 Decision Agent")
    print("=" * 60)
    print(f"Topic            : {decision.topic}")
    print(f"Web Search       : {decision.needs_web_search}")
    print(f"Image Generation : {decision.needs_image}")
    print(f"Review           : {decision.needs_review}")
    print(f"Reason           : {decision.reason}")
    print("=" * 60)

    # ----------------------------------------------------
    # Search Agent
    # ----------------------------------------------------

    search_results = []

    if decision.needs_web_search:

        tavily_tool = TavilySearchTool(
            api_key=settings.tavily_api_key,
        )

        search_agent = SearchAgent(
            search_tool=tavily_tool,
        )

        search_results = search_agent.search(
            topic=decision.topic,
        )

        print("\n🌍 Search Results")
        print("=" * 60)

        if not search_results:
            print("No search results found.")

        for index, result in enumerate(
            search_results,
            start=1,
        ):
            print(f"\n{index}. {result.title}")
            print(result.url)

        print("=" * 60)

    else:
        print("\n📚 Existing LLM knowledge is sufficient.")

    # ----------------------------------------------------
    # Image Agent
    # ----------------------------------------------------

    generated_image = None

    if decision.needs_image:

        image_prompt_agent = ImagePromptAgent(
            client=groq_client,
            prompt_service=prompt_service,
        )

        image_prompt = image_prompt_agent.generate(
            topic=decision.topic,
            search_results=search_results,
        )

        print("\n🎨 Final Image Prompt")
        print("=" * 80)
        print(image_prompt)
        print("=" * 80) 

        image_agent = ImageAgent(
            image_client=pollinations_client,
            save_image_tool=save_image_tool,
        )

        generated_image = image_agent.generate(
            topic=decision.topic,
            image_prompt=image_prompt,
        )

        print("\n🖼 Generated Image")
        print("=" * 60)
        print(generated_image.file_path)
        print("=" * 60)

    # ----------------------------------------------------
    # Writer Agent
    # ----------------------------------------------------

    writer_agent = LinkedInWriterAgent(
        client=groq_client,
        prompt_service=prompt_service,
    )

    post = writer_agent.generate(
        topic=decision.topic,
        search_results=search_results,
    )

    # ----------------------------------------------------
    # Reviewer Agent (Coming Soon)
    # ----------------------------------------------------

    if decision.needs_review:
        print("\n📝 Reviewer Agent will run (coming soon).")

    # ----------------------------------------------------
    # Output
    # ----------------------------------------------------

    print("\n" + "=" * 80)
    print("✨ Generated LinkedIn Post")
    print("=" * 80)
    print(post)

    if generated_image:
        print("\n🖼 Generated Image Location")
        print(generated_image.file_path)

    print("=" * 80)

    # ----------------------------------------------------
    # Publish
    # ----------------------------------------------------

    choice = input(
        "\nPublish to LinkedIn? (y/n): "
    ).strip().lower()

    if choice == "y":
        publisher = LinkedInPublisher()
        publisher.publish(
    content=post,
    image_path=generated_image.file_path if generated_image else None,
    )
    else:
        print("Publishing cancelled.")


if __name__ == "__main__":
    main()