import os
import sys
from pathlib import Path
import datetime

from dotenv import load_dotenv
from google.adk.agent import Agent, LoopAgent
from google.adk.tools import agent_tool

load_dotenv()

MODEL = os.getenv("MODEL", "gemini-flash-latest")

blog_planner = Agent(
    name = "BlogPlanner",
    model = MODEL,
    description = "Creates a practical, skimmable outline in Markdown",
    instruction = """
You are a technical content strategist. Produce a clear Markdown outline with:
- Title
- Short intro
- 4-6 main sections (each with 2-3 bullets)
- Conclusion

If 'codebase_context' exists in state, weave in specific sections/snippets.
Return only the outline in Markdown.
""",
    output_key = "blog_outline",
)