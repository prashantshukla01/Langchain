from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core import PromptTemplate
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

prompt1 = template1.invoke({'topic':'Blackhole'})

result = model.invoke(prompt1)

prompt2= template2.invoke({'report':result.content})

result1 = model.invoke(prompt2)
print("Detailed Report:\n", result.content)
print("Summary:\n", result1.content)