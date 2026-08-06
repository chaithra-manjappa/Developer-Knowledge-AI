from pathlib import Path

from app.agents.content_agent import ContentAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.search_agent import SearchAgent

from app.clients.groq_client import GroqClient

from app.config.settings import Settings

from app.graph.nodes import WorkflowNodes
from app.graph.workflow import build_graph

from app.services.prompt_service import PromptService

from app.tools.tavily_search_tool import TavilySearchTool
from app.agents.prompt_engineering_agent import PromptEngineeringAgent
from app.agents.hashtag_agent import HashtagAgent

class WorkflowFactory:

    def __init__(
        self,
        settings: Settings,
    ):

        groq = GroqClient(
            api_key=settings.llm_api_key,
            model=settings.llm_model,
        )

        prompts = PromptService(
            prompts_directory=Path("app/prompts"),
        )

        decision = DecisionAgent(
            groq_client=groq,
            prompt_service=prompts,
        )

        search = SearchAgent(
            search_tool=TavilySearchTool(
                api_key=settings.tavily_api_key,
            ),
        )


        prompt_engineering = PromptEngineeringAgent()

        content = ContentAgent(
            client=groq,
            prompt_service=prompts,
            prompt_engineering=prompt_engineering,
        )

        hashtag = HashtagAgent(
            client=groq,
            prompt_service=prompts,
        )

        nodes = WorkflowNodes(
            decision,
            search,
            content,
            hashtag,
        )

        self.graph = build_graph(nodes)