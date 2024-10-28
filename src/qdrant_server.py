import qdrant_client
from qdrant_client.models import Distance, VectorParams
from qdrant_client import QdrantClient
#client = QdrantClient("http://localhost:4444") # Connect to existing Qdrant instance
client = QdrantClient("http://qdrant:6333")  # Connect to the Qdrant service within Docker

collection_name = "paul_graham"
# vector_store = QdrantVectorStore(
#     client=client,
#     collection_name=collection_name,
# )
client.delete_collection(collection_name=collection_name)
client.create_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=100, distance=Distance.COSINE),
)




# Prepare your documents, metadata, and IDs
docs = ["Qdrant has Langchain integrations", "Qdrant also has Llama Index integrations"]
metadata = [
    {"source": "Langchain-docs"},
    {"source": "Linkedin-docs"},
]
ids = [42, 2]

# Use the new add method
client.add(
    collection_name="demo_collection",
    documents=docs,
    metadata=metadata,
    ids=ids
)

search_result = client.query(
    collection_name="demo_collection",
    query_text="This is a query document"
)
print(search_result)