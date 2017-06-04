from functools import partial
import json
import threading
import time
from requests_futures.sessions import FuturesSession
from app.entity.translation import TitleTranslation

__author__ = 'Flavio Ferrara'

from rx.subjects import Subject


class UnbabelTranslator:
    """
    Offers an asynchronous interface to Unbabel RESTful API, based on RX Observables.
    Due to the async nature of Unbabel translation process, results are not available in real-time.
    The translator is responsible to poll the HTTP endpoint or provide a webhook.

    When a translation is completed, it will be emitted on its stream (Observable).
    """

    def __init__(self):
        self.__pending = {}
        self.unbabel = UnbabelService()

    def translate(self, story, language):
        """
        Submits a translation job to Unbabel.
        :param story:
        :param language:
        """
        print('Translating')
        subject = Subject()
        self.__pending[(story.id, language)] = subject

        def callback(session, response):
            data = response.json()
            subject.on_next(data)

        #self.unbabel.translate(story.title, language, callback)
        self.unbabel.get_translation('', callback)

        return subject.as_observable()


class UnbabelService:
    def __init__(self):
        self.endpoint = 'https://www.unbabel.com/tapi/v2'
        self.headers = {
            'Authorization': 'ApiKey {}:{}'.format('gracaninja', '5a6406e31f77ef779c4024b1579f0f6103944c5e'),
            'Content-Type': 'application/json'
        }
        self.session = FuturesSession()

    def translate(self, text, language, callback):
        """
        Post a new MT Translation to Unbabel RESTful API
        :param str text:
        :param str language:
        :return:
        """
        payload = {
            "text": text,
            "source_language": "en",
            "target_language": language
        }

        return self.session.post('{}{}'.format(self.endpoint, '/mt_translation/'),
                                headers=self.headers,
                                data=json.dumps(payload),
                                background_callback=callback

        )

    def get_translation(self, uid, callback):
        """
        Retrieve an MT Translation from Unbabel RESTful API
        :param str uid:
        :return:
        """
        return self.session.get('{}{}'.format(self.endpoint, '/mt_translation/'),
                                headers=self.headers,
                                background_callback=callback)




