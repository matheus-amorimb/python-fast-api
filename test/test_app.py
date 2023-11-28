from fastapi.testclient import TestClient

from src.main import app


def test_root_deve_retornar_200_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'hello world'}


def test_get_posts_deve_retornar_200_e_this_is_your_post():
    client = TestClient(app)

    response = client.get('/posts')

    assert response.status_code == 200
    assert response.json() == {'data': 'This is your post'}


def test_post_deve_retornar_200_e_new_post():
    client = TestClient(app)

    data = {
        'title': 'Minha primeira API',
        'content': 'Como foi minha primeira viagem',
        'published': 'True',
        'rating': '10',
    }

    response = client.post('/createposts', json=data)

    assert response.status_code == 200
    assert response.json() == {'data': 'new post'}
