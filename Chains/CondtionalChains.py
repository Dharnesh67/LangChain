from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain.schema.runnable import RunnableBranch

load_dotenv()

# Define a Pydantic model for structured output
class FeedbackClassification(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"] = Field(
        description="The sentiment of the feedback"
    )

# Initialize the model and parser
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
parser = PydanticOutputParser(pydantic_object=FeedbackClassification)

# Define a clear prompt template for sentiment classification
prompt = PromptTemplate(
    input_variables=["feedback"],
    template=(
        "Classify the sentiment (positive, negative, or neutral) of the following feedback:\n"
        '"{feedback}"\n'
        "{format_instructions}\nSentiment:"
    ),
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Build the sentiment classifier chain
classifier_chain = prompt | model | parser

# Visualize the chain graph
classifier_chain.get_graph().print_ascii()

# Example feedback for classification
feedback_text = "The app has several features and works as expected."

# Invoke the chain and print the response
classification = classifier_chain.invoke({"feedback": feedback_text})
print("Sentiment:", classification.sentiment)

# Define prompt templates for generating responses to feedback
positive_prompt = PromptTemplate(
    input_variables=["feedback"],
    template=(
        "Thank the user for their positive feedback and encourage them to continue using the app. "
        "Feedback: \"{feedback}\""
    ),
)
negative_prompt = PromptTemplate(
    input_variables=["feedback"],
    template=(
        "Apologize for the negative experience and assure the user that their feedback will be used to improve the app. "
        "Feedback: \"{feedback}\""
    ),
)
neutral_prompt = PromptTemplate(
    input_variables=["feedback"],
    template=(
        "Thank the user for their feedback and let them know it has been noted. "
        "Feedback: \"{feedback}\""
    ),
)

# Create response chains for each sentiment
positive_chain = positive_prompt | model
negative_chain = negative_prompt | model
neutral_chain = neutral_prompt | model

# Branch chain based on sentiment
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', positive_chain),
    (lambda x: x.sentiment == 'negative', negative_chain),
    (lambda x: x.sentiment == 'neutral', neutral_chain),
)

# Run the full pipeline: classify, then respond
def classify_and_respond(feedback):
    classification = classifier_chain.invoke({"feedback": feedback})
    response = branch_chain.invoke(classification, {"feedback": feedback})
    print("Sentiment:", classification.sentiment)
    print("Response:", response.content if hasattr(response, "content") else response)

# Example usage
if __name__ == "__main__":
    feedback_text = "The app has several features and works as expected."
    classify_and_respond(feedback_text)
