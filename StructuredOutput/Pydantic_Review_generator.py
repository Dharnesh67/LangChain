from pydantic import BaseModel
from typing import Annotated
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import json

from pyparsing import Literal

load_dotenv()

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
 
# Define output schema
class ReviewOutput(BaseModel):
    date: str
    sentiment: Annotated[str, "positive", "neutral", "negative"]  # could also be Literal["positive", "neutral", "negative"]
    Summary: Annotated[str, "brief summary of the review"]

# Load all reviews
with open("review.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Split reviews – adjust delimiter as needed (e.g., '\n---\n' or numbered)
reviews = [r.strip() for r in content.split("\n\n") if r.strip()]

# Prepare structured model
structured_model = model.with_structured_output(ReviewOutput)

# Process each review
all_outputs = []
for idx, review in enumerate(reviews):
    try:
        prompt = (
            "Analyze the following review and provide the date, sentiment (positive, neutral, or negative), and a brief summary:\n\n"
            + review
        )
        response = structured_model.invoke(prompt)
        all_outputs.append(response.dict())
    except Exception as e:
        print(f"Error in review {idx+1}: {e}")

# Save to JSON
with open("output.json", "w", encoding="utf-8") as out_file:
    json.dump(all_outputs, out_file, ensure_ascii=False, indent=4)

print(f"Processed {len(all_outputs)} reviews and saved to output.json.")
