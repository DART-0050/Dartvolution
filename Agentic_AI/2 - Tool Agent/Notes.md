# Tool Types in ADK

ADK offers flexibility by supporting several types of tools:

## 1. Function Tools

Tools created by you, tailored to your specific application's needs.

- **Functions/Methods**: Define standard synchronous functions or methods in your code (e.g., Python `def`).
- **Agents-as-Tools**: Use another, potentially specialized, agent as a tool for a parent agent.
- **Long Running Function Tools**: Support for tools that perform asynchronous operations or take significant time to complete.

## 2. Built-in Tools

Ready-to-use tools provided by the framework for common tasks.

- Google Search
- Code Execution
- Retrieval-Augmented Generation (RAG)

Can only work with Gemini.

## 3. Third-Party Tools

Integrate tools seamlessly from popular external libraries.

- LangChain Tools
- CrewAI Tools

For detailed information and examples for each tool type, please refer to the respective documentation pages.
