from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}?",
    input_variables=["topic"],
)
model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="explain the joke in simple words:\n{text}",
    input_variables=["text"],
)

chain = RunnableSequence(prompt1 , model , parser, prompt2 , model , parser)

result = chain.invoke({"topic": "computers"})
print("Joke:\n", result)
