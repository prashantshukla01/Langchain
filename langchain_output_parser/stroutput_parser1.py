from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    task="text2text-generation",
    max_new_tokens=512,
    temperature=0.7
)
model = ChatHuggingFace(llm = llm)

#1 prompt --> detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

#2 prompt --> summary of the report
template2 = PromptTemplate(
    template="Summarize the following report:\n{report}",
    input_variables=["report"]
)
  
parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Blackhole'})
print("Final Summary:\n", result)