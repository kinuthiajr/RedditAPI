import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

celery_app = Celery(
    "reddit_scraper",
    broker=os.getenv("REDIS_URL"),
    backend=os.getenv("REDIS_URL")
)

