from server import mcp
import tools


# Entry point to run the server
if __name__ == "__main__":
    # RUNS ON LOCAL OR DEV ONLY
    # mcp.run(transport="stdio")
    
    # RUNS ON REMOTE SERVER
    import asyncio
    asyncio.run(mcp.run_sse_async(host="0.0.0.0", port=5001, log_level="debug"))
