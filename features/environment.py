from app.factory import create_app

__author__ = 'Flavio Ferrara'

def before_feature(context, feature):
    app = create_app()
    app.config['TESTING'] = True
    context.client = app.test_client()
