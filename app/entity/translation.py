__author__ = 'Flavio Ferrara'


class TitleTranslation:
    def __init__(self,
                 uid=-1,
                 translated_text=None,
                 target_language="",
                 status=None,
                 text_format='text'):
        self.uid = uid
        self.translated_text = translated_text
        self.target_language = target_language
        self.status = status
        self.text_format = text_format
