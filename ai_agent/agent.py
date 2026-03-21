from langchain_community.llms import  OpenAI
from langchain.agents import initialize_agent,Tool
from tools import get_weather,calculator

def create_agent():
    tools = [
        Tool(
            name = "Weather Tool",
            func = get_weather,
            description="Get weather of a city"
        ),
        Tool(
            name = "Calculator",
            func = calculator,
            description="Solve Math Expression"
        )
    ]
    
    llm = OpenAI(temperature = 0.6)
    
    agent = initialize_agent(
        tools,
        llm,
        agent = "zero-shot-react-description",
        verbose = True
    )
    
    return agent