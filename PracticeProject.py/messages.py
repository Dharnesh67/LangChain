from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

messages=[

    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about Langchain messages and how to use them."),
    ]

result=model.invoke(messages)

print(f"Chatbot: {result.content}")

aimessage=AIMessage(content=result.content)

messages.append(aimessage)

print(messages)






# PS C:\Users\Dharmesh raikwar\Desktop\LangchainModels\PracticeProject.py> python .\messages.py
# Chatbot: Langchain's `Message` objects are fundamental for managing conversational interactions with language models. They represent a single turn in a conversation, containing both the role (e.g., "system," "user," "AI") and the content of the message.  This structured approach is crucial for several reasons:

# * **Contextual Understanding:**  By explicitly defining the role of each message, Langchain enables the LLM to understand the conversation's flow and the relationship between different turns. This is particularly important for complex dialogues or when incorporating external knowledge.

# * **Chain Management:**  Messages are the building blocks of Langchain chains.  Chains like `ConversationChain` and `ConversationBufferMemory` rely on lists of `Message` objects to track the conversation history and pass it to the LLM.

# * **Memory and State:**  The sequence of `Message` objects maintains the conversational state. This allows the LLM to access and consider previous turns when generating a response, making the conversation more coherent and contextually aware.

# * **Flexibility and Extensibility:**  The `Message` class is designed to be versatile. You can easily add custom metadata or attributes to messages as needed, extending their functionality beyond basic role and content.

# **How to Use Langchain Messages:**

# 1. **Import the necessary class:**

# ```python
# from langchain.schema import Message
# ```

# 2. **Create Message objects:**  You create a `Message` object by specifying its `role` and `content`.

# ```python
# user_message = Message(role="user", content="What is the capital of France?")
# ai_message = Message(role="assistant", content="The capital of France is Paris.")
# system_message = Message(role="system", content="You are a helpful assistant.")
# ```

# 3. **Use Messages in Chains:**  Langchain chains typically take a list of `Message` objects as input.  This list represents the conversation history.  Here's an example with `ConversationChain`:

# ```python
# from langchain.chains import ConversationChain
# from langchain.llms import OpenAI

# # Replace with your OpenAI API key
# llm = OpenAI(temperature=0)

# conversation = ConversationChain(llm=llm)

# messages = [system_message, user_message] #adding system message for context

# response = conversation.predict(input=messages)
# print(response) # This will print the AI's response.

# # Add the AI's response to the message history:
# messages.append(Message(role="assistant", content=response))
# print(messages) # Show the updated conversation history.

# #Continue the conversation
# next_user_message = Message(role="user", content="And what's its population?")
# response2 = conversation.predict(input=messages + [next_user_message])
# print(response2)
# ```

# 4. **Using `ConversationBufferMemory`:**  This memory type efficiently manages the conversation history.

# ```python
# from langchain.memory import ConversationBufferMemory

# memory = ConversationBufferMemory()
# conversation = ConversationChain(llm=llm, memory=memory)

# response = conversation.predict(input="What is the capital of France?")
# print(response)

# response2 = conversation.predict(input="And what's its population?")
# print(response2) # This response will consider the previous turn.
# ```


# **Key Considerations:**

# * **System Messages:** System messages are crucial for setting the tone and behavior of the LLM. They provide instructions or context that influence the AI's responses.

# * **Message Order:** The order of messages in the list is critical; it dictates the conversational flow.

# * **Error Handling:**  Always handle potential exceptions (e.g., API errors) when interacting with LLMs.

# * **Large Conversations:** For very long conversations, consider strategies for managing memory efficiently to avoid exceeding LLM token limits.


# By understanding and effectively using Langchain's `Message` objects, you can build robust and contextually aware conversational applications powered by LLMs.  Remember to adapt the code examples to your specific LLM and application requirements.  You'll need to install the necessary packages (`pip install langchain openai`).  Also, remember to set your OpenAI API key.
# [SystemMessage(content='You are a helpful assistant.', additional_kwargs={}, response_metadata={}), HumanMessage(content='Tell me about Langchain messages and how to use them.', additional_kwargs={}, response_metadata={}), AIMessage(content='Langchain\'s `Message` objects are fundamental for managing conversational interactions with language models. They represent a single turn in a conversation, containing both the role (e.g., "system," "user," "AI") and the content of the message.  This structured approach is crucial for several reasons:\n\n* **Contextual Understanding:**  By explicitly defining the role of each message, Langchain enables the LLM to understand the conversation\'s flow and the relationship between different turns. This is particularly important for complex dialogues or when incorporating external knowledge.\n\n* **Chain Management:**  Messages are the building blocks of Langchain chains.  Chains like `ConversationChain` and `ConversationBufferMemory` rely on lists of `Message` objects to track the conversation history and pass it to the LLM.\n\n* **Memory and State:**  The sequence of `Message` objects maintains the conversational state. This allows the LLM to access and consider previous turns when generating a response, making the conversation more coherent and contextually aware.\n\n* **Flexibility and Extensibility:**  The `Message` class is designed to be versatile. You can easily add custom metadata or attributes to messages as needed, extending their functionality beyond basic role and content.\n\n**How to Use Langchain Messages:**\n\n1. **Import the necessary class:**\n\n```python\nfrom langchain.schema import Message\n```\n\n2. **Create Message objects:**  You create a `Message` object by specifying its `role` and `content`.\n\n```python\nuser_message = Message(role="user", content="What is the capital of France?")\nai_message = Message(role="assistant", content="The capital of France is Paris.")\nsystem_message = Message(role="system", content="You are a helpful assistant.")\n```\n\n3. **Use Messages in Chains:**  Langchain chains typically take a list of `Message` objects as input.  This list represents the conversation history.  Here\'s an example with `ConversationChain`:\n\n```python\nfrom langchain.chains import ConversationChain\nfrom langchain.llms import OpenAI\n\n# Replace with your OpenAI API key\nllm = OpenAI(temperature=0)\n\nconversation = ConversationChain(llm=llm)\n\nmessages = [system_message, user_message] #adding system message for context\n\nresponse = conversation.predict(input=messages)\nprint(response) # This will print the AI\'s response.\n\n# Add the AI\'s response to the message history:\nmessages.append(Message(role="assistant", content=response))\nprint(messages) # Show the updated conversation history.\n\n#Continue the conversation\nnext_user_message = Message(role="user", content="And what\'s its population?")\nresponse2 = conversation.predict(input=messages + [next_user_message])\nprint(response2)\n```\n\n4. **Using `ConversationBufferMemory`:**  This memory type efficiently manages the conversation history.\n\n```python\nfrom langchain.memory import ConversationBufferMemory\n\nmemory = ConversationBufferMemory()\nconversation = ConversationChain(llm=llm, memory=memory)\n\nresponse = conversation.predict(input="What is the capital of France?")\nprint(response)\n\nresponse2 = conversation.predict(input="And what\'s its population?")\nprint(response2) # This response will consider the previous turn.\n```\n\n\n**Key Considerations:**\n\n* **System Messages:** System messages are crucial for setting the tone and behavior of the LLM. They provide instructions or context that influence the AI\'s responses.\n\n* **Message Order:** The order of messages in the list is critical; it dictates the conversational flow.\n\n* **Error Handling:**  Always handle potential exceptions (e.g., API errors) when interacting with LLMs.\n\n* **Large Conversations:** For very long conversations, consider strategies for managing memory efficiently to avoid exceeding LLM token limits.\n\n\nBy understanding and effectively using Langchain\'s `Message` objects, you can build robust and contextually aware conversational applications powered by LLMs.  Remember to adapt the code examples to your specific LLM and application requirements.  You\'ll need to install the necessary packages (`pip install langchain openai`).  Also, remember to set your OpenAI API key.', additional_kwargs={}, response_metadata={})]