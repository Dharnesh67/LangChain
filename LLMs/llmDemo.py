# Import the OpenAI LLM wrapper from langchain_openai
from langchain_openai import OpenAI

# Import the function to load environment variables
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# We dont have credits in OpenAi # so we are using the model name directly


# Initialize the OpenAI language model with the specified model name
llm = OpenAI(model="gpt-3.5-turbo")

# Invoke the language model with a prompt and get the response
result = llm.invoke("What is the capital of France?")