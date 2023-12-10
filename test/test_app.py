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
        'published': True,
    }

    response = client.post('/posts/', json=data)

    assert response.status_code == 201
    assert response.json() == {
        'title': 'Minha primeira API',
        'content': 'Como foi construir minha primeira API',
        'published': True,
    }


def test_get_posts(client):
    response = client.get('/posts')

    assert response.status_code == 200
    result = response.json()['posts'][-1]
    assert result == {
        'title': 'Minha primeira API',
        'content': 'Como foi construir minha primeira API',
        'published': True,
    }


def test_get_post(client):
    response = client.get('/posts/2')

    assert response.status_code == 200
    result = response.json()
    assert result == {
        'post': {
            'title': 'Web Development Fundamentals',
            'content': 'Building a strong foundation',
            'published': False,
        }
    }


def test_put_post(client):
    data = {
        'title': 'Minha primeira API',
        'content': 'Como foi construir minha primeira FastAPI',
        'published': True,
    }

    response = client.put('/posts/39', json=data)

    assert response.status_code == 200
    assert response.json() == {
        'title': 'Minha primeira API',
        'content': 'Como foi construir minha primeira FastAPI',
        'published': True,
    }


def test_delete_post(client):
    response = client.delete('/posts/39')

    assert response.status_code == 200
    assert response.json() == {'detail': 'Post deleted'}
