from app.graph.flow import run_graph

def process_query(user_input: str):
    state = {"input": user_input}
    result = run_graph(state)
    return result["response"]