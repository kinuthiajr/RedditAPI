from pydantic import BaseModel

class ImageResponse(BaseModel):
    url:str
    title:str
    author:str