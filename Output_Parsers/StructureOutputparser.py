from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
)


schema = [
    ResponseSchema(
        name="Fact1",
        description="The first fact about the topic",
    ),
    ResponseSchema(
        name="Fact2",
        description="The second fact about the topic",
    ),
]


parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
    input_variables=["TOPIC"],
    template="Generate a report on the topic: {TOPIC}.\n\n"
    "Provide two facts about the topic in the following format:\n"
    "{format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()},
)



prompt=template.format(TOPIC="Black Hole")

llm_response = llm.invoke(prompt)

parsed_response = parser.parse(llm_response.content)

print("Parsed Response:", parsed_response)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(str(parsed_response))




# {'Fact1': 'Black holes are regions of spacetime where gravity is so strong that nothing, not even light, can escape.', 'Fact2': 'Black holes are formed from the remnants of massive stars that have collapsed at the end of their life cycle.'}
