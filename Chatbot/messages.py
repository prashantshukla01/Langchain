from langchain_core.messages import SystemMessage , HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
# learn about system , human and ai messages in langchain
# this is done so that we can distinguish between different types 
# of messages in the chat history

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content = " tell me about langchain?")
    
]
results = model.invoke(messages)
messages.append(AIMessage(content=results.content))

print(messages)