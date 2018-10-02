import constants
import os

auth = {
    constants.MONGO_USER: os.environ[constants.MONGO_USER],
    constants.MONGO_PASS: os.environ[constants.MONGO_PASS],
    constants.MONGO_DOMAIN: os.environ[constants.MONGO_DOMAIN],
    constants.MONGO_PORT: int(os.environ[constants.MONGO_PORT]),
    constants.MONGO_HEROKU: os.environ[constants.MONGO_HEROKU],
    constants.MONGO_DB_NAME: os.environ[constants.MONGO_DB_NAME],
    constants.MONGO_DB_COLLECTION: os.environ[constants.MONGO_DB_COLLECTION]
}
