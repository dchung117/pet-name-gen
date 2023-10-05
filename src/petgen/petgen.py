from typing import Optional
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_pet_name(pet: str,
    n: int = 5,
    temp: Optional[float] = 0.7) -> str:
    """
    Use OpenAI API to generate pet names.

    Args
    ----
        pet: str
            Type of pet (e.g. dog, cat, fish, etc.)
        n: int = 5
            Number of names to generate.
        temp: float = 0.7
            Temperature for sampling during text generation.
    Return
    ------
        str:
            Response from LLM
    """
    llm = OpenAI(temperature=temp)

    prompt_template = PromptTemplate(
        input_variables = ["pet", "n"],
        template = "I have a pet {pet} and I want to give it a cool name. Give me {n} names."
    )
    chain = LLMChain(
        llm=llm,
        prompt=prompt_template
    )

    response = chain(
        {"pet": pet, "n": n}
    )

    return response