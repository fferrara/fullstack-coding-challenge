from flask import Blueprint, render_template, g, current_app, request
from app.db import get_db
from app.entity.repository import StoryRepositoryMongo

__author__ = 'Flavio Ferrara'

stories_bp = Blueprint('stories', __name__, url_prefix='/stories')

@stories_bp.route('/')
def index():
    g.db, g.db_client = get_db(current_app)
    repository = StoryRepositoryMongo(g.db)
    stories = repository.find_all()

    language = request.args.get('lang', 'pt')
    return render_template('stories/index.html', stories=stories, language=language)
