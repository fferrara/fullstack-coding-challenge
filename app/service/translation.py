from functools import partial
import json
import threading
import time
from requests_futures.sessions import FuturesSession
from rx import Observable
from app.entity.repository import TranslationRepositoryMongo
from app.entity.translation import TitleTranslation

__author__ = 'Flavio Ferrara'

from rx.subjects import Subject


def build_translation(response, error):
    if response.status_code > 299:
        raise ValueError('Translation request failed: {}'.format(response.content))
    print(response)
    data = response.json()
    return TitleTranslation(**data)


class UnbabelTranslator:
    """
    Offers an asynchronous interface to Unbabel RESTful API, based on RX Observables.
    Due to the async nature of Unbabel translation process, results are not available in real-time.
    The translator is responsible to poll the HTTP endpoint or provide a webhook.

    When a translation is completed, it will be emitted on a stream (Observable).
    """

    def __init__(self):
        self.unbabel = UnbabelService()

    def translate(self, story, language):
        """
        Submits a translation job to Unbabel.
        :param story:
        :param language:
        """
        print('Translating')

        return self.unbabel.translate(story.original_title, language).map(build_translation)

    def check_translations(self, pending):
        """
        Check the state of all pending translations.

        Completed translations will be emitted on the Observable returned.
        :param pending: a list of pending TitleTranslations.
        :return: an Observable where completed TitleTranslations will be emitted
        """
        all_completed = []
        for pending_translation in pending:
            completed = self.unbabel.get_translation(pending_translation.uid) \
                .map(build_translation) \
                .filter(lambda translation: translation.is_completed)
            all_completed.append(completed)

        print(all_completed)
        return Observable.merge(all_completed)


class UnbabelService:
    def __init__(self):
        self.endpoint = 'https://sandbox.unbabel.com/tapi/v2/mt_translation'
        self.headers = {
            'Authorization': 'ApiKey {}:{}'.format('femferrara', 'e5978389579797963998666d6a61aed758417543'),
            'Content-Type': 'application/json'
        }
        self.session = FuturesSession()

    def translate(self, text, language):
        """
        Post a new MT Translation to Unbabel RESTful API
        :param str text:
        :param str language:
        :return:
        """
        print(text)
        payload = {
            "text": text,
            "source_language": "en",
            "target_language": language
        }

        future = self.session.post('{}/'.format(self.endpoint),
                                   headers=self.headers,
                                   data=json.dumps(payload))
        return Observable.from_future(future)

    def get_translation(self, uid):
        """
        Retrieve an MT Translation from Unbabel RESTful API
        :param str uid:
        :return:
        """
        future = self.session.get('{}/{}/'.format(self.endpoint, uid),
                                  headers=self.headers)
        return Observable.from_future(future)
