from app.entity.hackernews import HackernewsItem

__author__ = 'Flavio Ferrara'

class Comment(HackernewsItem):
    def __init__(self, id, deleted, by, time, text, dead, kids, parent):
        super().__init__(id, deleted, by, time, text, dead, kids)
        self.parent = parent

