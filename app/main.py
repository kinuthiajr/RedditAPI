from fastapi import FastAPI, HTTPException, Depends,BackgroundTasks
from endpoint.router import reddit_router
from db.redis import get_redis_connection
from services.reddit_service import get_images_from_blursed

app = FastAPI()

app.include_router(reddit_router)

def run_background_task(redis):
    """
    Background task to run the scraping process.
    """
    try:
        get_images_from_blursed(redis)
    except Exception as e:
        print(f"Error during scraping: {str(e)}")



@app.post("/start-scraping")
def start_scraping(background_tasks:BackgroundTasks,redis=Depends(get_redis_connection)):
    background_tasks.add_task(run_background_task, redis)
    return {"message": "Scraping started!"}