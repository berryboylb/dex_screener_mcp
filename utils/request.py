import httpx
import requests

BASE_URL = "https://api.dexscreener.com"


async def make_request(endpoint: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{BASE_URL}{endpoint}")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            print(f"Error making request to {endpoint}: {str(e)}")
            raise RuntimeError(f"Failed to fetch data from DexScreener API: {str(e)}")


def make_request_sync(endpoint: str):
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error making request to {endpoint}: {str(e)}")
        raise RuntimeError(f"Failed to fetch data from DexScreener API: {str(e)}")
