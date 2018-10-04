import pytest
import json
from server.app import app


@pytest.fixture
def client(request):
    test_client = app.test_client()
    return test_client


def post_json(client, url, dict):
    return client.post(
        url, data=json.dumps(dict), content_type='application/json')


def put_json(client, url, dict):
    return client.put(
        url, data=json.dumps(dict), content_type='application/json')


def test_index(client):
    response = client.get('/')
    assert b'Hello' in response.data


def test_healthcheck(client):
    return client.get('/healthcheck').status_code == 200


"""
def test_todos_add(client):
    assert post_json(client, '/todos.add', {'text': 'asdf'}).status_code == 200


def test_todo_toggleall(client):
    assert put_json(
        client, '/todos.toggleall', {'completed': True}).status_code == 200


def test_todo_toggle(client):
    assert put_json(
        client, '/todos.toggle', {'id': '0', 'completed': False}
        ).status_code == 200


def test_todos_get(client):
    assert client.get('/todos.get').status_code == 200

"""
