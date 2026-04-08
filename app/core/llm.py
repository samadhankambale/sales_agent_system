import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_model(agent_name: str) -> str:
    """
    Returns model for a specific agent.
    Falls back to DEFAULT_MODEL.
    """
    return (
        os.getenv(f"{agent_name.upper()}_MODEL")
        or os.getenv("DEFAULT_MODEL", "usf1-mini")
    )

def get_openai_config():
    """
    Returns shared OpenAI configuration.
    """
    return {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "base_url": os.getenv("OPENAI_BASE_URL"),
    }


config = get_openai_config()
client = OpenAI(**config)

def generate_response(prompt: str, model: str = None) -> str:
    """
    Generates a response from OpenAI given a prompt.
    """
    model = model or get_model("default")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
