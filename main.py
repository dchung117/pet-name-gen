from dotenv import load_dotenv
from petgen.petgen import generate_pet_name

if __name__ == "__main__":
    load_dotenv()

    response = generate_pet_name("dog", color="red")
    print("Our pet dog names: ")
    print(response["text"])