import json
from server.db import (
    get_todos,
    add_todo,
    toggle_todo,
    toggle_all,
    toggle_checkall
)


with open('tests/db/todo.json') as json_data:
    mock_collection = json.load(json_data)
    json_data.close()


def test_get_todos(mongodb):
    assert 'todo' in mongodb.collection_names()
    todos = get_todos(mongodb.todo)
    assert todos == mock_collection


def test_get_todos_no_checkall(mongodb):
    assert 'todonocheckall' in mongodb.collection_names()
    get_todos(mongodb.todonocheckall)
    checkall = mongodb.todonocheckall.find_one({'id': 'checkall'})
    assert checkall['completed'] is False


def test_add_todo(mongodb):
    assert 'todo' in mongodb.collection_names()
    input = {'text': 'testing'}
    mock_todo = {'text': 'testing', 'completed': False}
    dict = add_todo(mongodb.todo, input)
    assert dict['text'] == mock_todo['text']
    assert dict['completed'] == mock_todo['completed']


def test_toggle_todo(mongodb):
    assert 'todo' in mongodb.collection_names()
    mock_todo = {
        'text': 'asdf',
        'id': '0',
        'completed': True,
        'time': '2018-10-01 00:00:00.000000'
    }
    mock_request = {'id': '0', 'completed': False}
    dict = toggle_todo(mongodb.todo, mock_request)
    assert dict['completed'] is False
    assert dict['id'] == mock_todo['id']


def test_toggle_all(mongodb):
    assert 'todo' in mongodb.collection_names()
    mock_request = {'completed': False}
    dict = toggle_all(mongodb.todo, mock_request)
    assert dict['completed'] is False


def test_toggle_checkall(mongodb):
    assert 'todo' in mongodb.collection_names()
    toggle_checkall(mongodb.todo, True)
    checkall = mongodb.todo.find_one({'id': 'checkall'})
    assert checkall['completed'] is True
