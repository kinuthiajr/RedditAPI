import os
import redis
from dotenv import load_dotenv

load_dotenv()

def get_redis_connection():
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    r = redis.Redis.from_url(redis_url, decode_responses=True)
    return r