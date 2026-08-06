from dataclasses import dataclass


@dataclass
class Decision:

    topic: str

    content_type: str

    needs_web_search: bool

    needs_examples: bool

    needs_source_links: bool

    difficulty: str

    target_audience: str

    reason: str