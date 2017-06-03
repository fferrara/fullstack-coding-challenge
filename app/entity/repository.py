from abc import ABC
from app.entity.story import Story

__author__ = 'Flavio Ferrara'


class Repository(ABC):
    def add(self, entity):
        raise NotImplementedError

    def find_all(self):
        raise NotImplementedError

    def find_one(self, entity_id):
        raise NotImplementedError


class StoryRepositoryMongo(Repository):
    def __init__(self, db):
        """

        :param Database db_client:
        """
        self.db = db  # Database
        self.collection = db.stories

    def find_all(self):
        results = self.collection.find({})
        return [Story(**result) for result in results]

    def find_one(self, entity_id):
        result = self.collection.find_one({'_id': entity_id})
        return Story(**result)

    def add(self, story):
        story_dict = story.__dict__
        story_dict['_id'] = story.id
        story = self.collection.insert_one(story_dict)
        return story.inserted_id

    def update(self, entity):
        pass
