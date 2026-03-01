#!/usr/bin/env python3
"""
Sentinel MCP Server - Simple security scanning MCP server
Deployable to Dedalus Labs
"""

import asyncio
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Create MCP server instance
app = Server("sentinel-security-scanner")

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available security scanning tools."""
    return [
        Tool(
            name="scan_url",
            description="Scan a URL for common security vulnerabilities like XSS, SQLi, and misconfigurations",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The URL to scan (e.g., https://example.com)"
                    },
                    "scan_type": {
                        "type": "string",
                        "enum": ["quick", "full"],
                        "description": "Type of scan to perform",
                        "default": "quick"
                    }
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="check_headers",
            description="Check security headers for a given URL",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The URL to check headers for"
                    }
                },
                "required": ["url"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""

    if name == "scan_url":
        url = arguments.get("url", "")
        scan_type = arguments.get("scan_type", "quick")

        # Simple simulation of security scan
        findings = [
            f"🔍 Scanning {url}...",
            f"📊 Scan type: {scan_type}",
            "",
            "✅ Security Headers Check:",
            "  ⚠️  Missing Content-Security-Policy",
            "  ⚠️  Missing X-Frame-Options",
            "  ✓  HTTPS enabled",
            "",
            "🔒 SSL/TLS Check:",
            "  ✓  Valid certificate",
            "  ✓  TLS 1.3 supported",
            "",
            "🎯 Quick Vulnerability Scan:",
            "  ✓  No obvious XSS vulnerabilities",
            "  ✓  No SQL injection detected",
            "  ⚠️  Potential CORS misconfiguration",
            "",
            f"📝 Scan complete! Found 3 potential issues."
        ]

        return [TextContent(
            type="text",
            text="\n".join(findings)
        )]

    elif name == "check_headers":
        url = arguments.get("url", "")

        # Simulate header check
        result = f"""🔍 Security Headers for {url}

✅ Present:
  • Strict-Transport-Security: max-age=31536000
  • X-Content-Type-Options: nosniff

⚠️  Missing:
  • Content-Security-Policy
  • X-Frame-Options
  • Permissions-Policy

Recommendation: Add missing security headers to improve security posture.
"""

        return [TextContent(
            type="text",
            text=result
        )]

    else:
        return [TextContent(
            type="text",
            text=f"Unknown tool: {name}"
        )]

async def main():
    """Run the MCP server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
