from google.adk.agents import Agent

root_agent = Agent(
    name = "greeting_agent",
    model="llama-3.3-70b-versatile",
    description="Greeting Agent",
    instruction="""You are a helpful assistant that greets the user. Ask for the user's name and greet them by name.""",
)