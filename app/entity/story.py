from app.entity.hackernews import HackernewsItem

__author__ = 'Flavio Ferrara'

class Story(HackernewsItem):
    def __init__(self, id, deleted, by, time, text, dead, kids, url, score, title, descendants):
        super().__init__(id, deleted, by, time, text, dead, kids)
        self.descendants = descendants
        self.title = title
        self.score = score
        self.url = url
        self.translations = []

    @property
    def title(self, language):
        pass

    def add_translation(self, translation):
        pass
