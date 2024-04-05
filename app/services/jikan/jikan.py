from typing import Dict, Any, List # , Optional, Union
from ...handlers import ApiHandler 

BASE: str = "https://api.jikan.moe/v4"
api: ApiHandler = ApiHandler(BASE)
top_animes_uri: str = "/top/anime"

async def get_top_animes() -> List[Dict[str, Any]]:
    data: Dict[str, Any] = await api.get(top_animes_uri, params={
        "limit": "25",
    })

    return data["data"]
