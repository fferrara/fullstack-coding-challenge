from pymongo import MongoClient
import config

__author__ = 'Flavio Ferrara'


def get_db():
    """Initializes the database."""
    db_client = MongoClient(config.MONGO_HOST, config.MONGO_PORT)
    db = db_client[config.DATABASE]

    return db, db_client
