from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional #to define the dictionary type

load_dotenv()

model = ChatOpenAI(model_name="gpt-4", temperature=0)
#schema

class Review(TypedDict):
    key_themes:Annotated[str, "Write down all the key themes of the review"]
    summary:Annotated[str, "The summary of the review"]
    sentiment:Annotated[str, "The sentiment of the review either negative positive or neutral"]
    pros:Annotated[Optional[list[str]], "The pros of the review"]
    cons:Annotated[Optional[list[str]], "The cons of the review"]
    
structured_model = model.with_structured_output(Review)



result = model.invoke("""the hardware is great but the software feels bloated.
             There are to many preinstalled apps that i cant remove""")

print(result)
print(result['summary'])