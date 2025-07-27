from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(input_variables=["input"], template="Write Joke about {input}?")

prompt2 = PromptTemplate(input_variables=["input"], template="explain This Joke  {input}.")

model = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
)


parser = StrOutputParser()

chain = RunnableSequence(
    prompt1,
    model,
    parser,
    prompt2,
    model,  
    parser,
)


result = chain.invoke("Python")


print(result)  # Output: A joke about Python programming language