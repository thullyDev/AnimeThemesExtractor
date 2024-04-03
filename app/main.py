from fastapi import FastAPI
from .routers import extractor_router
from typing import Any, Dict

app = FastAPI()

@app.get("/")
def root() -> Dict[str, str]:
    return {"Message": "bot is running... follow me on https://github.com/thullDev"}

app.include_router(extractor_router.router)
