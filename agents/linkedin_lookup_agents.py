import os
from tempfile import template

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
from dotenv import load_dotenv

from tools.tools import get_profile_url_tavily

load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini",
    )
    template = """
    Give me the direct LinkedIn profile URL of {name_of_person}.
    Return ONLY ONE valid URL, nothing else, no explanation, no list.
    The output must be a single string in this format:
    https://www.linkedin.com/in/...
    """

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the Linkedin page URL",
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    aganet_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = aganet_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    linkdin_url = lookup(name="Viplav Dube")
    print(linkdin_url)
