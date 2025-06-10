from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.tools import Tool
from src.utils import get_llm
from src.exception import CustomException
from src.logger import logging
from src.tools.Rag_tool import rag_query_tool 
from src.tools.Duty_Calculator_tool import calculate_tariff_duty
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


class Agent:
    def __init__(self):
        self.tools = [rag_query_tool, calculate_tariff_duty]
        self.llm = get_llm(model_name = 'gemini-1.5-flash',api_key = api_key )

    def initialize_agent(self):
        agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # or AGENT_TYPE.ZERO_SHOT_REACT_DESCRIPTION
            verbose=True
        )

        return agent



if __name__=="__main__":
    agent = Agent().initialize_agent()
    

    response = agent.run("What is United States-Israel Free Trade Agreement?")
    print(response)
