from abc import ABC, abstractmethod
from app.entity.story import Story
from app.entity.translation import TitleTranslation, TranslationStatus

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
        # raise NotImplementedError


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
        self.collection.update({'_id': story.id}, {'$set': story_dict}, upsert=True)
        return story

    def update(self, story):
        story_dict = story.to_document()
        self.collection.update({'_id': story.id}, {'$set': story_dict})
        return story


class TranslationRepositoryMongo(Repository):
    def __init__(self, db):
        super().__init__(db)
        self.collection = self.db.stories

    def find_all(self):
        stories = self.collection.find({}, {'translations': 1})
        translations = []
        for story in stories:
            translations += [TitleTranslation(**t) for t in story['translations']]

        return translations

    def find_pending(self):
        stories = self._find_by_pending_translations()
        translations = []
        for story in stories:
            translations += [TitleTranslation(**t) for t in story['translations']
                             if t['status'] == TranslationStatus.PENDING]

        return translations

    def save(self, translation):
        story_doc = self._find_by_translation(translation.uid)
        if story_doc is None:
            raise ValueError('Translation not found')

        story_doc['translations'] = [translation.to_document()
                                     if translation.uid == t['uid'] else t
                                     for t in story_doc['translations']]

        self.collection.update({'_id': story_doc['_id']}, {'$set': story_doc})

    def _find_by_translation(self, translation_uid):
        return self.collection.find_one({
            'translations': {
                '$elemMatch': {'uid': translation_uid}
            }
        })

    def _find_by_pending_translations(self):
        query = {'translations':
                     {'$elemMatch':
                          {'status': TranslationStatus.PENDING}
                     }
        }
        return self.collection.find(query, {'translations': 1})
