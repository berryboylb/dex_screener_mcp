from server import mcp
from utils import make_request
import json


@mcp.tool()
async def get_pairs_by_token(chain_id: str, token_address: str):
    """
    Get one or multiple pairs by token address (rate-limit 300 requests per minute)

    Args:
        chain_id (str): Chain ID (e.g., "solana", "ethereum", "bsc")
        token_address (str): Token address

    Returns:
        dict: Formatted response with content
    """
    if not chain_id or not token_address:
        raise ValueError("chain_id and token_address must be non-empty strings")

    data = await make_request(f"/tokens/v1/{chain_id}/{token_address}")
    return {"content": [{"type": "text", "text": json.dumps(data, indent=2)}]}
