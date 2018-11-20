from pymongo import MongoClient
from server import config
from server import constants

mongo_uri = config.auth[constants.MONGO_AUTH]
client = MongoClient(mongo_uri)
db = client[config.auth[constants.MONGO_DB_NAME]]
collection = db[config.auth[constants.MONGO_DB_COLLECTION]]
