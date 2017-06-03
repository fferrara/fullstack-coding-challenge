__author__ = 'Flavio Ferrara'


class Translation:
    def __init__(self,
                 uid=-1,
                 text="",
                 translated_text=None,
                 target_language="",
                 source_language=None,
                 status=None,
                 topics=None,
                 text_format='text'):
        self.uid = uid
        self.text = text
        self.translated_text = translated_text
        self.source_language = source_language
        self.target_language = target_language
        self.status = status
        self.topics = topics
        self.text_format = text_format
