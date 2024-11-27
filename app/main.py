from fastapi import FastAPI,HTTPException,Depends
from endpoint.router import reddit_router
from db.redis import get_redis_pool
from services.reddit_service import get_images_from_blursed
#from services.task import fetch_blursed_images

app = FastAPI()

app.include_router(reddit_router)

@app.post("/start-scraping")
async def start_scraping(redis=Depends(get_redis_pool)):
    try:
        # Fetch images and store them in Redis
        images = await get_images_from_blursed(redis)
        return {"message": "Scraping started!", "images": images}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))