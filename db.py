from pymongo import MongoClient
import config
import constants
import uuid
import datetime

user = config.auth[constants.MONGO_USER]
passw = config.auth[constants.MONGO_PASS]
domain = config.auth[constants.MONGO_DOMAIN]
port = config.auth[constants.MONGO_PORT]
heroku = config.auth[constants.MONGO_HEROKU]
mongo_uri = 'mongodb://{}:{}@{}:{}/{}'.format(
    user, passw, domain, port, heroku)
client = MongoClient(mongo_uri)
db = client[config.auth[constants.MONGO_DB_NAME]]
collection = db[config.auth[constants.MONGO_DB_COLLECTION]]


def get_todos():
    cursor = collection.find({'checkall': {'$exists': True}}).limit(1)
    if (cursor.count() == 0):
        collection.insert_one({'id': 'checkall', 'completed': False})
    todos = []
    for todo in collection.find():
        del todo['_id']
        todos += [todo]
    return todos


def add_todo(dict):
    dict['id'] = uuid.uuid4().hex
    dict['completed'] = False
    dict['time'] = str(datetime.datetime.now())
    collection.insert_one(dict)
    toggle_checkall(False)
    del dict['_id']
    return dict


def toggle_todo(dict):
    completed = dict['completed']
    id = dict['id']
    collection.update_one({'id': id}, {'$set': {'completed': completed}})
    return dict


def toggle_todo_all(dict):
    completed = dict['completed']
    toggle_checkall(completed)
    collection.update_many({}, {'$set': {'completed': completed}})
    return dict


def toggle_checkall(completed):
    collection.update_one({'id': 'checkall'},
                          {'$set': {'completed': completed}})


def drop_db():
    client.drop_database(db)
