import json
import os
from typing import Any, Dict, Union

current_dir: str = os.path.dirname(os.path.abspath(__file__))
BASE_DIR: str = os.path.dirname(os.path.dirname(current_dir))

class JsonHandler:
    def __init__(self, *, FILENAME: str, DIR: str, in_root_dir: bool = True) -> None:
        if in_root_dir == True:
            self._DIR = os.path.join(BASE_DIR, DIR) 
        else:
            self._DIR = DIR
            
        self._FILENAME = FILENAME
        self._create_dir_file()

    def _get_path(self) -> str:
        return os.path.join(self._DIR, f"{self._FILENAME}.json")

    def _dump_data(self, data: Dict[str, Any], *, _path: str) -> None:
        with open(_path, 'w') as file:
            json.dump(data, file)

    def _load_data(self, *, _path: str) -> Union[Dict[str, Any], None]:
        if not os.path.exists(_path): return None

        with open(_path, 'r') as file:
            return json.load(file)

    def _create_dir_file(self) -> None:
        _path:str = self._get_path()
        if os.path.exists(_path): return None 

        self._dump_data(data={}, _path=_path)

    def set(self, data: Any) -> None:
        _path = self._get_path()
        self._dump_data(data, _path=_path)

    def get(self) -> Union[Dict[str, Any], None]:
        _path = self._get_path()
        return self._load_data(_path=_path)

    def delete(self, key: str) -> None:
        _path = self._get_path()
        if not os.path.exists(_path): return

        os.remove(_path)

