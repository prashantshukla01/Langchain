from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document

text = """LangChain is a framework for developing applications powered by 
language models. It can be used for chatbots, Generative Question-Answering (GQA), 
summarization, and much more.
"""

docs = [Document(page_content=text)]

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator="\n"
)

result = splitter.split_documents(docs)

print(result)
