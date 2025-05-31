# DexScreener MCP Server

A comprehensive Model Context Protocol (MCP) server that provides access to the DexScreener API for decentralized exchange data and analytics.

## 🚀 Features

- **8 Comprehensive Tools** for accessing DexScreener data
- **Async/Await Support** for optimal performance
- **Rate Limit Aware** with documented limits for each endpoint
- **Type Safe** with proper Python type hints
- **Error Handling** with detailed error messages
- **Modular Architecture** with clean separation of concerns

## 📊 Available Tools

### Token Profile & Boost Tools (60 req/min)
- **`get_latest_token_profiles`** - Get the latest token profiles
- **`get_latest_boosted_tokens`** - Get the latest boosted tokens
- **`get_most_active_boosted_tokens`** - Get tokens with most active boosts
- **`check_token_orders`** - Check orders paid for a specific token

### Trading Pair Tools (300 req/min)
- **`get_pair_by_chain_and_address`** - Get specific pair data by chain and address
- **`search_pairs`** - Search for trading pairs by query
- **`get_token_pools`** - Get all pools for a specific token
- **`get_pairs_by_token`** - Get all pairs for a specific token

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Dependencies
```bash
pip install mcp aiohttp, httx, requests
```

### Quick Setup
```bash
# Clone or download the project
git clone <your-repo-url>
cd dexscreener-mcp

# Install dependencies
pip install 

# Run the MCP server
python main.py
```

## 📁 Project Structure

```
dexscreener-mcp/
├── README.md                       # README.md
├── requirements.txt                # Python dependencies
├── dexscreener_client.py          # Core API client
├── server.py                      # MCP server instance
├── main.py                        # Tool registration & server startup
└── tools/                         # MCP tools directory
    ├── __init__.py               # Tool exports and registration
    ├── get_latest_token_profiles.py
    ├── get_latest_boosted_tokens.py
    ├── get_most_active_boosted_tokens.py
    ├── check_token_orders.py
    ├── get_pair_by_chain_and_address.py
    ├── search_pairs.py
    ├── get_token_pools.py
    └── get_pairs_by_token.py
```

## ⚙️ Configuration

### Environment Variables
No environment variables are required by default. The server uses the public DexScreener API.

### Custom Configuration
You can modify the base URL in `dexscreener_client.py`:
```python
# Default: https://api.dexscreener.com
DexScreenerClient(base_url='https://api.dexscreener.com')
```

## 🔧 Usage

### Starting the Server
```bash
python main.py
```

The server will start and listen for MCP requests via stdio.

### Integration with AI Tools
This MCP server can be integrated with AI assistants that support the Model Context Protocol, such as Claude Desktop or other MCP-compatible tools.

## 📚 API Reference

### Token Profile Tools

#### `get_latest_token_profiles()`
Get the latest token profiles from DexScreener.
- **Rate Limit**: 60 requests per minute
- **Parameters**: None
- **Returns**: Latest token profile data

#### `get_latest_boosted_tokens()`
Get the latest boosted tokens.
- **Rate Limit**: 60 requests per minute
- **Parameters**: None
- **Returns**: Latest boosted token data
- **Note**: Large response size - use sparingly

#### `get_most_active_boosted_tokens()`
Get tokens with the most active boosts.
- **Rate Limit**: 60 requests per minute
- **Parameters**: None
- **Returns**: Most active boosted tokens
- **Note**: Large response size - use sparingly

#### `check_token_orders(chain_id, token_address)`
Check orders paid for a specific token.
- **Rate Limit**: 60 requests per minute
- **Parameters**:
  - `chain_id` (str): Chain ID (e.g., "solana", "ethereum", "bsc")
  - `token_address` (str): Token address
- **Returns**: Token order data

### Trading Pair Tools

#### `get_pair_by_chain_and_address(chain_id, pair_address)`
Get pair data by chain and pair address.
- **Rate Limit**: 300 requests per minute
- **Parameters**:
  - `chain_id` (str): Chain ID (e.g., "solana", "ethereum", "bsc")
  - `pair_address` (str): Pair address
- **Returns**: Specific pair data

#### `search_pairs(query)`
Search for trading pairs matching a query.
- **Rate Limit**: 300 requests per minute
- **Parameters**:
  - `query` (str): Search query (e.g., "SOL/USDC", "ETH")
- **Returns**: Matching pairs

#### `get_token_pools(chain_id, token_address)`
Get all pools for a specific token.
- **Rate Limit**: 300 requests per minute
- **Parameters**:
  - `chain_id` (str): Chain ID (e.g., "solana", "ethereum", "bsc")
  - `token_address` (str): Token address
- **Returns**: Token pool data

#### `get_pairs_by_token(chain_id, token_address)`
Get all pairs for a specific token.
- **Rate Limit**: 300 requests per minute
- **Parameters**:
  - `chain_id` (str): Chain ID (e.g., "solana", "ethereum", "bsc")
  - `token_address` (str): Token address
- **Returns**: Token pairs data

## 🌐 Supported Chains

Common chain IDs supported by DexScreener:
- `ethereum` - Ethereum mainnet
- `bsc` - Binance Smart Chain
- `polygon` - Polygon
- `solana` - Solana
- `arbitrum` - Arbitrum
- `optimism` - Optimism
- `avalanche` - Avalanche
- `fantom` - Fantom

## ⚠️ Rate Limits

**Token Profile & Boost Tools**: 60 requests per minute
- `get_latest_token_profiles`
- `get_latest_boosted_tokens`
- `get_most_active_boosted_tokens`
- `check_token_orders`

**Trading Pair Tools**: 300 requests per minute
- `get_pair_by_chain_and_address`
- `search_pairs`
- `get_token_pools`
- `get_pairs_by_token`

## 🛡️ Error Handling

The server includes comprehensive error handling:

- **Validation Errors**: Invalid parameters are caught before API calls
- **Network Errors**: HTTP errors are properly handled and logged
- **Rate Limiting**: API rate limit responses are handled gracefully
- **Timeout Errors**: Network timeouts are caught and reported

### Common Error Scenarios
1. **Invalid Chain ID**: Ensure chain ID is supported by DexScreener
2. **Invalid Token Address**: Verify token address format for the specific chain
3. **Rate Limit Exceeded**: Wait before making additional requests
4. **Network Issues**: Check internet connection and DexScreener API status

## 🔍 Debugging

### Enable Debug Logging
Modify the logging level in `main.py`:
```python
logging.basicConfig(level=logging.DEBUG)
```

### Common Issues

#### Tool Not Found
- Ensure all tools are imported in `tools/__init__.py`
- Check that `@mcp.tool()` decorators are present
- Verify `main.py` imports all tools

#### Import Errors
- Check Python path configuration
- Ensure all dependencies are installed
- Verify file structure matches documentation

#### API Errors
- Check DexScreener API status
- Verify network connectivity
- Ensure parameters match expected format

## 🧪 Development

### Adding New Tools
1. Create new tool file in `tools/` directory
2. Import server and add `@mcp.tool()` decorator
3. Add import to `tools/__init__.py`
4. Add import to `main.py`

### Example New Tool
```python
# tools/my_new_tool.py
import json
from server import mcp
from utils import make_request

@mcp.tool()
async def my_new_tool(param: str) -> list[types.TextContent]:
    """Description of what this tool does"""
    data = await make_request(f'/my/endpoint/{param}')
    return [types.TextContent(type="text", text=json.dumps(data, indent=2))]
```

### Testing
```python
# Test individual tools
import asyncio
from tools.search_pairs import search_pairs

async def test():
    result = await search_pairs("SOL/USDC")
    print(result)

asyncio.run(test())
```

## 📄 Requirements

Create a `requirements.txt` file:
```txt
mcp>=1.0.0
aiohttp>=3.9.0
httpx>=0.28.1
requests>=2.32.3
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 conventions
- Add type hints to all functions
- Include docstrings for all public functions
- Add error handling for all external API calls

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [DexScreener](https://dexscreener.com/) for providing the API
- [Anthropic](https://anthropic.com/) for the Model Context Protocol specification
- The Python async/await community for excellent async patterns

## 📞 Support

For issues and questions:
1. Check the [troubleshooting section](#-debugging)
2. Review [DexScreener API documentation](https://docs.dexscreener.com/)
3. Open an issue in this repository

---

**Built with ❤️ for the DeFi community**