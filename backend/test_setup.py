from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "Python Developer with Machine Learning experience"

embedding = model.encode(text)

print("Embedding dimension:", len(embedding))

index = faiss.IndexFlatL2(len(embedding))
index.add(np.array([embedding]).astype("float32"))

print("FAISS working!")
print("Setup successful!")