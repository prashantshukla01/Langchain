from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    
)
model = ChatHuggingFace(llm = llm)

#1 prompt --> detailed report
template1 = PromptTemplate(
    template = "Write a detailed report on the {topic}",
    input_variable = ["topic"]
    
)
#2 prompt --> summary of the report
template2 = PromptTemplate(
    template = "Summarize the following report: {report}",
    input_variable = ["report"]   
)   
parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Blackhole'})
print("Final Summary:\n", result)