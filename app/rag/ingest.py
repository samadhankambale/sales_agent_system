from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from app.core.config import QDRANT_URL, COLLECTION_NAME

client = QdrantClient(url=QDRANT_URL)

def create_collection():
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)
    )

def insert_products():
    products = [
        {
            "id": 1,
            "name": "AI CRM Pro",
            "description": "Advanced CRM with automation and analytics for sales teams"
        },
        {
            "id": 2,
            "name": "Sales Automation Suite",
            "description": "Automates lead tracking, follow-ups, and conversions"
        },
        {
            "id": 3,
            "name": "Customer Insights Platform",
            "description": "Provides deep analytics on customer behavior and segmentation"
        }
    ]

    points = []
    for p in products:
        points.append(
            PointStruct(
                id=p["id"],
                vector=[0.2]*384,  
                payload={
                    "name": p["name"],
                    "description": p["description"],
                    "text": f"{p['name']} - {p['description']}"
                }
            )
        )

    client.upsert(collection_name=COLLECTION_NAME, points=points)


if __name__ == "__main__":
    create_collection()
    insert_products()
