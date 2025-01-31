# get_top_hackernews_stories
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.newspaper4k import Newspaper4k

import json
import httpx


def get_top_stories(num_stories: int = 10):
    """Use this function to get top stories urls from Hacker News.

    Args:
        num_stories (int) : Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of top stories

    """
    response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = response.json()
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        story = story_response.json()
        stories.append(story["url"])
    print(stories)
    return json.dumps(stories)


agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    description="You are senior researcher for fetching top Hacker News Article and Summarize them",
    instructions=[
        "For a given num_stories, search for the top stories",
        "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
        "Analyse and prepare for each url article based on the information.",
    ],
    tools=[get_top_stories, Newspaper4k()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)
