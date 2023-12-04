import time

import psycopg2
from fastapi import FastAPI, HTTPException, status
from psycopg2.extras import RealDictCursor

from src.schemas import Message, Post, PostDB, PostList, PostPublic, PostSchema

config = {
    'database': {
        'host': 'localhost',
        'user': 'postgres',
        'password': '148036',
        'database': 'fastapi',
        'port': 5432,
        'cursor_factory': RealDictCursor,
    }
}

connection_params = {
    'host': config['database']['host'],
    'user': config['database']['user'],
    'password': config['database']['password'],
    'database': config['database']['database'],
    'port': config['database']['port'],
    'cursor_factory': config['database']['cursor_factory'],
}

while True:
    try:
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()
        print('Database connection was sucessfull.')
        break
    except Exception as error:
        print('Connecting to database failed')
        print('Error: {error}')
        time.sleep(2)

app = FastAPI()


@app.post(
    '/posts/', status_code=status.HTTP_201_CREATED, response_model=PostPublic
)
def create_post(post: PostSchema):

    cursor.execute(
        """
        INSERT INTO posts (title, content, published) 
        VALUES
            (%s, %s, %s)
        RETURNING *            
        """,
        (post.title, post.content, post.published)
    )
    
    new_post = cursor.fetchone()

    return new_post


@app.get('/posts', response_model=PostList)
def get_posts():
    cursor.execute(
        """
        SELECT *
        FROM posts
        """
    )
    posts = cursor.fetchall()
    return {'posts': posts}


@app.get('/posts/{post_id}', response_model=Post)
def get_post(post_id: int):
    for post in my_posts:
        if post.id == post_id:
            return {'post': post}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'post with post_id {post_id} was not found',
        )


@app.put('/posts/{post_id}', response_model=PostPublic)
def update_post(post_id: int, post: PostSchema):
    if check_id(post_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Post with id {post_id} not found',
        )

    post_with_id = PostDB(**post.model_dump(), id=post_id)
    my_posts[post_id - 1] = post_with_id

    return post_with_id


@app.delete('/posts/{post_id}', response_model=Message)
def delete_post(post_id: int):
    if check_id(post_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Post with id {post_id} not found',
        )

    # post = my_posts[post_id - 1]

    del my_posts[post_id - 1]

    return {'detail': 'Post deleted'}


def check_id(post_id):
    return post_id > len(my_posts) or post_id < 1
