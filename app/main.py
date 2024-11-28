from fastapi import FastAPI, HTTPException, Depends
from endpoint.router import reddit_router
from db.redis import get_redis_connection
from services.reddit_service import get_images_from_blursed

app = FastAPI()

app.include_router(reddit_router)

@app.post("/start-scraping")
def start_scraping(redis=Depends(get_redis_connection)):
    try:
        #Fetch images and store them in Redis
        images = get_images_from_blursed(redis)
        return {"message": "Scraping started!", "images": images}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))