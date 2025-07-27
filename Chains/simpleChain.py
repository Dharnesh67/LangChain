from langchain_core.output_parsers import StrOutputParser 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()


prompt = PromptTemplate(
    input_variables=["topic"],
    template=(
        "You are a knowledgeable assistant. "
        "List 5 interesting and lesser-known facts about {topic}. "
        "Make each fact concise and unique."
    ),
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
)

parser = StrOutputParser()



chain = prompt | model | parser


chain.get_graph().print_ascii()

result = chain.invoke({"topic": "Nebulae and Star Formation"})


print("Final Result:", result)



# (venv) PS C:\Users\Dharmesh raikwar\Desktop\LangchainModels\Chains> python .\simpleChain.py
#       +-------------+      
#       | PromptInput |
#       +-------------+
#              *
#              *
#              *
#     +----------------+
#     | PromptTemplate |
#     +----------------+
#              *
#              *
#              *
# +------------------------+
# | ChatGoogleGenerativeAI |
# +------------------------+
#              *
#              *
#              *
#     +-----------------+
#     | StrOutputParser |
#     +-----------------+
#              *
#              *
#              *
# +-----------------------+
# | StrOutputParserOutput |
# +-----------------------+
# (venv) PS C:\Users\Dharmesh raikwar\Desktop\LangchainModels\Chains> python .\simpleChain.py
# Final Result: There's no celestial object officially or commonly known as "Nebula Star."  Nebulae are vast clouds of gas and dust, and stars are formed *within* them, not the other way around.  Perhaps you're thinking of a specific nebula or star with a similar name?  However, I can offer 5 interesting and lesser-known facts about *nebulae* and *star formation*:

# 1. **Some nebulae are powered by dying stars:**  Planetary nebulae, despite their name, aren't related to planets. They're formed when a sun-like star sheds its outer layers at the end of its life, energized by the exposed hot core.

# 2. **Bok globules are stellar nurseries in disguise:** These dark, dense clouds appear as voids in the sky, but are actually rich in gas and dust, collapsing under their own gravity to form stars.

# 3. **Herbig-Haro objects are supersonic jets:** These bright, fleeting knots of gas are formed by newborn stars violently ejecting material, often showing complex interactions with surrounding nebulae.

# 4. **Nebulae can influence the composition of newly formed stars:** The chemical makeup of a nebula directly impacts the elements present in the stars born within it.  This affects the star's eventual evolution and potential for planetary systems.

# 5. **Some nebulae are remnants of supernova explosions:**  Supernova remnants, like the Crab Nebula, are expanding clouds of debris left behind after a massive star's explosive death, showcasing the powerful forces at play in the universe.
# (venv) PS C:\Users\Dharmesh raikwar\Desktop\LangchainModels\Chains> 