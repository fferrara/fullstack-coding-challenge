from abc import ABC

__author__ = 'Flavio Ferrara'

class HackernewsItem(ABC):
    def __init__(self, id, by, time, text, kids):
        self.kids = kids or []
        self.text = text
        self.time = time
        self.by = by
        self.id = id

    def has_comments(self):
        return len(self.kids) > 0
