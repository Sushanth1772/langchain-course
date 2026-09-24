from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
import os
load_dotenv()

@tool
def search(query:str)-> str:
    """
    Tool that searches over the internet
    Args:
        query: The query search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return "Tokyo weather is sunny"

llm = ChatGroq(model="openai/gpt-oss-20b")
tools=[search]
agent= create_agent(model=llm,tools=tools)
def main():
    result = agent.invoke({"messages": [HumanMessage(content="Whats the weather in tokyo?")]})    
    print(result)

if __name__ == "__main__":
    main()
