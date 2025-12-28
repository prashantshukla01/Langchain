# here we will study how to maintain chat history in a chatbot using langchain
#here we will use dynamic chat history maintenance

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

chat_template = ChatPromptTemplate.from_messages([
    ('system', "You are a helpful {domain} expert."),
    ('human', "Explain in simple term about {topic}.")
])

prompt = chat_template.invoke({
    "domain": "AI",
    "topic": "transformers"
    
})
print(prompt)



