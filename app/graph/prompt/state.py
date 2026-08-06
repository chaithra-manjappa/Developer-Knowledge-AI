from typing import TypedDict

from app.models.decision import Decision


class PromptState(TypedDict):

    decision: Decision

    prompt: str