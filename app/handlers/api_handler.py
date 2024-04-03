import aiohttp
from typing import Any, Dict, Optional

class ApiHandler:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def request(self, endpoint: str, method: str = 'GET', **kwargs: Any) -> Dict[str, Any]:
        url = self.base_url + endpoint
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, **kwargs) as response:
                response.raise_for_status()
                return await response.json()

    async def get(self, endpoint: str, params: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
        return await self.request(endpoint, params=params, method='GET')

    async def post(self, endpoint: str, data: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
        return await self.request(endpoint, data=data, method='POST')

    async def put(self, endpoint: str, data: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
        return await self.request(endpoint, data=data, method='PUT')

    async def delete(self, endpoint: str, **kwargs: Any) -> Dict[str, Any]:
        return await self.request(endpoint, method='DELETE')