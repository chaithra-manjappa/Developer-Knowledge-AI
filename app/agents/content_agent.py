"""Content Generation Agent."""

from __future__ import annotations

from app.clients.groq_client import GroqClient
from app.models.decision import Decision
from app.services.prompt_service import PromptService
from app.agents.prompt_engineering_agent import PromptEngineeringAgent


class ContentAgent:
    """
    Generates content using the Prompt Engineering Agent
    and the configured LLM.
    """

    def __init__(
        self,
        client: GroqClient,
        prompt_service: PromptService,
        prompt_engineering: PromptEngineeringAgent,
    ) -> None:

        self._client = client
        self._prompt_service = prompt_service
        self._prompt_engineering = prompt_engineering

    def generate(
        self,
        decision: Decision,
        search_results: list | None = None,
    ) -> str:

        context = self._build_context(
            search_results or [],
        )

        prompt_name = (
            f"content/{decision.content_type}.md"
        )

        try:

            # -----------------------------
            # Load Base Prompt
            # -----------------------------

            prompt = self._prompt_service.load(
                prompt_name,
                topic=decision.topic,
                context=context,
                difficulty=decision.difficulty,
                target_audience=decision.target_audience,
                needs_examples=str(
                    decision.needs_examples
                ),
                needs_source_links=str(
                    decision.needs_source_links
                ),
            )

        except FileNotFoundError:

            print(
                f"⚠️ Prompt '{prompt_name}' not found."
            )
            print(
                "Using default prompt..."
            )

            prompt = self._prompt_service.load(
                "content/default.md",
                topic=decision.topic,
                context=context,
                difficulty=decision.difficulty,
                target_audience=decision.target_audience,
                needs_examples=str(
                    decision.needs_examples
                ),
                needs_source_links=str(
                    decision.needs_source_links
                ),
            )

        # ---------------------------------------
        # Prompt Engineering Agent (LangGraph)
        # ---------------------------------------

        prompt = self._prompt_engineering.optimize(
            decision=decision,
            prompt=prompt,
        )

        print("\n🧠 Optimized Prompt")
        print("=" * 80)
        print(prompt)
        print("=" * 80)

        print("\n🤖 Generating Content...\n")

        return self._client.generate(
            prompt,
        )

    def _build_context(
        self,
        search_results: list,
    ) -> str:

        if not search_results:

            return "No search results."

        context = []

        for result in search_results:

            context.append(
                f"""
Title:
{result.title}

URL:
{result.url}

Content:
{result.content}
"""
            )

        return "\n\n".join(
            context,
        )