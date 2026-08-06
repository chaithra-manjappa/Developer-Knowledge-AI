from __future__ import annotations

from app.graph.prompt.workflow import build_prompt_graph


class PromptEngineeringAgent:

    def __init__(self):

        self._graph = build_prompt_graph()

    def optimize(
        self,
        decision,
        prompt,
    ) -> str:

        state = self._graph.invoke(
            {
                "decision": decision,
                "prompt": prompt,
            }
        )

        return state["prompt"]