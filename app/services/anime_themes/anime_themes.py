from typing import Dict, Any, List # , Optional, Union
from ...handlers import ApiHandler 

BASE: str = "https://api.animethemes.moe"
api: ApiHandler = ApiHandler(BASE)
animes_uri: str = "/anime"

async def get_animes(filter_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    filter_data["include"] = "animethemes.animethemeentries.videos"
    data: Dict[str, Any] = await api.get(animes_uri, params=filter_data)

    return data["anime"]
