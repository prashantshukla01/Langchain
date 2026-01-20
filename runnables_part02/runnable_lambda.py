from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence , RunnableLambda , RunnableParallel , RunnablePassthrough 

load_dotenv()

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template="Write a joke about {topic}?",
    input_variables=["topic"],
)
model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1 , model , parser)



parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),  # Generates a joke
    "word_count": RunnableLambda( word_count),  # Counts the number of words in the joke       
})

final_chain = RunnableSequence(joke_gen_chain , parallel_chain)

result = final_chain.invoke({"topic": "artificial intelligence"})
print(result)