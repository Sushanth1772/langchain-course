from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
import os

load_dotenv()


# Tool not being used as tavily search is being used for the search functionality. This is just a placeholder for future use if needed.
@tool
def search(query: str) -> str:
    """
    Tool that searches over the internet
    Args:
        query: The query search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")


llm = ChatGroq(model="openai/gpt-oss-120b")
tools = [TavilySearch()]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "You are a job search assistant. Make at most 3 searches, one per "
        "platform. Then answer with the job titles and links. Do not repeat searches."
    ),
)


def main():
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="Search for 3 top job hostings available for Gen AI Engineer in India in the platforms naukri linkedin and indeed and provide the links to the job postings"
                )
            ]
        }
    )
    print(result)


if __name__ == "__main__":
    main()
