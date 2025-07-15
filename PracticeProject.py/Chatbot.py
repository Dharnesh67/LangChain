from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
load_dotenv()


model=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
temperature=0.7
                             )

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input("You: ")
    chat_history.append(
        HumanMessage(content=user_input)
    )
    if user_input.lower() == "exit":
        print("Exiting the chatbot. Goodbye!")
        break
    else:
        model_response = model.invoke(chat_history)
        chat_history.append(
            AIMessage(content=model_response.content)
        )
        print(f"Chatbot: {model_response.content}")