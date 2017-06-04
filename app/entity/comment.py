from app.entity.hackernews import HackernewsItem

__author__ = 'Flavio Ferrara'


class Comment(HackernewsItem):
    def __init__(self, id, by, time, text, parent, kids=None, **kwargs):
        super().__init__(id, by, time, text, kids)
        self.parent = parent

    def to_document(self):
        return self.__dict__

    @classmethod
    def from_document(cls, id, by, time, text, parent, kids=None, **kwargs):
        return Comment(id, by, time, text, parent, kids)

