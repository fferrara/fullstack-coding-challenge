from pymongo import MongoClient
from app.entity.repository import StoryRepositoryMongo
from app.entity.story import Story
from app.entity.translation import TitleTranslation

__author__ = 'Flavio Ferrara'

import unittest


class StoryRepositoryTest(unittest.TestCase):
    def setUp(self):
        db_client = MongoClient()
        self.db = db_client.test_db
        self.repository = StoryRepositoryMongo(self.db)
        self.collection = self.db.stories
        self.collection.drop()

        self.story_data = {
            "by": "dhouston",
            "descendants": 71,
            "id": 8863,
            "kids": [8952, 9224],
            "score": 111,
            "time": 1175714200,
            "title": "My YC app: Dropbox - Throw away your USB drive",
            "text": "<p>A wonderful story</p>",
            "type": "story",
            "url": "http://www.getdropbox.com/u/2/screencast.html"
        }

        self.translation_data = {
            "status": "new",
            "target_language": "pt",
            "uid": "5d10df62d3"
        }

    def test_new_story(self):
        story = Story(**self.story_data)

        self.repository.save(story)

        # testing
        added_story = self.collection.find_one({"_id": 8863})
        assert added_story is not None
        assert added_story['_id'] == 8863

    def test_get_all_stories(self):
        # setup
        self.__insert_example_story()

        # method call
        stories = self.repository.find_all()

        # testing
        assert stories is not None
        assert len(stories) == 1

        first_story = stories[0]
        assert isinstance(first_story, Story), True
        assert first_story.id == 8863

    def test_put_translation(self):
        # setup
        self.__insert_example_story()
        translation = TitleTranslation(**self.translation_data)


        # method call
        story = self.repository.find_one(8863)
        story.add_translation(translation)
        self.repository.update(story)

        # testing
        updated_story = self.collection.find_one({"_id": 8863})
        assert updated_story is not None
        print(updated_story)

    def __insert_example_story(self):
        self.story_data['_id'] = 8863
        self.collection.insert_one(self.story_data)
