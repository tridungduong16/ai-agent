from qdrant_client import QdrantClient
import pandas as pd
import pdb
from tqdm import tqdm 
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

load_dotenv()
QDRANT_SERVER = os.getenv("QDRANT_SERVER")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
client = QdrantClient(QDRANT_SERVER)
coll_name="demo_collection"
client.delete_collection(collection_name=COLLECTION_NAME)
client.create_collection(collection_name=COLLECTION_NAME, vectors_config=VectorParams(size=768, distance=Distance.COSINE))

