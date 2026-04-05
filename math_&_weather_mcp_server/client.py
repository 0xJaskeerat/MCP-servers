import mathserver
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio 

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"], # this is the command to start the server
                "transport": "stdio" # this is the transport to use
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "http"
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model - ChatGroq(model = "quen-qwq-32b");
    agent = create_react_agent(
        model, tools
    )

    math_response = await agent.ainvoke({
        "messages": [{
            "role": "user",
            "content": "what's (4 + 8) * 123 ?"
        }]
    })

    print("math response", math_response['messages'][-1].content)

    weather_response = await agent.ainvoke({    
        "messages": [{
            "role": "user",
            "content": "what's the weather like in New York?"
        }]
    })

    print("weather response", weather_response['messages'][-1].content)

asyncio.run(main())

