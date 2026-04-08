from langgraph.graph import StateGraph
from app.core.llm import generate_response
from app.agents.lead_agent import lead_agent
from app.agents.product_agent import product_agent
from app.agents.objection_agent import objection_agent
from app.agents.closing_agent import closing_agent


def detect_intent(user_input: str):
    prompt = f"""
    You are an expert intent classifier for a sales AI system.

    Classify the user's intent into ONE of the following categories:

    - lead → user is exploring, asking general questions, or giving background
    - product → user wants to see, list, or get product recommendations
    - objection → user expresses doubt, concern, pricing issues, or hesitation
    - closing → user shows buying intent or wants to proceed

    Guidelines:
    - Use semantic understanding, not keywords
    - Be strict in classification
    - Output ONLY one word from: lead, product, objection, closing

    User Input:
    {user_input}
    """
    return generate_response(prompt).strip().lower()


def intent_node(state):
   
    user_input = state.get("input", "")
    intent = detect_intent(user_input)
    return {"intent": intent, "input": user_input}


def lead_node(state):
    return {"response": lead_agent(state.get("input", ""))}


def product_node(state):
    return {"response": product_agent(state.get("input", ""))}


def objection_node(state):
    return {"response": objection_agent(state.get("input", ""))}


def closing_node(state):
    return {"response": closing_agent(state.get("input", ""))}


graph = StateGraph(dict)

graph.add_node("intent", intent_node)
graph.add_node("lead", lead_node)
graph.add_node("product", product_node)
graph.add_node("objection", objection_node)
graph.add_node("closing", closing_node)

graph.set_entry_point("intent")


def route_intent(state):
    return state.get("intent", "product")  

graph.add_conditional_edges(
    "intent",
    route_intent,
    {
        "lead": "lead",
        "product": "product",
        "objection": "objection",
        "closing": "closing",
    }
)

graph.set_finish_point("lead")
graph.set_finish_point("product")
graph.set_finish_point("objection")
graph.set_finish_point("closing")

compiled_graph = graph.compile()


def run_graph(user_input: str):
    
    result = compiled_graph.invoke({"input": user_input})
    return result.get("response", "")