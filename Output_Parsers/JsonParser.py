from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os
import json

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
)

parser = JsonOutputParser()

# Step 1: Define the prompt template (with format instructions placeholder)
template1 = PromptTemplate(
    input_variables=["input", "format_instructions"],
    template="""
You are an expert travel guide.

Task:
List several popular cities in the country: {input}.
For each city, provide a brief explanation of why it is popular.

Respond ONLY in the following JSON format:
{format_instructions}
"""
)

# Step 2: Apply partial() to inject format instructions
partial_template = template1.partial(
    format_instructions=parser.get_format_instructions()
)

# Step 3: Format final prompt
prompt = partial_template.format(input="India")

# Step 4: Call the model
result = llm.invoke(prompt)

# Step 5: Parse the JSON output
final_result = parser.parse(result.content)
print("Parsed Result:", final_result)
print("Result Type:", type(final_result))

# Step 6: Save to JSON file
with open("JSONPARSER.json", "w", encoding="utf-8") as f:
    json.dump(final_result, f, indent=2)
