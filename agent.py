# agent.py
from google_antigravity import LocalAgentConfig, Conversation
from google_antigravity.mcp import McpStdioConfig

# Define the MCP server configuration
mcp_config = McpStdioConfig(
    name="resource-db",
    command="python",
    args=["mcp_server.py"]
)

# Configure the agent
config = LocalAgentConfig(
    system_instruction="You are an emergency response coordinator. Use the provided tools and skills to find resources for people in need.",
    mcp_servers=[mcp_config],
    model="gemini-3.1-pro"
)

def run():
    conv = Conversation(config)
    response = conv.send_message("I need a shelter for my family.")
    print(response.text)

if __name__ == "__main__":
    run()
