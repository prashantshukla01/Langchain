from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt = PromptTemplate(
    template = "generate five interesting facts about this topic:{topic}",
    input_variables= ['topic']
    
)
model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'Space Exploration'})

print("Final Result:\n", result)
