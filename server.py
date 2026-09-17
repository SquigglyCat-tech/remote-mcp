from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Remote MCP")


@mcp.tool()
def ping(message: str = "hello") -> str:
    """Test that the remote MCP server is working."""
    return f"Pong! You said: {message}"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
