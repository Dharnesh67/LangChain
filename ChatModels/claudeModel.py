from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chatAnthropicModel = ChatAnthropic(
    model='claude-3-5-sonnet-20240229',
    temperature=0.7,
    max_tokens=1000,    
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    )

result = chatAnthropicModel.invoke("What is the capital of France?")

print(result.content)
