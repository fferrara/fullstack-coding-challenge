from abc import ABC

__author__ = 'Flavio Ferrara'

class HackernewsItem(ABC):
    def __init__(self, id, deleted, by, time, text, dead, kids): 
        self.kids = kids
        self.dead = dead
        self.text = text
        self.time = time
        self.by = by
        self.deleted = deleted
        self.id = id
