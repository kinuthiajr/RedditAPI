from fastapi import APIRouter,HTTPException,Depends
from models.schema import ImageSchema
from services.reddit_service import get_images_from_blursed
from db.redis import get_redis_connection

reddit_router = APIRouter()

@reddit_router.get("/fetch/blursed",response_model=list[ImageSchema])
def get_blursed_images(redis=Depends(get_redis_connection)):
    try:
        images =get_images_from_blursed(redis)
        return images
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))