# Import the ChatOpenAI class from langchain_openai, which provides an interface to OpenAI's chat models
from langchain_openai import ChatOpenAI

# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables from a .env file (e.g., your OpenAI API key)
load_dotenv()

# Create an instance of the ChatOpenAI model, specifying the model name (e.g., "gpt-4")

# this has different attributes and methods than chatOpenAI class
# chatopenai(
    # model="gpt-4",
    # temperature=0.7,
    # max_tokens=1000,
    # top_p=1.0,
    # frequency_penalty=0.0,
    # presence_penalty=0.0,
    # )
chatOpenAimodel = ChatOpenAI(model="gpt-4")

# Use the model to process a prompt/question and get a response
result = chatOpenAimodel.invoke("What is the capital of INDia?")

# Print the result to the output pane or terminal

# result will be and obeject have content and other attributes
# Here we are printing the content of the result
print(result.content)
