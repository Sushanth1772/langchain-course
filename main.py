import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_ollama import ChatOllama
load_dotenv()

def main():
    information ="I am a software developer with 5 years of experience in web development. I have worked with various technologies including Python, JavaScript, and React. I am passionate about learning new technologies and improving my coding skills. In my free time, I enjoy contributing to open-source projects and participating in hackathons."
    # information = input("Please provide the information: ")
    summary="""
        Given the information {information} provided by the user i want you to create:
        1.A short summary of the information provided by the user.
        2. A list of 5 questions that can be asked to the user based on the information provided by the user.
        """
    summary_prompt = ChatPromptTemplate.from_template(summary)
    print(summary_prompt.format(information=information))
    # llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0,google_api_key=os.environ.get("GOOGLE_API_KEY"))
    # llm = ChatOllama(model="gemma3:270m", temperature=0)
    llm = ChatGroq(model="openai/gpt-oss-20b",temperature=0,max_tokens=None,reasoning_format="parsed",max_retries=2)
    chain = summary_prompt | llm
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
