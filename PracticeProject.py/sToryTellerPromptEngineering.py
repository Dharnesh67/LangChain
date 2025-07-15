from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

st.title("Story Generator for Kids")
st.header("Create a Story for a 10-Year-Old!")

# Collect three inputs from the user
character = st.selectbox(
    "Choose a main character:",
    ["Dragon", "Astronaut", "Princess", "Robot", "Detective", "Pirate"],
    key="character"
)
setting = st.selectbox(
    "Choose a setting:",
    ["Forest", "Space", "Castle", "Underwater", "City", "Desert"],
    key="setting"
)
theme = st.selectbox(
    "Choose a theme or lesson:",
    ["Friendship", "Bravery", "Honesty", "Teamwork", "Kindness", "Perseverance"],
    key="theme"
)

template=PromptTemplate(
    input_variables=["character", "setting", "theme"],
    template="""You are a creative storyteller. Write a short story for a 10-year-old child. The story
    should feature a main character who is a {character}, take place in {setting}, and teach a lesson about {theme}. Keep the story fun, imaginative, and age-appropriate."""
)

prompt=template.format(
    character=character,
    setting=setting,
    theme=theme
)


if st.button("Generate Story"):
    if character and setting and theme:
        ChatModel = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        result = ChatModel.invoke(prompt)
        st.subheader("Your Story:")
        st.write(result.content)
    else:
        st.warning("Please fill in all three fields to generate a story.")