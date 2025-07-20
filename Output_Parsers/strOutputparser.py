from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
)


# 1st prompt
template1 = PromptTemplate(
    input_variables=["input"],
    template="Generate a Report on this topic: {input}",
)


# prompt1 = template1.invoke({"input": "What is the capital of France?"})

# result =llm.invoke(prompt1)

# print("result1:", result)
# second prompt
template2 = PromptTemplate(
    input_variables=["input"],
    template="Print input and a 5 line summary on this input : {input}",
)

# prompt2 = template2.invoke({"input": result.content})


# result2 = llm.invoke(prompt2)

# print("result2:", result2)


parser = StrOutputParser()


chain = template1 | llm | parser | template2 | llm | parser


result =chain.invoke({"input": "BlackHole"})


print("Final Result:", result)




# The BlackHole Exploit Kit (BHEK), active from 2007-2013, was a highly successful modular exploit kit that compromised websites and targeted user vulnerabilities in software like Flash and Java.  It used polymorphic techniques to evade detection and delivered various malicious payloads, including ransomware and banking Trojans, resulting in widespread data breaches and financial losses.  Its modular design and open-sourced nature (post-decline) made it highly adaptable and valuable for studying exploit development.  Effective mitigation includes software updates, robust security software, and user education.  BHEK's legacy continues to influence modern exploit kit development, highlighting the ongoing need for strong security measures.