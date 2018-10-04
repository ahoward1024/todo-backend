import uuid
import datetime


def get_todos(collection):
    count = collection.count_documents({'id': 'checkall'})
    if (count == 0):
        collection.insert_one({'id': 'checkall', 'completed': False})
    todos = []
    for todo in collection.find():
        del todo['_id']
        todos += [todo]
    return todos


def add_todo(collection, dict):
    dict['id'] = uuid.uuid4().hex
    dict['completed'] = False
    dict['time'] = str(datetime.datetime.now())
    collection.insert_one(dict)
    toggle_checkall(collection, False)
    del dict['_id']
    return dict


def toggle_todo(collection, dict):
    completed = dict['completed']
    id = dict['id']
    collection.update_one({'id': id}, {'$set': {'completed': completed}})
    return dict


def toggle_all(collection, dict):
    completed = dict['completed']
    toggle_checkall(collection, completed)
    collection.update_many({}, {'$set': {'completed': completed}})
    return dict


def toggle_checkall(collection, completed):
    collection.update_one({'id': 'checkall'},
                          {'$set': {'completed': completed}})
