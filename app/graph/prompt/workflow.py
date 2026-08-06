from __future__ import annotations

from langgraph.graph import END
from langgraph.graph import START
from langgraph.graph import StateGraph

from app.graph.prompt.nodes import PromptNodes
from app.graph.prompt.router import route_content_type
from app.graph.prompt.state import PromptState


def build_prompt_graph():

    nodes = PromptNodes()

    workflow = StateGraph(
        PromptState,
    )

    workflow.add_node(
        "learning",
        nodes.learning_node,
    )

    workflow.add_node(
        "interview",
        nodes.interview_node,
    )

    workflow.add_node(
        "roadmap",
        nodes.roadmap_node,
    )

    workflow.add_node(
        "comparison",
        nodes.comparison_node,
    )

    workflow.add_node(
        "architecture",
        nodes.architecture_node,
    )

    workflow.add_node(
        "linkedin",
        nodes.linkedin_node,
    )

    workflow.add_node(
        "summary",
        nodes.summary_node,
    )

    workflow.add_node(
        "cheatsheet",
        nodes.cheatsheet_node,
    )

    workflow.add_node(
        "examples",
        nodes.examples_node,
    )

    workflow.add_node(
        "sources",
        nodes.source_links_node,
    )

    workflow.add_node(
        "search",
        nodes.search_context_node,
    )

    workflow.add_conditional_edges(
        START,
        route_content_type,
        {
            "learning_guide": "learning",
            "interview_questions": "interview",
            "roadmap": "roadmap",
            "comparison": "comparison",
            "architecture": "architecture",
            "linkedin_post": "linkedin",
            "summary": "summary",
            "cheatsheet": "cheatsheet",
        },
    )

    for node in [
        "learning",
        "interview",
        "roadmap",
        "comparison",
        "architecture",
        "linkedin",
        "summary",
        "cheatsheet",
    ]:

        workflow.add_edge(
            node,
            "examples",
        )

    workflow.add_edge(
        "examples",
        "sources",
    )

    workflow.add_edge(
        "sources",
        "search",
    )

    workflow.add_edge(
        "search",
        END,
    )

    return workflow.compile()