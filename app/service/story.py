__author__ = 'Flavio Ferrara'

from app.entity.repository import StoryRepositoryMongo


class StoryService:
    def __init__(self, db):
        self.repository = StoryRepositoryMongo(db)

    def get_stories(self):
        return self.repository.find_all()
