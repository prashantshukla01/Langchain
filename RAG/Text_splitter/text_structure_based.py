from langchain_text_splitters import RecursiveCharacterTextSplitter

text= """
LangChain is a framework for developing applications powered by 
language models. It can be used for chatbots, Generative Question-Answering (GQA), 
summarization, and much more.
"""

#initialise the text splitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(chunks)