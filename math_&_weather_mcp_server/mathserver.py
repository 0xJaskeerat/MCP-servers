from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math MCP server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """ _summary_
    Add two numbers
    """
    return a+b

@mcp.tool()
def sub(a: int, b: int) -> int:
    """ _summary_
    Subtract two numbers
    """
    return a-b

@mcp.tool()
def mul(a: int, b: int) -> int:
    """ _summary_
    Multiply two numbers
    """
    return a*b

@mcp.tool()
def div(a: int, b: int) -> int:
    """ _summary_
    Divide two numbers
    """
    return a/b


# The transport "stdio" tells server to use standard input /output [ stdin & stdout ] to receive and respond to toll function calls
if __name__ == "__main__":
    mcp.run(transport="stdio")