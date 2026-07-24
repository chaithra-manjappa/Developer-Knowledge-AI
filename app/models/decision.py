from dataclasses import dataclass


@dataclass
class Decision:
    needs_web_search: bool
    needs_image: bool
    needs_review: bool
    topic: str
    reason: str