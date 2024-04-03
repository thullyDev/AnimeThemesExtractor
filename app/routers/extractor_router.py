from fastapi import APIRouter
from typing import Any, Dict

router = APIRouter(prefix="/extract")

@router.get("/start")
def start() -> Dict[str, str]:
     return {"message": "extractor here"}
