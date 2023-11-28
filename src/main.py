from typing import Optional

from fastapi import FastAPI

# from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get('/')
async def root():
    return {'message': 'hello world'}


@app.get('/posts')
def get_posts():
    return {'data': 'This is your post'}


@app.post('/createposts')
def create_posts(new_post: Post):
    print(new_post.model_dump())
    # print(new_post.title)
    # print(new_post.content)
    # print(new_post.published)
    return {'data': 'new post'}
