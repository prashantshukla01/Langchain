from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough , RunnableParallel , RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}?",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}?",
    input_variables=["topic"],
)

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
parser = StrOutputParser()  

joke_gen_chain = RunnableSequence(prompt1 , model , parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),  # Just passes the input through without changes
    "explanation": RunnableSequence(prompt2 , model , parser),  # Just passes the input through without changes
}) 
final_chain = RunnableSequence(joke_gen_chain , parallel_chain)

result = final_chain.invoke({"topic": "artificial intelligence"})
print(result)
