from server import mcp
from utils import make_request
import json
import urllib.parse

@mcp.tool()
async def search_pairs(query: str):
    """
    Search for pairs matching query (rate-limit 300 requests per minute)

    Args:
        query (str): Search query (e.g., "SOL/USDC")

    Returns:
        dict: Formatted response with content
    """
    if not query:
        raise ValueError("query must be a non-empty string")

    encoded_query = urllib.parse.quote(query)

    data = await make_request(f"/latest/dex/search?q={encoded_query}")
    return {"content": [{"type": "text", "text": json.dumps(data, indent=2)}]}
