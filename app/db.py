from pymongo import MongoClient

__author__ = 'Flavio Ferrara'


def get_db(app):
    """Initializes the database."""
    db_client = MongoClient('localhost', 27017)
    db = db_client[app.config['DATABASE']]

    return db, db_client
