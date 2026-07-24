"""Search Result Model."""

from dataclasses import dataclass


@dataclass
class SearchResult:
    """
    Represents one search result.
    """

    title: str
    content: str
    url: str