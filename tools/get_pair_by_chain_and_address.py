from server import mcp
from utils import make_request
import json

@mcp.tool()
async def get_pair_by_chain_and_address(chain_id: str, pair_address: str):
    """
    Get one or multiple pairs by chain and pair address (rate-limit 300 requests per minute)

    Args:
        chain_id (str): Chain ID (e.g., "solana", "ethereum", "bsc")
        pair_address (str): Pair address

    Returns:
        dict: Formatted response with content
    """
    if not chain_id or not pair_address:
        raise ValueError("chain_id and pair_address must be non-empty strings")

    data = await make_request(f"/latest/dex/pairs/{chain_id}/{pair_address}")
    return {"content": [{"type": "text", "text": json.dumps(data, indent=2)}]}
