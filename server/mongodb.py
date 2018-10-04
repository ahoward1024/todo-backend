from pymongo import MongoClient
from server import config
from server import constants


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
