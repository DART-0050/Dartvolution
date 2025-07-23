from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name = "Tool_Agent",
    model = "gemini-2.0-flash",
    description = "Tool Agent",
    instruction = "You are a tool agent that uses tools to complete tasks by using the following tools: google_search",
    tools = [google_search],
)