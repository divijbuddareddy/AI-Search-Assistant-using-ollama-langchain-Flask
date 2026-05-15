# AI Search Assistant using Ollama + LangChain

AI Search Assistant is a locally powered AI chatbot built using Ollama, LangChain, Flask, and the Phi-3. The project combines local Large Language Model (LLM) capabilities with real-time internet search to generate intelligent and up-to-date responses through a modern web interface. Unlike cloud-based AI systems, this application runs directly on the local machine without relying on paid APIs, making it lightweight, privacy-friendly, and cost-effective for learning and experimentation.

The application uses Flask as the backend server to manage requests between the frontend and the AI model. LangChain is used to orchestrate the interaction between the Ollama-powered Phi3 model and the internet search tool powered by DuckDuckGo Search. When a user asks a question, the application first performs an internet search, gathers relevant information, and then sends both the user query and search results to the AI model for intelligent response generation. This creates a simple Retrieval-Augmented Generation (RAG)-style workflow capable of answering coding questions, technical queries, general knowledge prompts, and real-time informational requests.

The frontend interface is designed using HTML, JavaScript, and Tailwind CSS to provide a modern chatbot experience with responsive design and interactive chat bubbles. The project architecture demonstrates the integration of AI models, search systems, backend APIs, and frontend user interfaces into a complete AI-powered web application. Since the system runs locally using Ollama, it does not require external API keys such as OpenAI APIs, making it suitable for students, beginners, and developers exploring local AI engineering.

This project also serves as a strong beginner-to-intermediate portfolio project for Artificial Intelligence and Machine Learning engineering. It demonstrates practical skills in local LLM deployment, AI-assisted search workflows, Flask backend development, prompt engineering, LangChain integration, and full-stack AI application development. Future improvements for the project can include conversation memory, voice assistant capabilities, PDF document chat, streaming AI responses, multi-agent systems, and database integration for persistent chat history.
# AI-Search-chatbot-using-ollama-langchain

## Tech Stack

- Flask
- LangChain
- Ollama
- Phi3
- Tailwind CSS
