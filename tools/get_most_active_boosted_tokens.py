from server import mcp
from utils import make_request
import json

@mcp.tool()
async def get_most_active_boosted_tokens():
    """
        Get the tokens with most active boosts (rate-limit 60 requests per minute)
        Note: Response is too big for context window - to be optimized

        Returns:
            dict: Formatted response with content
    """
    data = await make_request("/token-boosts/top/v1")
    return {"content": [{"type": "text", "text": json.dumps(data, indent=2)}]}
