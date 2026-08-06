from typing import TypedDict

from app.models.decision import Decision


class WorkflowState(TypedDict):
    user_request: str

    decision: Decision | None

    search_results: list

    content: str

    hashtags: str