from app.service.translation import UnbabelService

__author__ = 'Flavio Ferrara'

import unittest

class UnbabelServiceTest(unittest.TestCase):
    def setUp(self):
        self.unbabel = UnbabelService()

    # def testPostTranslation(self):
    #     future = self.unbabel.translate('Welcome!', 'it')
    #     assert future is not None
    #
    #     result = future.result()
    #     print(result.status_code)
    #     assert result.status_code in [201, 202]
    #
    #     data = result.json()
    #     assert data['uid'] != ''
    #     assert data['status'] == 'machine_translate_in_progress'
    #     assert data['text'] == 'Welcome!'
    #     assert data['target_language'] == 'it'
    #     assert data['source_language'] == 'en'

    def testGetTranslation(self):
        future = self.unbabel.get_translation('e578c3349f')
        assert future is not None

        result = future.result()
        print(result.status_code)
        assert result.status_code == 200

        data = result.json()
        assert data is not None
