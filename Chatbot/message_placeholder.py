
# message placeholder
# a message placeholder is a special placeholder used in 
# chat prompt templates to dynamically insert messages into the 
# chat history or a list of messages at runtime.

from langchain_core.prompts import MessagesPlaceholder , ChatPromptTemplate 

# chat template
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{query}'),
])
#load chat history
chat_history = []
with open('chat_history.txt', 'r') as f:
    chat_history.extend(f.readlines())
    
    
print(chat_history)
#create pompt

chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund?'})