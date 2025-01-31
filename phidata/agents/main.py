from phi.agent import Agent, RunResponse
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
from phi.utils.pprint import pprint_run_response
from typing import Iterator

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[DuckDuckGo(), Newspaper4k()],
    description="You are a senior NYT researcher writing an article on a topic.",
    instructions=[
        "For a given topic, search for the top 5 links.",
        "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
        "Analyse and prepare an NYT worthy article based on the information.",
    ],
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    # debug_mode=True,
)

# capturing agent response

# response: RunResponse = agent.run("Simulation theory")
# pprint_run_response(response, markdown=True)

response_stream: Iterator[RunResponse] = agent.run("Simulation theory", stream=True)
pprint_run_response(response_stream, markdown=True, show_time=True)
