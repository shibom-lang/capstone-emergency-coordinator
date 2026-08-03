from mcp.server.fastmcp import FastMCP
import sqlite3

mcp = FastMCP("resource-db")
db = sqlite3.connect(":memory:", check_same_thread=False)
db.execute("CREATE TABLE resources (id INTEGER PRIMARY KEY, type TEXT, name TEXT, capacity INTEGER)")
db.execute("INSERT INTO resources (type, name, capacity) VALUES ('shelter', 'Downtown Community Center', 50)")
db.execute("INSERT INTO resources (type, name, capacity) VALUES ('food', 'Food Bank A', 200)")

@mcp.tool()
def query_resources(resource_type: str) -> str:
    """Query the emergency resources database for a specific resource type (e.g. shelter, food)."""
    cursor = db.execute("SELECT * FROM resources WHERE type=?", (resource_type,))
    results = cursor.fetchall()
    return str(results)

if __name__ == "__main__":
    mcp.run()
