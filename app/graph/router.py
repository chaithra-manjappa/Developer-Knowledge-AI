from __future__ import annotations

from app.graph.state import WorkflowState


def should_search(
    state: WorkflowState,
) -> str:

    if state["decision"].needs_web_search:

        return "search"

    return "content"