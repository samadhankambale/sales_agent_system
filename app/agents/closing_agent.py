from openai import OpenAI
from app.core.llm import get_model, get_openai_config

config = get_openai_config()
client = OpenAI(**config)
MODEL = get_model("closing")


def closing_agent(state):
    print("running the closing agent")
    SYSTEM_PROMPT = """
    You are an expert Sales Closing AI.

    Your goal is to guide the customer toward completing the purchase.

    CONSTRAINTS:
    - Do not pressure the customer aggressively
    - Do not introduce new products unnecessarily

    OBJECTIVES:
    - Detect buying intent
    - Reinforce confidence
    - Suggest next steps

    RESPONSE STYLE:
    - Confident and persuasive
    - Clear and action-oriented
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