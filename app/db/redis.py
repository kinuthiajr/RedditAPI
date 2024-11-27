import os
from aioredis import Redis, from_url
from typing import AsyncIterator
from dotenv import load_dotenv

load_dotenv()

async def get_redis_pool() -> AsyncIterator[Redis]:
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")  
    redis = await from_url(redis_url, encoding="utf-8", decode_responses=True)
    try:
        yield redis
    finally:
        await redis.close()