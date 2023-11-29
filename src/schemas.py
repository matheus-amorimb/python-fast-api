from pydantic import BaseModel, EmailStr


class PostSchema(BaseModel):
    title: str
    content: str
    id: int = None
