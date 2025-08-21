from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agents import lookup
from third_party.linkedin import scrape_linkedin_profile

def get_linkedin_url(name:str) -> str:
    linkedin_url = lookup(name=name)
    return  linkedin_url

def get_brief_information(name:str) ->str:
    target_linkedin_profile_url = get_linkedin_url(name=name)
    person_information = scrape_linkedin_profile(
        linkedin_profile_url=target_linkedin_profile_url, mock=True
    )
    summary_template = """
                Give me the information {information} about a person from I want you to create:
                1.  Short summery
                2.  Two interesting fact about them
            """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": person_information})
    return res


if __name__ == "__main__":
    information_brief = get_brief_information(name="Viplav Dube")
    print(information_brief)
