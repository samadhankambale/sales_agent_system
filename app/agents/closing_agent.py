from app.core.llm import client, MODEL

def closing_agent(state):
    SYSTEM_PROMPT = """
    You are an expert Sales Closing AI.

    Your goal is to guide the customer toward completing the purchase.

    CONSTRAINTS:
    - Do not pressure the customer aggressively
    - Do not introduce new products unnecessarily

    OBJECTIVES:
    - Detect buying intent
    - Reinforce confidence
    - Suggest next steps (purchase, demo, onboarding)

    RESPONSE STYLE:
    - Confident and persuasive
    - Clear and action-oriented
    - Natural and professional
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