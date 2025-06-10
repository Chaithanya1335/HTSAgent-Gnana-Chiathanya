from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

def get_wiki_tool():
    """
    Initializes and returns a Wikipedia search tool for retrieving information from the internet.

    This function configures a `WikipediaAPIWrapper` to fetch a maximum of 5 top results
    with each document's content truncated to 600 characters. It then wraps this API
    client within a `WikipediaQueryRun` tool, making it suitable for use in LangChain
    agents or other tool-enabled applications.

    Returns:
        WikipediaQueryRun: An initialized instance of the Wikipedia search tool.
                           This tool can be used to query Wikipedia and retrieve
                           summarized information.
    """
    wrapper = WikipediaAPIWrapper(top_k_results=5,doc_content_chars_max=600)
    wiki_tool = WikipediaQueryRun(api_wrapper=wrapper,description="used to get information from internet")
    return wiki_tool