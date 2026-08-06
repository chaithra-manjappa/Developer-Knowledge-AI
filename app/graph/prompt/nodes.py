from __future__ import annotations

from app.graph.prompt.state import PromptState


class PromptNodes:

    # ---------------------------------

    def learning_node(
        self,
        state: PromptState,
    ) -> PromptState:

        state["prompt"] += """

Additional Instructions

- Explain concepts step by step.
- Explain WHY each concept exists.
- Include common mistakes.
- Include best practices.
"""

        return state

    # ---------------------------------

    def interview_node(
        self,
        state: PromptState,
    ) -> PromptState:

        state["prompt"] += """

Additional Instructions

- Generate ONLY topic specific interview questions.
- Avoid generic questions.
- Include scenario questions.
- Include debugging questions.
- Include coding questions.
- Explain every answer.
"""

        return state

    # ---------------------------------

    def roadmap_node(
        self,
        state: PromptState,
    ) -> PromptState:

        state["prompt"] += """

Additional Instructions

- Divide into phases.
- Suggest projects.
- Recommend milestones.
"""

        return state

    # ---------------------------------

    def comparison_node(
        self,
        state: PromptState,
    ) -> PromptState:

        state["prompt"] += """

Additional Instructions

- Compare feature by feature.
- Mention pros.
- Mention cons.
- Mention tradeoffs.
"""

        return state

    # ---------------------------------

    def architecture_node(
        self,
        state: PromptState,
    ) -> PromptState:

        state["prompt"] += """

Additional Instructions

- Explain architecture.
- Explain data flow.
- Explain scalability.
"""

        return state

    # ---------------------------------

    def linkedin_node(
        self,
        state: PromptState,
    ) -> PromptState:

        state["prompt"] += """

Additional Instructions

- Write conversationally.
- Start with a hook.
- End with engagement.
"""

        return state

    # ---------------------------------

    def summary_node(
        self,
        state: PromptState,
    ) -> PromptState:

        return state

    # ---------------------------------

    def cheatsheet_node(
        self,
        state: PromptState,
    ) -> PromptState:

        return state

    # ---------------------------------

    def examples_node(
        self,
        state: PromptState,
    ) -> PromptState:

        if state["decision"].needs_examples:

            state["prompt"] += """

Include practical examples.
Include code wherever possible.
"""

        return state

    # ---------------------------------

    def source_links_node(
        self,
        state: PromptState,
    ) -> PromptState:

        if state["decision"].needs_source_links:

            state["prompt"] += """

Add an Official Resources section with links.
"""

        return state

    # ---------------------------------

    def search_context_node(
        self,
        state: PromptState,
    ) -> PromptState:

        if state["decision"].needs_web_search:

            state["prompt"] += """

Treat search results as the source of truth.
"""

        return state