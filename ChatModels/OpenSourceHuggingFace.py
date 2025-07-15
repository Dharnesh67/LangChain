from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")


print (f"Hugging Face Token: {token}")
if not token:
    raise ValueError("Hugging Face token not found in environment variables.")

# Create the endpoint
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=token,  # ✅ Pass token here
)

# Chat wrapper
ChatModel = ChatHuggingFace(llm=llm)

# Test query
try:
    result = ChatModel.invoke("What is the name of PM of India?")
    print(result)
except Exception as e:
    print("Error occurred:", str(e))
