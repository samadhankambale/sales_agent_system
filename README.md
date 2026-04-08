# Sales & Customer Acquisition Multi-Agent System

This project implements an **intent-based multi-agent system** for handling sales processes and customer acquisition using FastAPI, LLMs, and Qdrant for RAG (Retrieval-Augmented Generation).

The system is designed to:
- Qualify leads
- Recommend products
- Handle objections
- Close deals
- Perform human handoff 


##  Features

- Intent-based agent routing (no rule-based logic)
- Natural language responses
- Product name visibility (no IDs)
- Qdrant-powered knowledge retrieval
- Graph-based agent coordination
- Hidden human handoff
- No session management
- Clean and scalable architecture


##  Project Structure


sales_agent_system/
│── app/
│ │── main.py
│ │── core/
│ │ │── config.py
│ │ │── llm.py
│ │── agents/
│ │ │── lead_agent.py
│ │ │── product_agent.py
│ │ │── objection_agent.py
│ │ │── closing_agent.py
│ │── graph/
│ │ │── flow.py
│ │── rag/
│ │ │── qdrant_client.py
│ │ │── retriever.py
│ │ │── ingest.py
│ │── models/
│ │ │── request.py
│ │── services/
│ │ │── orchestrator.py
│── .env
│── requirements.txt



##  Environment Setup

Create a `.env` file:


OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://api.your-provider.com/v1

QDRANT_URL=http://localhost:6333



##  Install Dependencies


pip install -r requirements.txt



##  Start Qdrant

Using Docker:


docker run -p 6333:6333 qdrant/qdrant


Qdrant will run at:

http://localhost:6333




##  Data Ingestion

Run the ingestion script to insert products into Qdrant:


python -m app.rag.ingest


This creates a collection and stores products like:
- AI CRM Pro
- Sales Automation Suite
- Customer Insights Platform



##  Run Application


uvicorn app.main:app --reload


API runs at:

http://127.0.0.1:8000



##  API Usage

### Endpoint

POST /chat


### Request Body

{
"message": "show all products"
}


### Response Example

{
"response": "AI CRM Pro, Sales Automation Suite, Customer Insights Platform"
}




##  System Flow


User Input
↓
Intent Detection (LLM)
↓
Orchestrator
↓
Graph Flow
↓
Agent Execution
↓
Final Response




## Agents Overview

### Lead Qualification Agent
- Understands user needs, budget, and intent

### Product Matching Agent
- Retrieves and shows product names
- Shows all products or best match based on intent

### Objection Handling Agent
- Handles pricing, trust, and usability concerns
- Uses contextual persuasion

### Deal Closing Agent
- Detects buying signals
- Guides toward conversion

### Handoff (Intent-Based)
- Triggered when user wants human assistance
- No keyword rules, fully semantic

---

##  End-to-End Test Flow

1. show all products  
→ AI CRM Pro, Sales Automation Suite, Customer Insights Platform  

2. I need a CRM for my sales pipeline  
→ AI CRM Pro  

3. we are a startup  
→ lead qualification response  

4. what do you recommend  
→ AI CRM Pro  

5. this is expensive  
→ objection handled  

6. not sure if it works  
→ objection handled  

7. okay looks good  
→ closing response  

8. I want to buy  
→ deal closing  

9. connect me to human  
→ Our sales specialist will reach out to you shortly  



##  Expected Behavior

- Product names always visible when required
- No product IDs exposed
- No structured/JSON responses (natural language only)
- Intent-based routing (not rule-based)
- Clean and minimal responses for UI
- Handoff handled without exposing logic



##  Common Issues

### Qdrant Not Running
Error:

Connection refused localhost:6333

Solution:

docker run -p 6333:6333 qdrant/qdrant




### No Products Returned
Cause:
- Ingestion not executed

Solution:

python -m app.rag.ingest



## Future Improvements

- Real embeddings for accurate semantic search
- Product ranking system
- Multi-intent detection
- Sentiment-based auto handoff
- UI separation (products vs chat)


