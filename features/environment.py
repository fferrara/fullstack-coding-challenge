from app.factory import create_app
import os
from bson import json_util

__author__ = 'Flavio Ferrara'


def before_feature(context, feature):
    app = create_app()
    app.config['TESTING'] = True
    context.client = app.test_client()


def fill_db(db):
    db.stories.drop()
    with open(os.path.join(os.path.dirname(__file__), 'sample_db.json'), 'r', encoding='utf8') as db_file:
        try:
            data = json_util.loads(db_file.read())
            for record in data:
                db.stories.insert_one(record)
        except Exception as e:
            print(e)
