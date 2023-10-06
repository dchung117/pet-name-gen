from petgen.petgen import generate_pet_name
import streamlit as st

st.title("Pet Name Generator")

pet_type = st.text_input("What kind of pet do you have?",
    value="dog",
    max_chars=15)
pet_color = st.text_input(f"What color is your {pet_type}?",
    max_chars=15)

gen_button = st.button("Generate pet names!")

if gen_button:
    response = generate_pet_name(pet_type, color=pet_color)
    st.text(response["pet_names"])