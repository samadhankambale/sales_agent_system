from openai import OpenAI
from app.core.llm import get_model, get_openai_config
from app.rag.retriever import retrieve_products

config = get_openai_config()
client = OpenAI(**config)
MODEL = get_model("objection")


def objection_agent(state):
    print("running the objection agent")
    products = retrieve_products(state["input"], limit=5)

    SYSTEM_PROMPT = f"""
    You are an expert Sales Objection Handling AI.

    AVAILABLE PRODUCTS:
    {products}

    CONSTRAINTS:
    - Do not ignore objections
    - Do not be defensive
    - Do not invent product features

    OBJECTIVES:
    - Understand the concern
    - Address it clearly
    - Reinforce product value
    - Build trust

    RESPONSE STYLE:
    - Empathetic and confident
    - Natural and human-like
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