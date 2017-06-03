from flask import Blueprint, render_template

__author__ = 'Flavio Ferrara'

stories_bp = Blueprint('stories', __name__, url_prefix='/stories')

@stories_bp.route('/')
def index():
    return render_template('stories/index.html')
