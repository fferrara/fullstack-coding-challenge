import collections
from pymongo import MongoClient
from app.entity.repository import StoryRepositoryMongo, TranslationRepositoryMongo
from app.entity.story import Story
from app.entity.translation import TitleTranslation

__author__ = 'Flavio Ferrara'

import unittest


class TranslationRepositoryTest(unittest.TestCase):
    def setUp(self):
        db_client = MongoClient()
        self.db = db_client.test_db
        self.repository = TranslationRepositoryMongo(self.db)
        self.collection = self.db.stories
        self.collection.drop()

        self.story = Story(**{
            "by": "dhouston",
            "descendants": 71,
            "id": 8863,
            "kids": [8952, 9224],
            "score": 111,
            "time": 1175714200,
            "title": "My YC app: Dropbox - Throw away your USB drive",
            "text": "<p>A wonderful story</p>",
            "type": "story",
            "url": "http://www.getdropbox.com/u/2/screencast.html",
        })

        self.t1 = TitleTranslation("5d10df62d3", "My YC app: Dropbox - Throw away your USB drive", "machine_translate_in_progress", "pt")

        self.t2 = TitleTranslation("5d10df62d4", "My YC app: Dropbox - Throw away your USB drive", "deliver_ok", "it",
                                   translatedText='Butta via il tuo USB drive')

        self.__insert_example_story()

    def test_find_all(self):
        translations = self.repository.find_all()

        assert translations is not None
        assert isinstance(translations, list)
        assert len(translations) == 2

        assert not translations[0].is_completed()
        assert translations[1].is_completed()

    def test_find_pending(self):
        translations = self.repository.find_pending()

        assert translations is not None
        assert isinstance(translations, list)
        assert len(translations) == 1

        assert not translations[0].is_completed()

    def test_save_translation(self):
        self.t1.complete_translation('Jogue fora seu USB drive')
        self.repository.save(self.t1)

        updated_story = self.collection.find_one({"_id": 8863})
        assert updated_story is not None
        assert len(updated_story['translations']) > 0
        translation = updated_story['translations'][0]
        assert translation['status'] == 'deliver_ok'
        assert translation['translatedText'] == 'Jogue fora seu USB drive'


    def __insert_example_story(self):
        self.story.add_translation(self.t1)
        self.story.add_translation(self.t2)
        doc = self.story.to_document()
        self.collection.insert_one(doc)
