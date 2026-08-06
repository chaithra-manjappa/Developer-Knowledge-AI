from __future__ import annotations

from app.graph.prompt.state import PromptState


def route_content_type(
    state: PromptState,
) -> str:

    return state["decision"].content_type