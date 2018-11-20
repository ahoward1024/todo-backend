import os
from server import constants

auth = {
    constants.MONGO_DB_NAME: os.environ[constants.MONGO_DB_NAME],
    constants.MONGO_DB_COLLECTION: os.environ[constants.MONGO_DB_COLLECTION],
    constants.MONGO_AUTH: os.environ[constants.MONGO_AUTH]
}
