from abc import ABC, abstractmethod
from app.entity.story import Story
from app.entity.translation import TitleTranslation

__author__ = 'Flavio Ferrara'


class Repository(ABC):
    def __init__(self, db):
        """

        :param Database db:
        """
        self.db = db

    @abstractmethod
    def save(self, entity):
        raise NotImplementedError

    @abstractmethod
    def find_all(self):
        raise NotImplementedError
    #
    # @abstractmethod
    # def find_one(self, entity_id):
    #     raise NotImplementedError

    @abstractmethod
    def update(self, entity):
        raise NotImplementedError


class StoryRepositoryMongo(Repository):
    def __init__(self, db):
        super().__init__(db)
        self.collection = self.db.stories

    def find_all(self):
        results = self.collection.find({})
        return [Story.from_document(**result) for result in results]

    def find_one(self, entity_id):
        result = self.collection.find_one({'_id': entity_id})

        if result is not None:
            return Story.from_document(**result)
        return None

    def save(self, story):
        story_dict = story.to_document()
        story_dict['_id'] = story.id
        self.collection.update({'_uid': story.id}, story_dict, upsert=True)
        return story

    def update(self, entity):
        pass


class TranslationRepositoryMongo(Repository):
    def __init__(self, db):
        super().__init__(db)
        self.collection = self.db.translations

    def find_all(self):
        results = self.collection.find({})
        print(results.count())
        return [TitleTranslation(**result) for result in results]

    def save(self, translation):
        print('Save translation')
        translation_dict = translation.__dict__
        translation_dict['_id'] = translation.uid
        translation = self.collection.insert_one(translation_dict)
        return translation.inserted_id

    def update(self, entity):
        pass
