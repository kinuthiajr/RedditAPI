import praw
import os
from dotenv import load_dotenv
from db.redis import get_redis_pool
import asyncio

load_dotenv()

# Access environment variables
client_id=os.getenv("REDDIT_CLIENT_ID")
client_secret=os.getenv("REDDIT_CLIENT_SECRET")
password=os.getenv("PASSWORD")
user_agent=os.getenv("REDDIT_USER_AGENT")
username=os.getenv("USERNAME")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent=user_agent,
    username=username,
)

async def get_images_from_blursed(redis):
    """
    Func fetches images from blursed community on Reddit
    - Works with already configured connection(PRAW - Python Reddit API Wrapper)
    - It requests the 10 newest posts from that subreddit.
    Returns a dict with complete image information.
    
    """
    images = []
    subreddit = reddit.subreddit("blursedimages")
    submissions = subreddit.new(limit=10)

    for submission in submissions:
        if submission.url.endswith(('jpg','jpeg','png')):
            image_data = {
                    "url":submission.url,
                    "title": submission.title,
                    "author": str(submission.author)
                    }
        images.append(image_data)

        await redis.set(f'image:{submission.id}', submission.url)
        
    return images