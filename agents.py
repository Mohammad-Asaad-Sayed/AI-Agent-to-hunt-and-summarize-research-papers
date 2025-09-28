import asyncio
import os
import arxiv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.messages import TextMessage, ToolCallRequestEvent, ToolCallExecutionEvent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo, ModelFamily
from dotenv import load_dotenv

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")

groq_model_info = ModelInfo(
    vision=False,
    function_calling=True,
    json_output=True,
    family=ModelFamily.UNKNOWN,
    structured_output=True,
)

# ---- Tool function ----
def search_arxiv(query: str, max_results: int = 5):
    """Search arXiv for papers matching a query."""
    client = arxiv.Client()
    search = arxiv.Search(query=query, max_results=max_results)

    papers = []
    for paper in client.results(search):
        papers.append({
            "title": paper.title,
            "authors": [author.name for author in paper.authors],
            "summary": paper.summary,
            "url": paper.entry_id,
        })
    return papers


def teamConfig():
    model = OpenAIChatCompletionClient(
        model="llama-3.3-70b-versatile",   # ✅ supported Groq model
        api_key=groq_key,
        base_url="https://api.groq.com/openai/v1",
        model_info=groq_model_info,
    )

    arxiv_agent = AssistantAgent(
        name="ArxivAgent",
        system_message="Search arXiv for relevant papers using the provided tool.",
        model_client=model,
    )

    researcher = AssistantAgent(
        name="Researcher",
        system_message=(
            "Analyze papers and create a markdown report with: "
            "intro, research overview, and for each paper: "
            "title, authors, summary, URL, problem, and approach."
        ),
        model_client=model,
    )

    # Round-robin workflow
    team = RoundRobinGroupChat([arxiv_agent, researcher], max_turns=5)
    return team


async def orchestrate(team, task):
    async for message in team.run_stream(task=task):
        if isinstance(message, TextMessage):
            print(f"[{message.source}]: {message.content}")
        elif isinstance(message, ToolCallRequestEvent):
            print(f"[ToolCallRequest]: {message.to_text()}")
        elif isinstance(message, ToolCallExecutionEvent):
            print(f"[ToolCallExecution]: {message.to_text()}")
        yield message   # ✅ so it’s iterable


async def main(task):
    team = teamConfig()
    async for msg in orchestrate(team, task):
        pass   # here you could forward to Streamlit instead of just printing


if __name__ == "__main__":
    task = "find best papers on GAN for image generation"
    asyncio.run(main(task))
