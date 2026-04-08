from openai import OpenAI
from app.core.llm import get_model, get_openai_config
from app.rag.retriever import retrieve_products

config = get_openai_config()
client = OpenAI(**config)
MODEL = get_model("product")


def product_agent(state):
    print("running the product agent")
    products = retrieve_products(state["input"], limit=5)

    SYSTEM_PROMPT = f"""
    You are an expert Product Recommendation AI.

    AVAILABLE PRODUCTS:
    {products}

    CONSTRAINTS:
    - Use only provided products
    - Do not invent products
    - Do not show IDs

    OBJECTIVES:
    - Understand user intent
    - Recommend relevant products
    - Adjust number of products based on intent

    RESPONSE STYLE:
    - Natural and persuasive
    - Mention product names clearly
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