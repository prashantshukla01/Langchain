from langchain_experimental.text_splitter import SemanticChunker  # type: ignore
from langchain_openai.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()       


text_splitter = SemanticChunker(
    OpenAIEmbeddings(),breakpoint_threshold_type = "standard deviation",
    breakpoint_threshold_ampunt = 1.0,
    chunk_size=100,
)
sample = """LangChain is a framework for developing applications powered by 
language models. It can be used for chatbots, Generative Question-Answering (GQA), 
summarization, and much more.
"""

docs = text_splitter.create_documents([sample])
print(docs)