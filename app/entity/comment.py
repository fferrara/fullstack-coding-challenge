from app.entity.hackernews import HackernewsItem

__author__ = 'Flavio Ferrara'


class Comment(HackernewsItem):
    def __init__(self, id, by, time, text, parent, kids=None, **kwargs):
        super().__init__(id, by, time, text, kids)
        self.parent = parent
        self.comments = []

    def to_document(self):
        doc = self.__dict__
        doc['comments'] = [c.to_document() for c in self.comments]
        return doc

    @classmethod
    def from_document(cls, id, by, time, text, parent, kids=None, comments=None, **kwargs):
        c = Comment(id, by, time, text, parent, kids)

        if comments is not None:
            for comment in comments:
                c.comments.append(Comment.from_document(**comment))

        return c

