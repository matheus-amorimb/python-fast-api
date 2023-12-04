from datetime import datetime

from pydantic import BaseModel


class PostSchema(BaseModel):
    title: str
    content: str
    published: bool


class PostPublic(BaseModel):
    title: str
    content: str
    published: bool


class PostDB(PostSchema):
    id: int
    created_at: datetime


class Message(BaseModel):
    detail: str


class PostList(BaseModel):
    posts: list[PostPublic]


class Post(BaseModel):
    post: PostPublic
