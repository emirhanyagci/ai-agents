from smolagents import CodeAgent, tool, LiteLLMModel, DuckDuckGoSearchTool,ManagedAgent
from phoenix.otel import register

model = LiteLLMModel(
    model_id="ollama/qwen2.5-coder:latest", 
    api_base="http://localhost:11434", 
)

web_agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

managed_web_agent = ManagedAgent(
    agent=web_agent,
    name="web_search",
    description="Runs web searches for you. Give it your query as an argument."
)
manager_agent = CodeAgent(
    tools=[], model=model, managed_agents=[managed_web_agent]
)


manager_agent.run("If the US keeps its 2024 growth rate, how many years will it take for the GDP to double?")
