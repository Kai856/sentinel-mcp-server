# Sentinel MCP Server

A simple Model Context Protocol (MCP) server for basic security scanning, built with FastMCP.

## Features

- **scan_url**: Scan a URL for common security vulnerabilities
- **check_headers**: Check security headers for a given URL

## Installation

```bash
pip install fastmcp
```

## Usage

### Run locally
```bash
python server.py
```

The server will start on http://localhost:8000 with the MCP endpoint at `/mcp`.

### Deploy to Dedalus Labs

1. Go to https://www.dedaluslabs.ai/dashboard/servers
2. Click "Add Server"
3. Select "From GitHub Repository"
4. Enter: `https://github.com/Kai856/sentinel-mcp-server`
5. Deploy!

## Tools Available

### scan_url
Performs a quick security scan on a URL.

**Parameters:**
- `url` (required): The URL to scan
- `scan_type` (optional): "quick" or "full" (default: "quick")

**Example:**
```json
{
  "url": "https://example.com",
  "scan_type": "quick"
}
```

### check_headers
Checks security headers for a URL.

**Parameters:**
- `url` (required): The URL to check

**Example:**
```json
{
  "url": "https://example.com"
}
```

## Example Output

```
🔍 Scanning https://example.com...
📊 Scan type: quick

✅ Security Headers Check:
  ⚠️  Missing Content-Security-Policy
  ⚠️  Missing X-Frame-Options
  ✓  HTTPS enabled

🔒 SSL/TLS Check:
  ✓  Valid certificate
  ✓  TLS 1.3 supported

🎯 Quick Vulnerability Scan:
  ✓  No obvious XSS vulnerabilities
  ✓  No SQL injection detected
  ⚠️  Potential CORS misconfiguration

📝 Scan complete! Found 3 potential issues.
```

## Testing Locally

```bash
# Start the server
python server.py

# In another terminal, test the endpoint
curl http://localhost:8000/mcp
```

## License

MIT
