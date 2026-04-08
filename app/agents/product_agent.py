from app.core.llm import client, MODEL
from app.rag.retriever import retrieve_products

def product_agent(state):
    products = retrieve_products(state["input"], limit=5)

    SYSTEM_PROMPT = f"""
    You are an expert Product Recommendation AI.

    Your job is to recommend the most relevant products based on customer intent.

    AVAILABLE PRODUCTS:
    {products}

    CONSTRAINTS:
    - Use only the provided products
    - Do NOT invent products
    - Do NOT show IDs

    OBJECTIVES:
    - Understand user intent
    - Recommend appropriate number of products:
        • 1–2 if user wants recommendation
        • multiple if user is exploring
    - Mention product names naturally

    RESPONSE STYLE:
    - Natural, persuasive, and concise
    - Focus on value and relevance
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": state["input"]},
        ],
    )

    state["response"] = response.choices[0].message.content
    return state