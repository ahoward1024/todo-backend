from pymongo import MongoClient
import config
import constants

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
    todos = []
    for todo in collection.find():
        todos += [todo]
    return todos


def add_todo(dict):
    print(dict)
    dict['_id'] = dict['todo']['id']
    collection.insert_one(dict)


def toggle_todo(dict):
    print(dict)
    completed = dict['completed']
    id = int(dict['id'])
    collection.update_one({'_id': id}, {'$set': {'todo.completed': completed}})


def toggle_todo_all(dict):
    completed = dict['completed']
    ret = collection.update_one(
        {'_id': 'checkall'}, {'$set': {'checkall': completed}})
    if(ret.matched_count == 0):
        collection.insert_one({'_id': 'checkall', 'checkall': completed})
    collection.update_many({}, {'$set': {'todo.completed': completed}})


def set_checkall(dict):
    id = 'checkall'
    checkall = dict['checkall']
    collection.update_one({'_id': id}, {'$set': {'checkall': checkall}})


def drop_db():
    client.drop_database(db)
