"""Tavily Search Tool."""

from __future__ import annotations

from tavily import TavilyClient

from app.models.search_result import SearchResult


class TavilySearchTool:
    """
    Search tool backed by the Tavily Search API.
    """

    def __init__(
        self,
        api_key: str,
    ) -> None:

        self._client = TavilyClient(
            api_key=api_key,
        )

    def search(
        self,
        query: str,
        max_results: int = 5,
    ) -> list[SearchResult]:
        """
        Search the web.

        Args:
            query: Search query.
            max_results: Maximum number of results.

        Returns:
            List of SearchResult objects.
        """

        response = self._client.search(
            query=query,
            search_depth="advanced",
            max_results=max_results,
        )

        results: list[SearchResult] = []

        for item in response.get("results", []):

            results.append(
                SearchResult(
                    title=item.get("title", ""),
                    content=item.get("content", ""),
                    url=item.get("url", ""),
                )
            )

        return results