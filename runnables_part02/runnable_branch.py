from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough , RunnableParallel ,RunnableBranch, RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report about {topic}?",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Summarize the following report in bullet points:\n{text}",
    input_variables=["text"],
)

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1 , model , parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model , parser)),  # Just passes the input through without changes
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain , branch_chain)

print(final_chain.invoke({"topic":'Russia vs Ukraine war'}))