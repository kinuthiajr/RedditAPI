from fastapi import APIRouter,HTTPException
from models.models import ImageResponse
from services.reddit_service import get_images_from_blursed

reddit_router = APIRouter()

@reddit_router.get("/fetch/blursed",response_model=list[ImageResponse])
async def get_blursed_images():
    try:
        images =get_images_from_blursed()
        return images
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))