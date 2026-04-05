from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather MCP server")

@mcp.tool()
async def get_weather(city: str) -> str:
    """ _summary_
     Get the weather location.
    """
    return "It's mostly running in this city "

if __name__ == "__main__":
    mcp.run(transport = "streamable-http")       