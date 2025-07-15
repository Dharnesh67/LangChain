from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embeding=OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=32,# dimension of vector
    )


x=embeding.embed_query("What is the capital of India?")

# or we can use 


documents=[
    "India is a country in South Asia.",
    "The capital of India is New Delhi.",
    "India is the seventh-largest country by land area.",
    "India is the second-most populous country in the world.",]


result=embeding.embed_documents(documents)
print(x)

