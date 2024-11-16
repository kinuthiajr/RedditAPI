from celery_config import celery_app
from .reddit_service import get_images_from_blursed

@celery_app.task
def fetch_blursed_images():
    images = get_images_from_blursed()
    return images