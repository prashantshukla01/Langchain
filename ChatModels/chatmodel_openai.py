# sare chatmodels BaseChatModel class ko inherit krte h

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4', temperature=0.7,max_completion_tokens=50)
## temperature --> randomness ko control krta h, it affect how creative and deterministic responses are there
## value of temperature 0 se 2 ke beech hota h, jaha 0 means deterministic responses and 2 means more creative responses
result = model.invoke(" what is the capital of India?")

# print(result)    this include keyword arguments(kwargs) like temperature, max_tokens etc.

print(result.content)
