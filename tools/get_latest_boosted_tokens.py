from server import mcp
from utils import make_request
import json


@mcp.tool()
async def get_latest_boosted_tokens():
    """
    Get the latest boosted tokens (rate-limit 60 requests per minute)
    Note: Response is too big for context window - handle carefully

    Returns:
        dict: Formatted response with content
    """
    data = await make_request("/token-boosts/latest/v1")
    return {"content": [{"type": "text", "text": json.dumps(data, indent=2)}]}
