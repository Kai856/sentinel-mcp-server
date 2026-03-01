#!/usr/bin/env python3
"""
Main entrypoint for Sentinel MCP Server
Uses HTTP/SSE transport for cloud deployment
"""

from server import mcp

if __name__ == "__main__":
    # Run with HTTP transport (not stdio) for cloud deployment
    mcp.run(transport="sse")
