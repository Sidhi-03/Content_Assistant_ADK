# agent.py
import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.adk.agents import LlmAgent, SequentialAgent

# Load .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# Configure Google Gen AI SDK
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("Missing GOOGLE_API_KEY in .env")
genai.configure(api_key=api_key)

# Tool functions
def generate_ideas(topic: str) -> str:
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    resp = model.generate_content(f"Brainstorm 4–6 creative blog post ideas for the topic:\n\n{topic}")
    return resp.text

def write_content(ideas: str) -> str:
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    resp = model.generate_content(f"Expand the following outline into a cohesive ~300-word blog post:\n\n{ideas}")
    return resp.text

def format_draft(draft: str) -> str:
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    resp = model.generate_content(f"Format this draft as clean Markdown with headings, sub-headings, and bullet lists:\n\n{draft}")
    return resp.text

# Define LLM agents
topic_agent = LlmAgent(
    name="IdeaAgent",
    model="gemini-2.0-flash",
    description="Brainstorms blog post ideas.",
    instruction="Call generate_ideas(topic) with the exact topic string you receive and return only the ideas.",
    tools=[generate_ideas],
    output_key="ideas"
)

draft_agent = LlmAgent(
    name="WriterAgent",
    model="gemini-2.0-flash",
    description="Writes a blog post draft from ideas.",
    instruction="Call write_content(ideas), where `ideas` is the output from the prior step, and return only the draft text.",
    tools=[write_content],
    output_key="draft"
)

format_agent = LlmAgent(
    name="FormatterAgent",
    model="gemini-2.0-flash",
    description="Formats the draft into Markdown.",
    instruction="Call format_draft(draft), where `draft` is the previous output, and return only the final Markdown.",
    tools=[format_draft],
    output_key="formatted"
)

# Root agent
root_agent = SequentialAgent(
    name="ContentAssistant",
    sub_agents=[topic_agent, draft_agent, format_agent],
    description="Takes a user topic → generates ideas → writes draft → formats as Markdown"
)

