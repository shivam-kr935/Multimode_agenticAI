#import openai
from phi.agent import Agent
import phi.api
#from phi.model.openai import OpenAIChat
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools 
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv 

import os
import phi 
from phi.playground import Playground,serve_playground_app

#Load environment variables from dotenv file
load_dotenv()
phi.api=os.getenv("phi-dtttV0vaSs6pGhv5bWSv5XMOeAOY8FhhMDUghZnHCa0") 

## web search agent
web_search_agent=Agent(
    name="Web Seach_Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    markdown=True,
) 
#Financial Agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=
                      True,company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

app=Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)