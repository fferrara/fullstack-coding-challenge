from app.entity.comment import Comment
from app.entity.hackernews import HackernewsItem

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

    @property
    def title(self, language='pt'):
        return self.original_title

    def add_translation(self, translation):
        pass

    def to_document(self):
        doc = self.__dict__.copy()
        doc['comments'] = [c.to_document() for c in self.comments]
        doc['translations'] = [t.to_document() for t in self.translations]

        return doc

    @classmethod
    def from_document(cls, id, by, time, url, score, original_title, descendants, text='', kids=None, comments=None, **kwargs):
        s = Story(id, by, time, url, score, original_title, descendants, text, kids)

        if comments is not None:
            for comment in comments:
                s.comments.append(Comment.from_document(**comment))

        return s
