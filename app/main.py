from fastapi import FastAPI,HTTPException
from endpoint.router import reddit_router
from services.task import fetch_blursed_images

app = FastAPI()

app.include_router(reddit_router)

@app.post("/start-scraping")
async def start_scraping():
    try:
        fetch_blursed_images.delay()  # Trigger the Celery task asynchronously
        return {"message": "Scraping started!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))