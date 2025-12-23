from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(model= 'text-embedding-3-large', dimensions=300)
documents = [
    "Virat Kohli is a famous Indian cricketer.",
    "Sachin Tendulkar is known as the God of Cricket.",
    "The capital of India is New Delhi.",
    "The Eiffel Tower is located in Paris.",
    "Rohit Sharma is another prominent Indian cricketer.",
    "Jasprit Bumrah is a leading fast bowler from India."
]

query = " Tell me about Virat Kohli"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding] , doc_embeddings)[0]

index , score=sorted(list(enumerate(scores)),key = lambda x:x[1])[-1]

print("Query: ", query)
print(documents[index])
print("Score: ", score)


