from app.entity.hackernews import HackernewsItem

__author__ = 'Flavio Ferrara'

class Story(HackernewsItem):
    def __init__(self, id, by, time, text, kids, url, score, title, descendants, **kwargs):
        super().__init__(id, by, time, text, kids)
        self.descendants = descendants
        self.original_title = title
        self.score = score
        self.url = url
        self.translations = []

    @property
    def title(self, language):
        pass

    def add_translation(self, translation):
        pass
