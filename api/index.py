from fastapi import FastAPI, Request
from pydantic import BaseModel
from google.antigravity import Agent, LocalAgentConfig, types
import os
import sys

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MCP_PATH = os.path.join(BASE_DIR, "mcp_server.py")

# Configuration for the Antigravity Agent
config = LocalAgentConfig(
    system_instruction="You are an emergency response coordinator. Use the provided tools to find resources. Format all output cleanly in Markdown.",
    mcp_servers=[
        types.McpStdioServer(
            name="resource-db",
            command=sys.executable,
            args=[MCP_PATH]
        )
    ]
)

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    if not os.environ.get("GEMINI_API_KEY"):
        return {"response": "Error: GEMINI_API_KEY is not set on the server."}
        
    try:
        async with Agent(config) as agent:
            response = await agent.chat(request.message)
            text = await response.text()
            return {"response": text}
    except Exception as e:
        return {"response": f"An error occurred: {str(e)}"}
