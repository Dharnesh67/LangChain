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
    template="Print the report and give 5 Pointer summary on the report : {input}",
)

# prompt2 = template2.invoke({"input": result.content})


# result2 = llm.invoke(prompt2)

# print("result2:", result2)


parser = StrOutputParser()


chain = template1 | llm | parser | template2 | llm | parser


result =chain.invoke({"input": "BlackHole"})


print("Final Result:", result)



# Final Result: Here's a printed version of the report, followed by a 5-pointer summary:


## Black Hole Report: A Comprehensive Overview

# **1. Introduction:**

# Black holes are regions of spacetime exhibiting such strong gravitational effects that nothing—not even particles and electromagnetic radiation such as light—can escape from inside them. This report will explore the formation, properties, types, detection methods, and ongoing research surrounding these fascinating and enigmatic celestial objects.

# **2. Formation:**

# Black holes typically form from the gravitational collapse of massive stars at the end of their life cycle. When a star with a mass significantly greater than our Sun exhausts its nuclear fuel, it can no longer support itself against its own gravity. This leads to a catastrophic inward collapse, resulting in a singularity—a point of infinite density—at the center. The surrounding matter is compressed into an incredibly small volume, creating a region of intense gravity.

# Less massive stars follow a different path, ending their lives as white dwarfs or neutron stars. Supermassive black holes, found at the centers of most galaxies, are believed to form through different mechanisms, possibly involving the merger of smaller black holes or the indirect collapse of massive gas clouds.

# **3. Properties:**

# Key properties of black holes include:

# * **Singularity:** The point of infinite density at the center.
# * **Event Horizon:** The boundary beyond which nothing can escape. This is defined by the Schwarzschild radius, which depends on the black hole's mass.
# * **Accretion Disk:** A swirling disk of superheated matter orbiting the black hole before being consumed. Friction within this disk generates intense radiation, making it detectable.       
# * **Mass:** Black holes can range in mass from a few solar masses (stellar-mass black holes) to billions of solar masses (supermassive black holes).
# * **Spin (Angular Momentum):** Most black holes are believed to possess significant spin.      
# * **Charge:** While theoretically possible, the charge of black holes is expected to be negligible in practice.

# **4. Types:**

# Several types of black holes are recognized:

# * **Stellar-mass Black Holes:** Formed from the collapse of massive stars.
# * **Intermediate-mass Black Holes:** A relatively less understood category, with masses between stellar-mass and supermassive black holes.
# * **Supermassive Black Holes:** Found at the centers of most galaxies, with masses millions or billions of times that of the Sun.
# * **Primordial Black Holes:** Hypothetical black holes formed in the early universe.

# **5. Detection Methods:**

# Directly observing a black hole is impossible, as light cannot escape its event horizon. However, their presence can be inferred through their effects on surrounding matter:

# * **Gravitational Effects:** Observing the motion of stars and gas orbiting an unseen object can reveal the presence of a black hole.
# * **X-ray Emission:** Accretion disks around black holes emit intense X-rays, which can be detected by telescopes.
# * **Gravitational Waves:** The merger of two black holes produces ripples in spacetime, known as gravitational waves, which can be detected by observatories like LIGO and Virgo.
# * **Shadow Imaging:** The Event Horizon Telescope (EHT) has successfully imaged the shadow of a supermassive black hole, providing direct visual evidence.

# **6. Ongoing Research:**

# Current research on black holes focuses on:

# * **Understanding the formation and evolution of supermassive black holes.**
# * **Exploring the physics of the singularity and the event horizon.**
# * **Investigating the role of black holes in galaxy formation and evolution.**
# * **Developing more advanced techniques for detecting and characterizing black holes.**        
# * **Testing theories of gravity in extreme environments.**

# **7. Conclusion:**

# Black holes are among the most fascinating and mysterious objects in the universe. While many aspects remain unknown, ongoing research using advanced observational techniques and theoretical models is continually expanding our understanding of these enigmatic celestial bodies and their profound impact on the cosmos. Further study will undoubtedly reveal even more about their nature and their crucial role in the universe's structure and evolution.


# **5-Pointer Summary:**

# 1. **Formation:** Black holes form from the gravitational collapse of massive stars or through other mechanisms like the merger of smaller black holes, resulting in a singularity of infinite density.

# 2. **Key Properties:** Defined by their singularity, event horizon (point of no return), accretion disk (emitting intense radiation), mass (varying greatly), spin, and negligible charge.    

# 3. **Types:**  Categorized into stellar-mass, intermediate-mass, supermassive, and hypothetical primordial black holes.

# 4. **Detection:**  Detected indirectly through gravitational effects on surrounding matter, X-ray emissions from accretion disks, gravitational waves from mergers, and recently, through direct shadow imaging.

# 5. **Ongoing Research:**  Focuses on understanding their formation, exploring the physics of singularities and event horizons, their role in galaxy evolution, developing better detection methods, and testing gravity theories in extreme conditions.
# (venv) PS C:\Users\Dharmesh raikwar\Desktop\LangchainModels\Output_Parsers> 