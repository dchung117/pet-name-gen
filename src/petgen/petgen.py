from typing import Optional
from langchain.llms import OpenAI

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

    names = llm(f"I have a pet {pet} and I want to give it a cool name. Give me {n} names.")

    return names