from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer("./models/all-MiniLM-L6-v2")

print("Model loaded!")

emb = model.encode(["hello world"])

print("Embedding shape:", emb.shape)