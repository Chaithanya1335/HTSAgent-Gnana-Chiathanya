from langchain_community.tools import DuckDuckGoSearchRun
from src.exception import CustomException
from src.logger import logging



def get_duck_tool():
    """
    Initializes and returns a DuckDuckGo web search tool.

    This function creates an instance of DuckDuckGoSearchRun, which allows
    an agent to perform web searches using DuckDuckGo.

    Returns:
        DuckDuckGoSearchRun: An instance of the DuckDuckGo web search tool.
    """
    duct_tool = DuckDuckGoSearchRun()
    return duct_tool


