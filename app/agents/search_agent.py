"""Search Agent."""

from __future__ import annotations

from app.models.search_result import SearchResult


class SearchAgent:
    """
    Agent responsible for retrieving the latest information
    using the configured search tool.
    """

    def __init__(self, search_tool) -> None:
        """
        Args:
            search_tool: Any search tool that exposes
                         a search(query, max_results) method.
        """
        self._search_tool = search_tool

    def search(
        self,
        topic: str,
        max_results: int = 5,
    ) -> list[SearchResult]:
        """
        Search for the latest information.

        Args:
            topic: Search query.
            max_results: Maximum number of search results.

        Returns:
            List of SearchResult objects.
        """

        print(f"\n🔍 Searching web for: {topic}")

        results = self._search_tool.search(
            query=topic,
            max_results=max_results,
        )

        print(f"✅ Found {len(results)} results")

        return results