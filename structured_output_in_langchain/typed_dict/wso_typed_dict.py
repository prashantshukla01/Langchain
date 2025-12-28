from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict #to define the dictionary type

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0)
#schema

class Review(TypedDict):
    summary:str
    sentiment:str
    
    
structured_model = model.with_structured_output(Review)



result = model.invoke("""the hardware is great but the software feels bloated.
             There are to many preinstalled apps that i cant remove""")

print(result)
print(result['summary'])