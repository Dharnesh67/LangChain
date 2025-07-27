from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate



load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


class Person(BaseModel):
    name: str = (Field(..., description="Name of the person"),)
    age: int = (Field(..., description="Age of the person"),)
    city: str = (Field(..., description="City where the person lives"),)


parser = PydanticOutputParser(pydantic_object=Person)


template = PromptTemplate(
    input_variables=["place"],
    template="Generate a Fictional Character:\n"
             "Place: {place}\n"
             "Respond in the following format:\n{format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)


prompt = template.format(place="India")


print("Prompt:", prompt)



chain =template | llm | parser

result = chain.invoke({"place": "India"})
print("Parsed Result:", result)
# result = llm.invoke(prompt)


# parsed_result = parser.parse(result.content)

# print("Parsed Result:", parsed_result)
# with open("PydanticOutput.txt", "w", encoding="utf-8") as f:
#     f.write(str(parsed_result))