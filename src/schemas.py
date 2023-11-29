from pydantic import BaseModel


class PostSchema(BaseModel):
    title: str
    content: str
    password: str


class PostPublic(BaseModel):
    title: str
    content: str


class PostDB(PostSchema):
    id: int


class Message(BaseModel):
    detail: str


class PostList(BaseModel):
    posts: list[PostPublic]
