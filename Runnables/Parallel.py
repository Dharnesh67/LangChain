from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()


prompt1 = PromptTemplate(
    input_variables=["input"], template="Write a tweet content on the topic: {input}?"
)

prompt2 = PromptTemplate(
    input_variables=["input"],
    template="Write some Reply comments Tweets about {input}?",
)


model = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet_content": RunnableSequence(prompt1, model, parser),
        "reply_comments": RunnableSequence(prompt2, model, parser),
    }
)


result = parallel_chain.invoke("Elon Musk")

print(result)  # Output: A tweet content and reply comments about Elon Musk




# (venv) PS C:\Users\Dharmesh raikwar\Desktop\LangchainModels\Runnables> python .\Parallel.py
# {'tweet_content': "Here are a few options for a tweet about Elon Musk, playing on different angles:\n\n**Option 1 (Neutral/Impact-focused):**\nElon Musk: The name synonymous with pushing the limits of technology, space, and social media. What's the first thing that comes to mind when you hear his name? #ElonMusk #TechVisionary #SpaceX #Tesla #X\n\n**Option 2 (Engaging/Polarizing):**\nLove him or... well, you know. @elonmusk always sparks conversation. Visionary disruptor or chaotic provocateur? What's your take? 👇 #ElonMusk #Tech #Debate #X\n\n**Option 3 (Future-focused/Humorous):**\nJust when you think you've got @elonmusk figured out, he launches something new (or buys something old). Never a dull moment! What's your prediction for his next big move? 🚀 #ElonMusk #FutureTech #Innovation #Unpredictable\n\n**Option 4 (Concise/Broad):**\nElon Musk: From electric cars to Mars ambitions. A constant force in tech news. #ElonMusk #Tesla #SpaceX #X #Innovation\n\nChoose the one that best fits the tone you're going for!",
# 
# 
# 
# 'reply_comments': 'Okay, here are some reply comments you could use on Twitter about Elon Musk, ranging from supportive to critical to humorous. Choose the one that best fits the context of the tweet you\'re replying to!\n\n---\n\n**Supportive/Positive:**\n\n1.  **"Say what you will, the man is genuinely pushing humanity forward. #SpaceX #Innovation"**\n2.  **"Another day, another step closer to Mars. Can\'t wait to see what he does next with Starship! 🚀"**\n3.  **"He\'s definitely shaking things up, and sometimes that\'s exactly what\'s needed. Love the ambition!"**\n4.  **"Unpopular opinion: X is actually way more interesting since Elon took over. Chaos creates content! 😂"**\n5.  **"The vision for Tesla and AI is incredible. People don\'t always see the long game."**\n\n---\n\n**Critical/Skeptical:**\n\n6.  **"Still waiting for that full self-driving, Elon. My car\'s getting old! 😅 #FSD"**\n7.  **"Another poll? Is this how we\'re running a multi-billion dollar company now? 🤔"**\n8.  **"It\'s wild how much X has changed since he bought it. Not always for the better, IMO."**\n9.  **"Remember when this app actually worked? Good times. #XFail"**\n10. **"Promises vs. delivery. Always an interesting balance with Elon."**\n\n---\n\n**Humorous/Sarcastic:**\n\n11. **"Someone get this man a nap. Or maybe a new social media manager. 😴"**\n12. **"Is this a serious tweet or is Elon just stress-testing the internet again? Can\'t tell anymore. 😂"**\n13. **"Just when you think he can\'t surprise you... he does. Again. What\'s the over/under on the next big announcement?"**\n14. **"My brain cells are struggling to keep up with the latest Elon saga."**\n15. **"Plot twist: This whole account is actually run by Grok."**\n\n---\n\n**Concerned/Observational:**\n\n16. **"Seriously, is he okay? The late-night tweets are getting a bit much. #Concerned"**\n17. **"Never a dull moment when Elon\'s tweeting. That\'s for sure."**\n18. **"It\'s fascinating to watch, whether you agree with him or not."**\n19. **"He really lives rent-free in a lot of people\'s heads."**\n20. **"The duality of man, encapsulated in one Twitter account."**\n\n---\n\nRemember to always consider the original tweet\'s tone and context before replying!'}
# (venv) PS C:\Users\Dharmesh raikwar\Desktop\LangchainModels\Runnables> 