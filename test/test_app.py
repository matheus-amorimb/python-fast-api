import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_create_post(client):
    data = {
        'title': 'Minha primeira API',
        'content': 'Como foi construir minha primeira API',
        'password': 'abcd',
    }

    response = client.post('/posts/', json=data)

    assert response.status_code == 201
    assert response.json() == {
        'title': 'Minha primeira API',
        'content': 'Como foi construir minha primeira API',
    }


def test_get_posts(client):
    response = client.get('/posts')

    assert response.status_code == 200
    assert response.json() == {
        'posts': [
            {
                'title': 'Minha primeira API',
                'content': 'Como foi construir minha primeira API',
            }
        ]
    }


def test_put_post(client):
    data = {
        'title': 'Minha primeira FastAPI',
        'content': 'Como foi construir minha primeira FastAPI',
        'password': 'abcde',
    }

    response = client.put('/posts/1', json=data)

    assert response.status_code == 200
    assert response.json() == {
        'title': 'Minha primeira FastAPI',
        'content': 'Como foi construir minha primeira FastAPI',
    }


def test_delete_post(client):
    response = client.delete('/posts/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'Post deleted'}
