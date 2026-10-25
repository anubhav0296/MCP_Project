from mcp.server import MCPServer

# Create an object of MCP Server
mcp = MCPServer("Travel Server")

@mcp.tool()
def my_tool():
    pass

@mcp.resource()
def my_resource():
    pass

@mcp.prompt()
def my_prompt():
    pass
