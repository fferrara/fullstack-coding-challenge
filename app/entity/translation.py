__author__ = 'Flavio Ferrara'


class TranslationStatus():
    PENDING = 'machine_translate_in_progress'
    COMPLETED = 'deliver_ok'


class TitleTranslation:
    def __init__(self,
                 uid,
                 text,
                 status,
                 target_language,
                 translatedText=None,
                 text_format='text',
                 **kwargs):
        self.uid = uid
        self.text = text
        self.translatedText = translatedText
        self.target_language = target_language
        self.status = status
        self.text_format = text_format

    def is_completed(self):
        return self.status == TranslationStatus.COMPLETED

    def to_document(self):
        return self.__dict__.copy()

    def complete_translation(self, text):
        self.translatedText = text
        self.status = TranslationStatus.COMPLETED
