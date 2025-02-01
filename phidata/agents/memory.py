from phi.agent import Agent
from phi.model.google import Gemini
from rich.pretty import pprint

# every agent has built in memory but without database these message are in memmory only while session currently active
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    # Set add_history_to_messages=true to add the previous chat history to the messages sent to the Model.
    add_history_to_messages=True,
    # Number of historical responses to add to the messages.
    num_history_responses=3,
    description="You are a helpful assistant that always responds in a polite, upbeat and positive manner.",
)
agent.print_response("Share a 2 sentence horror story", stream=True)
pprint([m.model_dump(include={"role", "content"}) for m in agent.memory.messages])

print(agent.memory.messages[0])
# agent.print_response("What was my first message?", stream=True)
# pprint([m.model_dump(include={"role", "content"}) for m in agent.memory.messages])
