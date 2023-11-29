from fastapi import FastAPI, HTTPException, status

from src.schemas import Message, Post, PostDB, PostList, PostPublic, PostSchema

app = FastAPI()

my_posts = []


@app.post(
    '/posts/', status_code=status.HTTP_201_CREATED, response_model=PostPublic
)
def create_post(post: PostSchema):

    post_with_id = PostDB(**post.model_dump(), id=len(my_posts) + 1)

    my_posts.append(post_with_id)

    return post_with_id


@app.get('/posts', response_model=PostList)
def get_posts():
    return {'posts': my_posts}


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
