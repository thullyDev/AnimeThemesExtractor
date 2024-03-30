from fastapi import FastAPI
from .routers import extractor_router

app = FastAPI()

@app.get("/")
def root():
    return {"Message": "bot is running... follow me on https://github.com/thullDev"}

app.include_router(extractor_router.router)
