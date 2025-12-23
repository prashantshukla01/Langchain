from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# sare llms BaseLLM class ko inherit krte h 
llm = OpenAI(model = 'gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India?")
print(result)