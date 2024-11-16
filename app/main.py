from fastapi import FastAPI
from endpoint.router import reddit_router

app = FastAPI()

app.include_router(reddit_router)
