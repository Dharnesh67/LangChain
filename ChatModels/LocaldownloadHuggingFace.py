from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Llama-2-7b-chat-hf",
    task="text-generation",
    model_kwargs={
        # model key word arguments 
        "temperature": 0.1,
        "max_length": 512,
        "top_p": 0.95,
        "repetition_penalty": 1.2,
    },
)


ChatModel = ChatHuggingFace(llm=llm)

x = input("Enter your question: ")
result = ChatModel.invoke(x)
print(result.content)