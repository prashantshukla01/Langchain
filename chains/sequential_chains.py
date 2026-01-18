from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1 = PromptTemplate(
    template= "Generate a detailed report on the topic: {topic}",
    input_variables= ['topic']
    
)
prompt2 = PromptTemplate(
    template= "Summarize the following report:\n{report}",
    input_variables= ['report']
)

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'Space Exploration'})
print("Final Summary:\n", result)
