from app.entity.comment import Comment

__author__ = 'Flavio Ferrara'

import unittest


class CommentTest(unittest.TestCase):
    def testCreatingWithoutComments(self):
        data = {"kids": [],
                "text": "For me, calling a BBS will always be a modem and modem tones.",
                "time": 1496592233, "by": "chrissnell", "id": 14482164,
                "parent": 14481296}
        comment = Comment(**data)
        assert comment is not None
        assert isinstance(comment, Comment)
        assert comment.id == 14482164
        assert comment.has_comments() == False
        assert comment.text == "For me, calling a BBS will always be a modem and modem tones."

    def testCreatingWithComments(self):
        data = {"kids": [14481297, 14481290],
                "text": "For me, calling a BBS will always be a modem and modem tones.",
                "time": 1496592233, "by": "chrissnell", "id": 14482164,
                "parent": 14481296}
        comment = Comment(**data)
        assert comment is not None
        assert isinstance(comment, Comment)
        assert comment.id == 14482164
        assert comment.has_comments() == True
        assert comment.text == "For me, calling a BBS will always be a modem and modem tones."

    def testCreatingFromDocument(self):
        document = {"kids": [14482164],
                    "text": "Archive as the site is dead at the moment",
                    "time": 1496587720, "by": "aw3c2", "id": 14481838, "parent": 14481296,
                    "comments": [
                        {"kids": [], "text": "the way it was meant to be done", "time": 1496592233, "by": "chrissnell",
                         "id": 14482164, "parent": 14481838}]}

        comment = Comment.from_document(**document)
        assert comment is not None
        assert isinstance(comment, Comment)
        assert comment.id == 14481838
        assert comment.text == "Archive as the site is dead at the moment"
        assert comment.has_comments() == True
        assert len(comment.comments) == 1

        comment = comment.comments[0]
        assert isinstance(comment, Comment)
        assert comment.text == "the way it was meant to be done"
