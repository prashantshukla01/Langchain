from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0)

while True:

    user_input = input('You: ')
    if user_input == 'exit':
        break

    result = model.invoke(user_input)
    
    print('AI:', result.content)
    
