import os
from sentence_transformers import SentenceTransformer
from app.core.config import EMBEDDING_MODEL  


model_name = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
embed_model = SentenceTransformer(model_name)

def get_embedding(text: str) -> list[float]:
    """
    Generate a semantic embedding vector for the given text.

    Args:
        text (str): Input text to embed.

    Returns:
        list[float]: Embedding vector.
    """
    vector = embed_model.encode(text, convert_to_numpy=True)
    return vector.tolist()