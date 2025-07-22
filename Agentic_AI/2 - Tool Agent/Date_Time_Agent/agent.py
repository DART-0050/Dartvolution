from datetime import datetime

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
api_base = os.getenv("GROQ_API_BASE")

def get_current_date():
    return {"date": datetime.now().strftime("%Y-%m-%d")}

def get_current_time():
    return {"time": datetime.now().strftime("%H:%M:%S")}

root_agent = LlmAgent(
    model=LiteLlm(
        model="groq/llama-3.3-70b-versatile",
        api_key=api_key,
        api_base=api_base,
    ),
    name="Date_Time_Agent",
    description="Date and time agent",
    instruction="You are a helpful AI that provides information about the current date and time.",
    tools=[get_current_date, get_current_time],
)

