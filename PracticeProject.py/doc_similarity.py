from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

from dotenv import load_dotenv
load_dotenv()

embeding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=32,  # dimension of vector
    )

documents = [
    "Virat Kohli is a famous Indian cricketer.",
   "rohit Sharma is the captain of the Indian cricket team.",
    "Sachin Tendulkar is considered one of the greatest batsmen in cricket history.",
    "MS Dhoni is known for his captaincy and finishing skills in cricket.",
    "Rohit Sharma holds the record for the highest individual score in One Day Internationals (ODIs).",
    "Kapil Dev led India to its first Cricket World Cup victory in 1983.",
    "Anil Kumble is India's highest wicket-taker in Test cricket.",
    "Sunil Gavaskar was the first player to score 10,000 runs in Test"
]
query_embedding=embeding.embed_query("Who is the captain of the Indian cricket team?")
doc_embeddings = embeding.embed_documents(documents)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]


index,score=sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[0]

print(f"Most similar document: {documents[index]}")
print(f"Similarity score: {score:.4f}")


