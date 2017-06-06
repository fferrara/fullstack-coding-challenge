from app.entity.repository import TranslationRepositoryMongo

__author__ = 'Flavio Ferrara'

from flask import Blueprint, current_app, render_template, g
from app.db import get_db

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
def index():
    g.db, g.db_client = get_db()
    repository = TranslationRepositoryMongo(g.db)
    translations = repository.find_all()
    return render_template('dashboard/index.html', translations=translations)
