from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()



passthrough=RunnablePassthrough()



prompt1 = PromptTemplate(input_variables=["input"], template="Write Joke about {input}?")

prompt2 = PromptTemplate(input_variables=["input"], template="explain This Joke  {input}.")

model = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
)


parser = StrOutputParser()
joke_chain = RunnableSequence(
    prompt1,
    model,
)


parellel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explain_joke": RunnableSequence(prompt2, model, parser),
    }
)

chain=RunnableSequence(
    joke_chain,
    parellel_chain,
    )
result = chain.invoke("Python")


print(result)  # Output: A joke about Python programming language





#  python .\PassThrough.py
# {'joke': "Here are a few Python jokes for you:\n\n**Classic:**\n\n> Why did the Python programmer break up with their girlfriend?\n> Because she kept messing up his **indentation**!\n\n**About Libraries:**\n\n> What do you call a Python developer who's always calm?\n> A Zen master, because they know there's a **library for everything**.\n\n**About Readability:**\n\n> Why don't Python programmers like to play hide-and-seek?\n> Because good luck hiding when your code is that **readable**!\n\n**About the Zen of Python:**\n\n> What's a Python programmer's favorite way to meditate?\n> They just type `import this`.\n\n**A Bit More Technical:**\n\n> What's a Python's favorite type of error?\n> A `TypeError`... because it's so *dynamic*!\n\nPick your favorite!", 'explain_joke': 'These are great! Let\'s break down each one:\n\n---\n\n### **Classic:**\n\n> Why did the Python programmer break up with their girlfriend?\n> Because she kept messing up his **indentation**!\n\n*   **Explanation:** In Python, **indentation** (the whitespace at the beginning of a line) is not just for readability; it\'s syntactically significant. It defines code blocks (like `if` statements, `for` loops, function definitions). If your indentation is off by even one space, your code will throw an `IndentationError` or `SyntaxError` and won\'t run.\n*   **The Joke:** It\'s a humorous exaggeration. For a Python programmer, incorrect indentation is a constant source of frustration and a critical error. The joke applies this highly technical, precise requirement to a personal relationship, implying that the "messing up" of something so fundamental to their work (and by extension, their sanity) was a deal-breaker. It plays on the stereotype of programmers being meticulous and particular.\n\n---\n\n### **About Libraries:**\n\n> What do you call a Python developer who\'s always calm?\n> A Zen master, because they know there\'s a **library for everything**.\n\n*   **Explanation:** Python has an incredibly rich ecosystem of **libraries** (also called modules or packages). These are collections of pre-written code that provide functions and tools for almost any task imaginable – web development, data analysis, machine learning, networking, graphics, etc. This means Python developers often don\'t have to "reinvent the wheel" and can quickly find existing solutions for complex problems.\n*   **The Joke:** A "Zen master" is someone who is calm, enlightened, and finds peace and solutions easily. The joke suggests that Python developers achieve this state of calm because the vast availability of libraries means they rarely face a problem for which a ready-made solution doesn\'t already exist, saving them immense time and effort.\n\n---\n\n### **About Readability:**\n\n> Why don\'t Python programmers like to play hide-and-seek?\n> Because good luck hiding when your code is that **readable**!\n\n*   **Explanation:** One of Python\'s core design philosophies is **readability**. Its syntax is often described as resembling plain English, and the mandatory indentation (mentioned in the first joke) also contributes to a clear, structured appearance. The goal is for code to be easily understood by humans, even those who didn\'t write it.\n*   **The Joke:** In hide-and-seek, the goal is to be hidden and not found. The humor comes from the absurd comparison: if Python code is *so* clear and easy to understand ("readable"), then it\'s impossible for its purpose or logic to be "hidden" or obscure. It\'s a playful jab at one of Python\'s greatest strengths.\n\n---\n\n### **About the Zen of Python:**\n\n> What\'s a Python programmer\'s favorite way to meditate?\n> They just type `import this`.\n\n*   **Explanation:** This is an "Easter egg" built right into the Python interpreter. If you open a Python shell and type `import this` and press Enter, it will output a poem called "The Zen of Python" by Tim Peters. This poem consists of 19 guiding principles for writing good Python code (e.g., "Beautiful is better than ugly," "Readability counts," "There should be one-- and preferably only one --obvious way to do it.").\n*   **The Joke:** Meditation is about reflection, finding inner peace, and contemplating guiding principles. The joke literally connects this concept to a Python command that reveals the guiding principles of the language itself. It\'s an inside joke that Python programmers appreciate because it\'s a real, accessible feature of the language.\n\n---\n\n### **A Bit More Technical:**\n\n> What\'s a Python\'s favorite type of error?\n> A `TypeError`... because it\'s so *dynamic*!\n\n*   **Explanation:**\n    *   **Dynamic Typing:** Python is a **dynamically typed** language. This means you don\'t declare the type of a variable when you create it (e.g., you don\'t say `int x = 5;`). A variable can hold values of different types throughout its lifetime. Type checking happens at *runtime* (when the code is executing), not at *compile time*.\n    *   **`TypeError`:** This error occurs when an operation is performed on a value of an inappropriate type (e.g., trying to add a string and an integer directly, or calling a method that doesn\'t exist on an object of a certain type). Because Python is dynamically typed, these type-related errors often only become apparent when the program actually tries to execute the problematic line of code.\n*   **The Joke:** The humor is a bit ironic. While `TypeError`s can be frustrating, they are a very common and direct consequence of Python\'s dynamic nature. The joke personifies the error, suggesting it\'s a "favorite" because it perfectly embodies a core characteristic of the language – its dynamism. It\'s a nod to the fact that dealing with `TypeError`s is a fundamental part of working with Python.\n\n---\n\nMy favorite is the **"Zen of Python"** joke (`import this`). It\'s a clever, accurate, and truly "inside" joke that highlights a unique and beloved feature of the language\'s philosophy.'}    
# (venv) PS C:\Users\Dharmesh raikwar\Desktop\LangchainModels\Runnables> 