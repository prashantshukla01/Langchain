from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    task="text2text-generation",
    max_new_tokens=512,
    temperature=0.7
)
model = ChatHuggingFace(llm = llm)

class Person(BaseModel):
    name: str = Field(..., description="The name of the person")
    age: int = Field(..., description="The age of the person in years")
    city: str = Field(..., description="The city of the person")
    
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template= 'Generate the name, age, and city of a fictional {place} person \n {format_instruction}',
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
    
)
prompt = template.invoke({'place':'Indian'})
result =model.invoke(prompt)
final_result = parser.parse(result)

print("Final Result:\n", final_result)