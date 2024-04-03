from typing import Any, Dict, Union
from app.handlers.json_handler import JsonHandler

jhandler = JsonHandler(
        FILENAME="cache",
        DIR="JSONs",
    )

class Cache():
    _instance: Any = False
    
    def __new__(cls) -> 'Cache':
        if not cls._instance:
            cls._instance = super(Cache, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        data: Union[Dict[str, Any], None] = jhandler.get()

        if data == None:
            data  = {}

        self.cache_hashmap: Dict[str, Any] = data

    def update(self, key: str, data: Dict[str, Any]) -> None:
        old_data: Dict[str, Any] = self.get(key, {})
        for key, val in data.items():
            old_data[key] = val
        self.set(key, old_data)

    def set(self, key: str, data: Any) -> None:
        self.cache_hashmap[key] = data
        self.save()

    def get(self, key: str, default: Any = None) -> Any:
        return self.cache_hashmap.get(key, default)

    def delete(self, key: str) -> None:
        del self.cache_hashmap[key]
        self.save()

    def save(self) -> None:
        jhandler.set(data=self.cache_hashmap)
