from __future__ import annotations

from langgraph.graph import END
from langgraph.graph import START
from langgraph.graph import StateGraph

from app.graph.state import WorkflowState
from app.graph.router import should_search


def build_graph(
    nodes,
):

    workflow = StateGraph(
        WorkflowState,
    )

    workflow.add_node(
        "decision",
        nodes.decision_node,
    )

    workflow.add_node(
        "search",
        nodes.search_node,
    )

    workflow.add_node(
        "content",
        nodes.content_node,
    )

    workflow.add_node(
        "hashtags",
         nodes.hashtag_node,
    )

    workflow.add_edge(
        START,
        "decision",
    )

    workflow.add_conditional_edges(
        "decision",
        should_search,
        {
            "search": "search",
            "content": "content",
        },
    )

    workflow.add_edge(
        "search",
        "content",
    )

    workflow.add_edge(
        "content",
        "hashtags",
    )

    workflow.add_edge(
        "hashtags",
        END,
    )

    return workflow.compile()