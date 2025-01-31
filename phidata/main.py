from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo

agent = Agent(
    name="Web Agent",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
    monitoring=True,
    debug_mode=True,
)
agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[
        "https://upload.wikimedia.org/wikipedia/commons/b/bf/Krakow_-_Kosciol_Mariacki.jpg"
    ],
    stream=True,
)
# debug mode is important!
