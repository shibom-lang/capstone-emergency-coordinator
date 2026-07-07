# agent.py
import asyncio
from google.antigravity import Agent, LocalAgentConfig, types

# Configure the agent
config = LocalAgentConfig(
    system_instruction="You are an emergency response coordinator. Use the provided tools and skills to find resources for people in need.",
    mcp_servers=[
        types.McpStdioServer(
            name="resource-db",
            command="python3",
            args=["mcp_server.py"]
        )
    ]
)

async def run():
    async with Agent(config) as agent:
        response = await agent.chat("I need a shelter for my family.")
        print(await response.text())

if __name__ == "__main__":
    asyncio.run(run())
