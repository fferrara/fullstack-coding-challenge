from flask.helpers import url_for
from app.pages import stories
from flask import Flask, redirect, g

__author__ = 'Flavio Ferrara'


def create_app(config=None):
    app = Flask('raquer_news')

    app.config.update(dict(
        DEBUG=True,
        DATABASE='test_db',
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='default'
    ))
    app.config.update(config or {})

    register_blueprints(app)
    register_teardowns(app)

    return app


def register_blueprints(app):
    """Register all blueprint modules
    """
    # app.register_blueprint(dashboard)
    app.register_blueprint(stories.stories_bp)

    @app.route('/')
    def index():
        return redirect(url_for('stories.index'))

    return None


def register_teardowns(app):
    @app.teardown_appcontext
    def close_db(error):
        """Closes the database again at the end of the request."""
        if hasattr(g, 'db_client'):
            print('Closed')
            g.db_client.close()

