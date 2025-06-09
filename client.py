from agents import Agent, Runner, WebSearchTool
from agents.tool import UserLocation
from agents.mcp import MCPServerStdio, MCPServerSse
from dotenv import load_dotenv
import asyncio
import json
import logging

logger = logging.getLogger(__name__)
load_dotenv()

PROMPT = """
    You are an expert cryptocurrency analyst with access to real-time DexScreener data. Use search pairs instead of token profiles for you tool calls.

    Your expertise includes:
    - Token analysis and price trends
    - Liquidity pool analysis  
    - Trading volume patterns
    - Market cap evaluation
    - Risk assessment for DeFi tokens
    - Identifying potential opportunities and red flags

    When users ask about crypto tokens or markets:
    1. **Always fetch current data** using DexScreener tools before providing analysis
    2. **Provide comprehensive analysis** including:
    - Current price and 24h change
    - Trading volume and liquidity
    - Market cap and fully diluted valuation
    - Price trends (1h, 24h, 7d if available)
    - Liquidity pool health
    3. **Risk assessment**: Always mention potential risks and volatility
    4. **Educational context**: Explain technical terms for beginners
    5. **No financial advice**: Make clear this is analysis, not investment advice

    Key areas to analyze:
    - **Price Action**: Current trends, support/resistance levels
    - **Volume**: Trading activity and liquidity depth  
    - **Tokenomics**: Supply metrics, distribution
    - **Market Behavior**: Unusual activity, whale movements
    - **Comparative Analysis**: How token performs vs similar projects

    Always start responses with current data, then provide your expert analysis.

    **Disclaimer**: Always remind users that crypto is highly volatile and they should do their own research.
"""


async def run_local() -> None:
    async with MCPServerStdio(
        params={
            "command": "uv",
            "args": ["run", "main.py"],
            "cwd": "/Users/user/Documents/python/dex_screnner_mcp",
            "env": {},  # optional environment variables
        }
    ) as server:

        # tools = await server.list_tools()

        # print("📋 Listing tools...")
        # tools = await server.list_tools()
        # print(f"Found {len(tools)} tools:")
        # for tool in tools:
        #     print(f"  - {tool.name}: {tool.description}")

        agent = Agent(
            name="dex_screener",
            instructions=PROMPT,
            model="gpt-4o-mini",
            tools=[
                WebSearchTool(
                    search_context_size="high",
                    user_location=UserLocation(
                        type="approximate",
                    ),
                ),
            ],
            mcp_servers=[server],
        )

        while True:
            user_input = input("Ask your questions: ")
            if user_input.lower() == "exit":
                print("Bye")
                break

            result = await Runner.run(
                agent,
                input=user_input,
            )
            print(">>> response <<<", result.final_output)


async def run_sse() -> None:
    logger.info("Using SSE protocol for mcp")
    URL = "http://0.0.0.0:5001/sse"
    server = MCPServerSse({"url": URL})

    try:
        await server.connect()
        agent = Agent(
            name="dex_screener",
            instructions=PROMPT,
            model="gpt-4o-mini",
            tools=[
                WebSearchTool(
                    search_context_size="high",
                    user_location=UserLocation(
                        type="approximate",
                    ),
                ),
            ],
            mcp_servers=[server],
        )

        while True:
            user_input = input("Ask your questions: ")
            if user_input.lower() == "exit":
                print("Bye")
                break

            result = await Runner.run(
                agent,
                input=user_input,
            )
            print(">>> response <<<", result.final_output)
    finally:
        await server.cleanup()


async def main(local: True) -> None:
    if local:
       await run_local()
    else:
       await run_sse()


async def debug_connection():
    try:
        print("🔍 Attempting to connect to MCP server...")

        async with MCPServerStdio(
            params={
                "command": "uv",
                "args": ["run", "main.py"],
                "cwd": "/Users/user/Documents/python/dex_screnner_mcp",
            }
        ) as server:
            print("✅ Connection established!")

            # Try to list tools
            print("📋 Listing tools...")
            tools = await server.list_tools()
            print(f"Found {len(tools)} tools:")
            for tool in tools:
                print(f"  - {tool.name}: {tool.description}")

    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print(f"Error type: {type(e).__name__}")

        # Print full traceback
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main(local=False))
