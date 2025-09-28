
---

# Literature Review Agent

An AI-powered research assistant that automatically **searches, summarizes, and analyzes academic papers** from arXiv. Built with **Streamlit**, **GROQ API**, and **AutoGen agents** for multi-agent orchestration.

---

## 🔹 Features

* **Automated Literature Search**: Search arXiv for relevant papers using natural language queries.
* **Multi-Agent Analysis**: A round-robin workflow between:

  * **ArxivAgent**: Finds papers on a topic.
  * **Researcher**: Summarizes and generates a structured markdown report.
* **Interactive Chat Interface**: Streamlit-based chat UI showing agent messages and tool execution events.
* **Tool Integration**: Handles tool call requests and executions within the interface.
* **Live Streaming**: Messages appear in real-time as agents process the task.

---

## 🔹 Demo

[Open Live App](https://ai-agent-to-hunt-and-summarize-research-papers-nyycihyvq9nbnzj.streamlit.app/)

---

## 🔹 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/literature-review-agent.git
cd literature-review-agent
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your **GROQ API key**:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🔹 Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

* Enter your research topic in the text input.
* Click **Find Papers**.
* View live results in the chat interface:

  * **Human messages** → Papers fetched by ArxivAgent.
  * **Assistant messages** → Summaries and structured reports by Researcher.
* Tool call requests and executions can be expanded in the interface.

---

## 🔹 Project Structure

```
literature-review-agent/
│
├── agents.py           # Multi-agent configuration & orchestration
├── app.py              # Streamlit frontend
├── requirements.txt    # Python dependencies with pinned versions
├── .env                # Environment variables (API keys)
├── README.md
└── utils/              # Optional: helper functions (e.g., arXiv search)
```

---

## 🔹 Dependencies

Key packages:

* `streamlit`
* `autogen-agentchat`
* `autogen-core`
* `autogen-ext`
* `arxiv`
* `python-dotenv`
* `asyncio`

*(Full pinned versions in `requirements.txt`.)*


---

## 🔹 License

MIT License © 2025

---


