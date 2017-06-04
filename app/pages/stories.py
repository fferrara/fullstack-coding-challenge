from flask import Blueprint, render_template, g, current_app
from app.db import get_db
from app.service.story import StoryService

__author__ = 'Flavio Ferrara'

stories_bp = Blueprint('stories', __name__, url_prefix='/stories')

@stories_bp.route('/')
def index():
    g.db, g.db_client = get_db(current_app)
    service = StoryService(g.db)
    stories = service.get_stories()
    return render_template('stories/index.html', stories=stories)
