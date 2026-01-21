from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_openai import ChatOpenAI

loader = DirectoryLoader(
    path = "data/",
    glob = "*.pdf",
    loader_cls =PyPDFLoader,
)

docs = loader.load()

print(len(docs))
