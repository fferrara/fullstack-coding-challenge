from pymongo import MongoClient
from flask import g

__author__ = 'Flavio Ferrara'


def connect_db():
    """Connects to the specific database."""
    db_client = MongoClient('localhost', 27017)
    return db_client


def init_db(app):
    """Initializes the database."""
    db_client = connect_db()
    db = db_client[app.config['DATABASE']]

    return db, db_client
