from dotenv import load_dotenv

from typing import Optional
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools, initialize_agent, AgentType, AgentExecutor

load_dotenv()

def generate_pet_name(pet: str,
    n: int = 5,
    color: Optional[str] = None,
    temp: Optional[float] = 0.7) -> str:
    """
    Use OpenAI API to generate pet names.

    Args
    ----
        pet: str
            Type of pet (e.g. dog, cat, fish, etc.)
        n: int = 5
            Number of names to generate.
        color: Optional[str] = None
            Optionally mention pet color to generate names.
        temp: Optional[float] = 0.7
            Temperature for sampling during text generation.
    Return
    ------
        str:
            Response from LLM
    """
    llm = OpenAI(temperature=temp)

    prompt = "I have a pet {pet} and I want to give it a cool name."
    input_variables = ["pet", "n"]
    input_dict = {"pet": pet, "n": n}
    if color:
        prompt += " It is {color} in color."
        input_variables.append("color")
        input_dict["color"] = color
    prompt += " Give me {n} names."
    prompt_template = PromptTemplate(
        input_variables = input_variables,
        template = prompt
    )
    chain = LLMChain(
        llm=llm,
        prompt=prompt_template,
        output_key="pet_names"
    )

    response = chain(
        input_dict
    )

    return response

def get_agent(temp: Optional[float] = 0.5) -> AgentExecutor:
    """
    Create an agent w/ OpenAI LLM and access to Wikipedia and llm-math libaries.

    Args
    ----
        temp: Optional[float] = 0.5
            Temperature for sampling during text generation
    Return
    ------
        AgentExecutor
            Langchain agent

    """
    llm = OpenAI(temperature=temp)

    tools = load_tools(["wikipedia", "llm-math"],
        llm=llm)

    agent = initialize_agent(tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True)

    return agent