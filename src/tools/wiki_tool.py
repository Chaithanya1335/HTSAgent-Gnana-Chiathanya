from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

def get_wiki_tool():
    wrapper = WikipediaAPIWrapper(top_k_results=5,doc_content_chars_max=600)
    wiki_tool = WikipediaQueryRun(api_wrapper=wrapper,description="used to get information from internet")
    return wiki_tool