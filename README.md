# Multimode_agenticAI

**Multimode_agenticAI** is a Python-based agentic AI project designed to simulate multi-agent behavior for real-world tasks such as financial decision-making, contextual interactions, and intelligent responses. The system integrates LLM-based agents, real-time data tools, and interactive prompts to showcase agent collaboration and reasoning.

---

## 🚀 Overview

This project demonstrates:
- Autonomous financial agent reasoning
- Multi-agent coordination
- Real-time query processing
- Streamed LLM responses and external tool calling
- Usage of LangGraph, Groq, OpenAI, and DuckDuckGo tools

---

## 🧱 Project Structure

- financial_agent.py: Implements a financial analyst agent capable of real-time decision-making and data summarization.
- playground.py: A sandbox for testing custom tasks, user prompts, and agent collaboration.
- .env: Stores API keys and environment configs (like GROQ_API_KEY, OPENAI_API_KEY).
- requirements.txt: Lists Python libraries and versions needed to run the project.
- .gitignore: Git tracking exclusions for venv, .env, cache files etc.

---

## 🧑‍💻 Tech Stack

- **Language**: Python
- **LLMs**: Groq (via qwen-2.5-32b), OpenAI (optional)
- **Frameworks**: LangGraph, LangChain Community
- **Tool Integration**: DuckDuckGoTools, PDFUrlKnowledgeBase
- **Vector Store**: LanceDB
- **Embeddings**: SentenceTransformer (MiniLM)
- **Deployment Ready**: Easily expandable to Streamlit/FastAPI-based frontends

---

## 🛠️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/shivam-kr935/Multimode_agenticAI.git
cd Multimode_agenticAI
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
# Windows:
venv\\Scripts\\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API keys
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_key
OPENAI_API_KEY=your_openai_key
```

---

## ▶️ Running the Project

### Run financial agent
```bash
python financial_agent.py
```

### Run multi-agent playground
```bash
python playground.py
```

> ℹ️ Agents will stream output based on tasks like summarizing stock news, comparing companies, etc.

---

## 📌 Features

- Multi-agent task delegation
- Groq + OpenAI LLMs
- Embedded PDF-based knowledge base
- External tool support via DuckDuckGo
- LanceDB hybrid vector search
- SentenceTransformer-based embeddings
- Modular and scalable codebase

---

## 📄 License

This project is licensed under the [GPL-2.0 License](LICENSE).

---

## 🤝 Contributing

Feel free to fork, improve, and create pull requests. Let's build smarter agents together!

---

## 📬 Contact

For queries or collaboration, reach out to [shivam-kr935](https://github.com/shivam-kr935).
