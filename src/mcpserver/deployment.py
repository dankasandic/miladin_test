from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b