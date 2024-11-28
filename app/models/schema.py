from pydantic import BaseModel

class ImageSchema(BaseModel):
    id: str
    url:str
    title:str
    author:str
    created_utc: int