from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from third_party.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Langchain")
    summary_template = """
            Give me the information {information} about a person from I want you to create:
            1.  Short summery
            2.  Two interesting fact about them
        """
    person_information = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/viplav-dube-116043ba/", mock=True
    )
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": person_information})
    print(res)
