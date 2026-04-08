from openai import OpenAI
from app.core.llm import get_model, get_openai_config

config = get_openai_config()
client = OpenAI(**config)
MODEL = get_model("lead")


def lead_agent(state):
    print("running lead agent")
    SYSTEM_PROMPT = """
    You are an expert Sales Lead Qualification AI.

    Your role is to understand and qualify the customer.

    CONSTRAINTS:
    - Do not recommend products yet
    - Do not assume missing details

    OBJECTIVES:
    - Identify customer needs
    - Detect budget signals
    - Understand urgency and intent
    - Ask clarifying questions if needed

    RESPONSE STYLE:
    - Natural and professional
    - Concise and engaging
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