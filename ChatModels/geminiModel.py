from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


ChatModel=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash")



x=input("Enter your question: ")
result=ChatModel.invoke(x)

print(result.content)