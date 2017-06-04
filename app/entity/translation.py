__author__ = 'Flavio Ferrara'


class TitleTranslation:
    def __init__(self,
                 uid,
                 text,
                 translated_text=None,
                 target_language="",
                 status=None,
                 text_format='text',
                 **kwargs):
        self.uid = uid
        self.text = text,
        self.translated_text = translated_text
        self.target_language = target_language
        self.status = status
        self.text_format = text_format
