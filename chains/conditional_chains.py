from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import Literal

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableParallel # for parallel chains
from langchain_core.runnables import RunnableBranch # for conditional chains 
from langchain_core.runnables import RunnableLambda # converts the lambda function into a runnable so that can be used in a chain
load_dotenv()

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

parser = StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template='classify the sentiment of the following text as positive or negative \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

classfier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Generate a thank you note for the positive feedback: {feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template='Generate an apology note for the negative feedback: {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Sentiment not recognized.")
)

chain = classfier_chain | branch_chain

chain_result = chain.invoke({'feedback': "The product quality is excellent and I am very satisfied with my purchase."})
print("Final Response:\n", chain_result)