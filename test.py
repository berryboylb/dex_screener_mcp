from fastmcp import Client
from server import mcp
import tools
import asyncio


async def test_server_locally():
    print("\n--- Testing Server Locally ---")
    client = Client(mcp)

    async with client:
        # get_latest_boosted_tokens = await client.call_tool(
        #     "get_latest_boosted_tokens", {}
        # )
        # print(f"get_latest_boosted_tokens: {get_latest_boosted_tokens}")

        # get_latest_token_profiles = await client.call_tool(
        #     "get_latest_token_profiles", {}
        # )
        # print(f"get_latest_token_profiles: { get_latest_token_profiles}")

        get_most_active_boosted_tokens = await client.call_tool(
            "get_most_active_boosted_tokens", {}
        )
        print(f"get_most_active_boosted_tokens: {get_most_active_boosted_tokens}")

        search_pairs = await client.call_tool("search_pairs", {"query": "$pump"})
        print(f"search_pairs: {search_pairs}")



# Run the local test function
asyncio.run(test_server_locally())
