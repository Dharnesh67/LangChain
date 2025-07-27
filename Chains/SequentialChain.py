from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file (for API keys, etc.)
load_dotenv()

# Initialize the Gemini model with specified parameters
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
# Initialize a parser to extract string output from the model's response
parser = StrOutputParser()

# Define a prompt template for generating a detailed report on a given topic
prompt = PromptTemplate(
    input_variables=["topic"],
    template=(
        "You are an expert research assistant. "
        'Write a detailed, well-structured report on the topic: "{topic}". '
        "Begin with an engaging introduction, followed by several unique, insightful facts or perspectives. "
        "Conclude with a clear summary of key points. "
        "Use professional, accessible language and avoid repetition or generic statements."
    ),
)

# Define a prompt template for summarizing the generated report
prompt2 = PromptTemplate(
    input_variables=["text"],
    template=(
        'Summarize the following report on "{text}" in 5 Points, highlighting the most important insights and conclusions. '
        "Ensure the summary is clear, concise, and suitable for a general audience."
    ),
)


# # Generate a detailed report on the ISS topic using the first prompt
# model_response = model.invoke(prompt.format(topic="ISS (International Space Station)"))

# # Parse the model's response to extract the text content
# parsed_response = parser.parse(model_response.content)

# # Print the parsed detailed report
# print("Parsed Response 1:", parsed_response)

# # Generate a summary of the detailed report using the second prompt
# model_response2 = model.invoke(prompt2.format(text=parsed_response))

# # Parse the summary response to extract the text content
# parsed_response2 = parser.parse(model_response2.content)

# # Print the parsed summary
# print("Parsed Response 2:", parsed_response2)

chain = prompt | model | parser | prompt2 | model | parser


chain.get_graph().print_ascii()  # for debugging the chain structure

# Invoke the chain with a specific topic to generate the report and summary
result = chain.invoke({"topic": "ISS (International Space Station)"})

print("Final Result:", result)


# python .\SequentialChain.py
# Final Result: 1. **Unique Scientific Research:** The ISS provides a unique microgravity environment allowing for scientific breakthroughs impossible on Earth, impacting fields like materials science, medicine, and physics.


# 2. **Human Adaptation Studies:**  Research on the ISS is crucial for understanding the long-term effects of spaceflight on the human body and mind, informing future long-duration space missions.

# 3. **International Collaboration:** The ISS exemplifies successful international cooperation, demonstrating the potential for shared scientific goals to overcome geopolitical divides.

# 4. **Sustainable Space Operations:**  The ISS highlights the challenges of managing orbital debris and resources in space, providing valuable lessons for future sustainable space infrastructure.

# 5. **Technological Innovation:** The ISS drives technological advancements with applications both in space and on Earth, benefiting various sectors through spin-off technologies.
# (venv) PS C:\Users\Dharmesh raikwar\Desktop\LangchainModels\Chains>
