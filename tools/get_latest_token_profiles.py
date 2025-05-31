from server import mcp
from utils import make_request
import json


@mcp.tool()
async def get_latest_token_profiles():
    """
        Get the latest token profiles (rate-limit 60 requests per minute)
        
        Returns:
            dict: Formatted response with content
    """
    data = await make_request("/token-profiles/latest/v1")
    return {"content": [{"type": "text", "text": json.dumps(data, indent=2)}]}
