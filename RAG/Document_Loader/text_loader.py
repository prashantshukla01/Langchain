# Updated import path
from langchain_community.document_loaders import TextLoader 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

prompt = PromptTemplate(
    template = "Write a summary of the following poem - \n {poem}",
    input_variables = ["poem"]
)
parser = StrOutputParser()


# Initialize and load
loader = TextLoader("cricket.txt", encoding="utf-8")
docs = loader.load()

print(docs)

chain = prompt | model | parser

print(chain.invoke({"poem": docs[0].page_content}))