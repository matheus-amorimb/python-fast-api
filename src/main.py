import random

from fastapi import FastAPI

from src.schemas import PostSchema

app = FastAPI()

my_posts = [
    {'title': 'title of post 1', 'content': 'content of post 1', 'id': 1},
    {'title': 'title of post 2', 'content': 'content of post 2', 'id': 2},
]


@app.get('/')
def root():
    return {'message': 'hello world'}


@app.post('/posts')
def create_post(post: PostSchema):
    post_dict = post.model_dump()
    post_dict['id'] = random.randrange(1, 10000001)
    my_posts.append(post_dict)
    return {'data': post_dict}


@app.get('/posts')
def get_posts():
    return {'data': my_posts}


@app.get('/posts/{id}')
def get_post(id):
    for post in my_posts:
        if post['id'] == int(id):
            return {'data': post}
    else:
        return {'data': None}