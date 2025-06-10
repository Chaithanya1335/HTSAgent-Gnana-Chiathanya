from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from src.utils import get_llm
from src.exception import CustomException
from src.logger import logging
from src.tools.Rag_tool import rag_query_tool 
from src.tools.Duty_Calculator_tool import calculate_tariff_duty
from src.tools.DuckDuckgo import get_duck_tool
from src.tools.wiki_tool import get_wiki_tool
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


class Agent:
    def __init__(self):
        duck = get_duck_tool()
        wiki_tool = get_wiki_tool()
        self.tools = [rag_query_tool, calculate_tariff_duty,duck,wiki_tool]
        self.llm = get_llm(model_name = 'gemini-1.5-flash',api_key = api_key )
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    def initialize_agent(self):
        agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            memory=self.memory,  
            verbose=True,
        )

        return agent



if __name__=="__main__":
    agent = Agent().initialize_agent()
    

    response = agent.run("What is United States-Israel Free Trade Agreement?")
    print(response)
