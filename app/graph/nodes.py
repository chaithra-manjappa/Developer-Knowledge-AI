from __future__ import annotations

from app.graph.state import WorkflowState


class WorkflowNodes:

    def __init__(
        self,
        decision_agent,
        search_agent,
        content_agent,
        hashtag_agent,
    ):

        self._decision = decision_agent

        self._search = search_agent

        self._content = content_agent

        self._hashtags = hashtag_agent

    # -----------------------------------

    def decision_node(
        self,
        state: WorkflowState,
    ) -> WorkflowState:

        print("\n🧠 Decision Node")

        decision = self._decision.analyse(
            state["user_request"],
        )

        state["decision"] = decision

        return state

    # -----------------------------------

    def search_node(
        self,
        state: WorkflowState,
    ) -> WorkflowState:

        print("\n🌍 Search Node")

        decision = state["decision"]

        results = self._search.search(
            topic=decision.topic,
        )

        state["search_results"] = results

        return state

    # -----------------------------------

    def content_node(
        self,
        state: WorkflowState,
    ) -> WorkflowState:

        print("\n✍️ Content Node")

        state["content"] = self._content.generate(
            decision=state["decision"],
            search_results=state.get(
                "search_results",
                [],
            ),
        )

        return state

        # -----------------------------------

    def hashtag_node(
        self,
        state: WorkflowState,
    ) -> WorkflowState:

        print("\n🏷️ Hashtag Node")

        state["hashtags"] = self._hashtags.generate(
            topic=state["decision"].topic,
            content=state["content"],
        )

        state["content"] += "\n\n" + state["hashtags"]

        return state