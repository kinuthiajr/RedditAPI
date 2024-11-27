from pydantic import BaseModel

class ImageSchema(BaseModel):
    url:str
    title:str
    author:str