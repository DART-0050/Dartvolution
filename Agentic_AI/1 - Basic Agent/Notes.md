# Agentic Development Kit (ADK) — Modules Overview

Google’s **Agent Development Kit (ADK)** is a modular Python & Java toolkit to build *agentic* applications — ones that use LLMs as reasoning engines with goals, memory, tools, and autonomy.

---

## Key ADK Python Modules

| Module                       | Description                                                                                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `google.adk.agents`          | Contains core agent classes like `LlmAgent`, `GoalAgent`, and `MultiAgent` which represent different types of intelligent agents.                                   |
| `google.adk.models`          | Contains model wrappers like `LiteLlm`, `Claude`, and support for Gemini/Vertex/Anthropic APIs. These let you plug in any LLM backend.                              |
| `google.adk.models.lite_llm` | Contains the `LiteLlm` class — a wrapper that makes 100+ models (like Groq, OpenAI, Claude) compatible via the [LiteLLM](https://github.com/BerriAI/litellm) layer. |
| `google.adk.models.registry` | Lets you register custom models (needed for advanced custom or third-party usage).                                                                                  |
| `google.adk.memory`          | Modules for agent memory and state tracking across turns.                                                                                                           |
| `google.adk.tools`           | Lets you register tools/functions that agents can use through function calling.                                                                                     |
| `google.adk.planning`        | Enables hierarchical and goal-directed behavior via planning modules.                                                                                               |
| `google.adk.cli`             | Command-line tools and utilities for managing agents and interactions.                                                                                              |

---

## Why we use `LlmAgent` and `LiteLlm` (not just `Agent`)

| Class                         | Why we use it                                                                                                                                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`LlmAgent`**                | This is an *LLM-powered agent*. It handles basic prompting, context, memory (if needed), and outputs the LLM’s reply. Ideal for simple chat and single-turn reasoning.                                  |
| **`LiteLlm`**                 | This is a *model adapter*, not an agent. It plugs in **Groq, OpenAI, Claude**, and many other models into ADK using \[LiteLLM] so you don’t need to write custom integrations.                          |
| **We don’t use `Agent` here** | `Agent` is a base abstract class. It's used under the hood in more complex scenarios (like `GoalAgent` or `ToolAgent`). For chatting with an LLM, `LlmAgent` is easier and built specifically for this. |

---

## Dissecting Your `root_agent` Code

```python
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

root_agent = LlmAgent(
    model=LiteLlm(
        model="groq/llama-3.3-70b-versatile",
        api_key="YOUR_API_KEY",
        api_base="https://api.groq.com/openai/v1"
    ),
    name="greeting_agent",
    description="Greeting agent",
    instruction="You are a friendly AI that warmly greets people and responds casually to greetings.",
)
```

| Part                                   | Meaning                                                                                                                                              |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LlmAgent`                             | Main agent class that lets you define how the LLM should behave. It calls the model using prompt + instruction.                                      |
| `model=LiteLlm(...)`                   | Injects a LiteLLM-compatible model — in this case, **Groq’s LLaMA 3.3 70B**. LiteLlm handles the API format so ADK can treat it like a native model. |
| `model="groq/llama-3.3-70b-versatile"` | A string identifier used by LiteLLM to know which model to route the call to.                                                                        |
| `api_key=...`                          | Authenticates the API call. Keep this in a `.env` file ideally.                                                                                      |
| `api_base=...`                         | Points LiteLLM to Groq’s OpenAI-compatible endpoint.                                                                                                 |
| `name="greeting_agent"`                | Gives your agent an internal name (can be useful in multi-agent setups).                                                                             |
| `description="Greeting agent"`         | Adds a docstring-style label about this agent’s role.                                                                                                |
| `instruction="..."`                    | System prompt — tells the LLM how to behave in general. This becomes the *system message* under the hood.                                            |

---

## Summary

* **ADK modules** give you access to agents, memory, tools, and model adapters.
* **`LlmAgent`** is perfect for chat-style agents or anything driven by prompt-response.
* **`LiteLlm`** makes it easy to use 100+ models including Groq, OpenAI, Anthropic, Ollama etc.
* You don’t use `Agent` directly unless doing custom builds.
* `root_agent` is a single-agent that uses Groq’s LLaMA model to behave like a friendly greeter.
