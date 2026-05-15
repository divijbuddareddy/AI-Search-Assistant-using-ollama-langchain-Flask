## Project Architecture
                ┌──────────────────────┐
                │        User          │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Flask Web UI       │
                │ (HTML + Tailwind)    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │    Flask Backend     │
                │      (app.py)        │
                └──────────┬───────────┘
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
┌──────────────────────┐     ┌──────────────────────┐
│ DuckDuckGo Search    │     │      Ollama          │
│   Internet Search    │     │   Local LLM Server   │
└──────────┬───────────┘     └──────────┬───────────┘
           │                            │
           ▼                            ▼
┌──────────────────────┐     ┌──────────────────────┐
│   Search Results     │     │     Phi3 Model       │
│   Context Retrieval  │     │  AI Response Engine  │
└──────────┬───────────┘     └──────────┬───────────┘
           │                            │
           └─────────────┬──────────────┘
                         ▼
              ┌──────────────────────┐
              │   AI Generated       │
              │      Response        │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Response Display   │
              │      in Browser      │
              └──────────────────────┘
```

The application begins when the user enters a query through the Flask-based web interface. The request is sent to the Flask backend, where the user query is processed using LangChain workflows. The system first performs an internet search using DuckDuckGo Search to gather relevant real-time information related to the query. Simultaneously, the Ollama server hosts the Phi3 local language model, which is responsible for generating intelligent responses. LangChain combines both the search results and the original user query into a structured prompt before sending it to the Phi3 model. The model processes the context and generates a final AI response, which is then returned through the Flask backend and displayed dynamically in the browser interface.
