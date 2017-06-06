from app.entity.comment import Comment
from app.entity.hackernews import HackernewsItem
from app.entity.translation import TitleTranslation

__author__ = 'Flavio Ferrara'


class Story(HackernewsItem):
    def __init__(self, id, by, time, url, score, title, descendants, text='', kids=None, **kwargs):
        super().__init__(id, by, time, text, kids)
        self.descendants = descendants
        self.original_title = title
        self.score = score
        self.url = url
        self.translations = []
        self.comments = []

    def get_title(self, language):
        if not self.translations:
            return self.original_title

        try:
            translation = next(t for t in self.translations if t.target_language == language and t.is_completed())
            return translation.translatedText
        except StopIteration:
            return self.original_title

    def add_translation(self, translation):
        self.translations.append(translation)

    def to_document(self):
        doc = self.__dict__.copy()
        doc['comments'] = self.comments and [c.to_document() for c in self.comments]
        doc['translations'] = self.translations and [t.to_document() for t in self.translations] or None
        doc['_id'] = self.id

        if not self.comments:
            del doc['comments']
        if not self.translations:
            del doc['translations']

        return doc

    @classmethod
    def from_document(cls, id, by, time, url, score, original_title, descendants, text='', kids=None,
                      comments=None, translations=None, **kwargs):
        s = Story(id, by, time, url, score, original_title, descendants, text, kids)

        if comments is not None:
            for comment in comments:
                s.comments.append(Comment.from_document(**comment))

        if translations is not None:
            for translation in translations:
                s.translations.append(TitleTranslation(**translation))

        return s
