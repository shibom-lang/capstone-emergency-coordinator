# mcp_server.py
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import sqlite3
import asyncio

server = Server("resource-db")
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE resources (id INTEGER PRIMARY KEY, type TEXT, name TEXT, capacity INTEGER)")
db.execute("INSERT INTO resources (type, name, capacity) VALUES ('shelter', 'Downtown Community Center', 50)")
db.execute("INSERT INTO resources (type, name, capacity) VALUES ('food', 'Food Bank A', 200)")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="query_resources",
            description="Query the emergency resources database",
            inputSchema={
                "type": "object",
                "properties": {
                    "resource_type": {"type": "string", "description": "Type of resource (e.g., 'shelter', 'food')"}
                },
                "required": ["resource_type"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "query_resources":
        resource_type = arguments.get("resource_type")
        cursor = db.execute("SELECT * FROM resources WHERE type=?", (resource_type,))
        results = cursor.fetchall()
        return [TextContent(type="text", text=str(results))]

async def main():
    async with stdio_server() as (read, write):
        init_options = server.create_initialization_options()
        await server.run(read, write, init_options)

if __name__ == "__main__":
    asyncio.run(main())
