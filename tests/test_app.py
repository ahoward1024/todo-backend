import pytest
from server.app import app


@pytest.fixture
def client(request):
    test_client = app.test_client()
    return test_client


def test_index(client):
    response = client.get('/')
    assert b'Hello' in response.data


def test_healthcheck(client):
    return client.get('/healthcheck').status_code == 200
