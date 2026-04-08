from app.rag.qdrant_client import client
from app.core.config import COLLECTION_NAME
from app.rag.embeddings import get_embedding  

def retrieve_products(query: str, limit: int = 5) -> str:
    query_vector = get_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=limit
    )

    products = []
    for point in results.points:
        payload = point.payload
        products.append(f"{payload.get('name')} - {payload.get('description')}")

    return "\n".join(products)

