from re import search

from langchain_tavily import TavilySearch


def get_profile_url_tavily(text: str):
    """Search for LinkedIn or Tweeter profile Page."""
    search_text = TavilySearch()
    response = search_text.run(f"{text}")
    return response
