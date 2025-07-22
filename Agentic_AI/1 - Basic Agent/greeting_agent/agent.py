from dotenv import load_dotenv
load_dotenv()

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

root_agent = LlmAgent(
    model=LiteLlm(
        model="groq/llama-3.3-70b-versatile",
        api_key="...",
        api_base="https://api.groq.com/openai/v1"
    ),
    name="greeting_agent",
    description="Greeting agent",
    instruction="You are a friendly AI that warmly greets people and responds casually to greetings.",
)
