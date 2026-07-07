---
name: resource-matcher
description: |
  Helps match emergency requests with available resources. Use this skill when the user asks for shelter, food, or emergency supplies.
---

# Resource Matcher Skill

When asked to find resources, follow these steps:
1. Identify the exact resource type requested.
2. Query the `query_resources` tool provided by the MCP server.
3. If no resources are found, advise the user to contact emergency services directly.
4. Format the output clearly for the user.
