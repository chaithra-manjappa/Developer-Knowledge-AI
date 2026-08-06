"""Application entry point."""

from pathlib import Path

from app.config.env import EnvLoader
from app.config.settings import Settings

from app.graph.factory import WorkflowFactory

from app.publisher.linkedin_publisher import LinkedInPublisher


def main() -> None:

    print("🚀 Welcome to Personal Content AI\n")

    EnvLoader(
        Path(".env"),
    ).load()

    settings = Settings.from_environment()

    topic = input(
        "📝 Enter a topic: ",
    ).strip()

    if not topic:

        print("Topic cannot be empty.")

        return

    workflow = WorkflowFactory(
        settings,
    )

    result = workflow.graph.invoke(
        {
            "user_request": topic,
            "decision": None,
            "search_results": [],
            "content": "",
        }
    )

    decision = result["decision"]

    print("\n🧠 Decision")
    print("=" * 60)
    print(f"Topic            : {decision.topic}")
    print(f"Content Type     : {decision.content_type}")
    print(f"Web Search       : {decision.needs_web_search}")
    print(f"Examples         : {decision.needs_examples}")
    print(f"Source Links     : {decision.needs_source_links}")
    print(f"Difficulty       : {decision.difficulty}")
    print(f"Audience         : {decision.target_audience}")
    print("=" * 60)

    print("\n📄 Generated Content")
    print("=" * 80)
    print(result["content"])
    print("=" * 80)

    publish = input(
        "\nPublish to LinkedIn? (y/n): "
    ).lower()

    if publish == "y":

        LinkedInPublisher().publish(
            content=result["content"],
            image_path=None,
        )

    else:

        print("Publishing cancelled.")


if __name__ == "__main__":

    main()