from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()


Notesmodel = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
)

Quizmodel = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
)


NotesPrompt = PromptTemplate(
    input_variables=["input"],
    template="Generate Short and Simple Notes on the following topic:\n{input}\n\n",
)
quizPrompt = PromptTemplate(
    input_variables=["input"],
    template="Generate a 5 short question quiz based on the following topic:\n{input}\n\n",
)


MergeTemplate = PromptTemplate(
    input_variables=["notes", "quiz"],
    template="Merge the following notes and quiz questions into a single document:\n\n  {notes}\n\n  {quiz}",
)


parser = StrOutputParser()



parallelchain = RunnableParallel(
    {
        "notes": NotesPrompt | Notesmodel | parser,
        "quiz": quizPrompt | Quizmodel | parser,
    }
)


mergeChain = MergeTemplate | Notesmodel | parser


finalchain = parallelchain | mergeChain

print("Graph Structure:")
finalchain.get_graph().print_ascii() 

Result = finalchain.invoke({"input": "Data Science and Machine Learning"})

print("Final Result:", Result)



# Saved output to a file    
with open("ParallelChainOutput.txt", "w", encoding="utf-8") as f:
    f.write(str(Result))