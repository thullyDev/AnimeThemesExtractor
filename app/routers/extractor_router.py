from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/extract")

@router.get("/start")
def start():
     return {"message": "extractor here"}
