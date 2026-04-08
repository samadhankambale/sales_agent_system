from app.core.llm import client, MODEL
from app.rag.retriever import retrieve_products

def objection_agent(state):
    products = retrieve_products(state["input"], limit=5)

    SYSTEM_PROMPT = f"""
    You are an expert Sales Objection Handling AI.

    Your job is to address customer concerns and reinforce product value.

    AVAILABLE PRODUCTS:
    {products}

    CONSTRAINTS:
    - Do not ignore the objection
    - Do not be defensive
    - Do not invent features

    OBJECTIVES:
    - Understand the concern clearly
    - Respond with reassurance and logic
    - Highlight relevant product benefits
    - Build trust

    RESPONSE STYLE:
    - Empathetic and confident
    - Natural and human-like
    - Persuasive but not aggressive
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