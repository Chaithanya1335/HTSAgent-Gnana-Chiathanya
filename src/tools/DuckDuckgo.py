from langchain_community.tools import DuckDuckGoSearchRun
from src.exception import CustomException
from src.logger import logging



def get_duck_tool():
    """
    This function is used for websearch
    """
    duct_tool = DuckDuckGoSearchRun()
    return duct_tool


