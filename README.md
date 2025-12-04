
---

# 📘 Content AI ADK — Multi-Agent Content Automation Pipeline

**Google ADK • Gemini • Python • FastAPI • Multi-Agent Orchestration**

A fully automated **AI content generation pipeline** built using the **Google Agent Development Kit (ADK)**.
This project demonstrates a clean, production-style multi-agent workflow where each agent performs a specific role:

👉 **IdeaAgent → WriterAgent → FormatterAgent**
Sequential. Consistent. Fully orchestrated.

---

## 🚀 Features

*   **Google ADK-based multi-agent workflow**
*   **Three-stage content automation pipeline**
*   **End-to-end orchestration with tool functions**
*   **Auto-generated Markdown content**
*   **ADK Web UI support**
*   **Reproducible and extensible for any content domain**

---

## 🧠 Agent Pipeline Overview

```
[ IdeaAgent ]
    ↓  (Generates 10 relevant blog ideas)

[ WriterAgent ]
    ↓  (Creates a 250–300 word draft on selected idea)

[ FormatterAgent ]
    ↓  (Outputs clean, structured Markdown)

Final Output → Ready-to-publish blog section
```

Each agent receives the previous agent’s output via **Google ADK’s orchestrated pipeline**.

---

## 📂 Project Structure

```
content-ai-adk/
│── agents/
│    ├── idea_agent.py
│    ├── writer_agent.py
│    └── formatter_agent.py
│
```

---


## Quick Start

- **Idea Agent** — comes up with topic ideas.
- **Writer Agent** — turns ideas into a draft.
- **Formatter Agent** — turns the draft into something ready to publish.

Each sub-agent does its part. The main agent runs them all in order.

---



### Setup and Prerequisites

- Download VS Code or another IDE.
- **Install Python and PIP** if you don’t have it.
- **Create and activate a virtual environment** in your project folder:

```bash
python3 -m venv venv  
source venv/bin/activate   # macOS/Linux  
.\venv\Scripts\activate    # Windows
```

- Install Google’s ADK and Dependencies

```bash
pip install google-generativeai google-ad-agents
```




- Create a project folder for your agent.

```bash
mkdir adk-example  
cd adk-example
```

- Get API Key for Gemini
- Go to [https://aistudio.google.com/](https://aistudio.google.com/), sign in, and click Get API Key.
- Create a new key and copy it — treat it like a password.
- In your project folder, create a file named .env:

```python
GEMINI_API_KEY=YOUR_API_KEY_HERE
```
- Create an __**init__.py** file and add the following content:

```python
# __init__.py  
from . import agent
```
- Create an **agent.py** file.

Your project structure should look like this:

```bash
my-agent-project/  
├── agent.py  
├── __init__.py  
└── .env
```

- Run ADK

```bash
 adk run .
venv\Scripts\adk.exe --help
venv\Scripts\adk.exe web --help
venv\Scripts\adk.exe web --port 8000 .
```


###  Open the Web UI

You will see:
✔ Three agents running sequentially
✔ Each agent’s input + output displayed
✔ Final formatted Markdown generated automatically

---

## 📝 Example Output (Short Preview)

```
## 🔥 The Future of AI Content Workflows  
AI-native pipelines are transforming content creation by...

- Agent 1: Generated the content idea  
- Agent 2: Wrote a 300-word draft  
- Agent 3: Output formatted Markdown
```

---

## 🛠 Tech Stack

* **Google Agent Development Kit (ADK)**
* **Python**
* **Gemini API**
* **FastAPI (optional)**
* **Tool-based agent orchestration**

---

## 📈 Why This Project Matters

This repo demonstrates **real, practical multi-agent development**, including:

* Sequential agent routing
* Custom tool integration
* JSON-based message passing
* ADK Web UI for transparency & debugging

Perfect foundation for:

* AI blogging tools
* Article writing pipelines
* Newsletter automation
* Research summarization
* Multi-agent LLM applications

---

## 🤝 Contributions

PRs welcome. Issues welcome. Ideas welcome.
Let’s build more AI-native content systems!

---

## 📬 Contact

**Sidhi Vyas**
🔗 LinkedIn: linkedin.com/in/sidhi-vyas
💻 GitHub: github.com/Sidhi-03

---
