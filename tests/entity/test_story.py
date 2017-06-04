from app.entity.comment import Comment
from app.entity.story import Story

__author__ = 'Flavio Ferrara'

import unittest


class StoryTest(unittest.TestCase):
    def testCreatingWithouComments(self):
        data = {
            "by": "shara",
            "descendants": 0,
            "id": 8866,
            "score": 2,
            "time": 1175714617,
            "title": "What Entrepreneurs Most Want to Know: March 2007's Most Popular Work.com How-to Guides",
            "type": "story",
            "url": "http://blogs.work.com/community/2007/04/what_entreprene.html"
        }
        story = Story(**data)
        assert story is not None
        assert isinstance(story, Story)
        assert story.id == 8866
        assert story.has_comments() == False
        assert story.title == "What Entrepreneurs Most Want to Know: March 2007's Most Popular Work.com How-to Guides"

    def testCreatingWithComments(self):
        data = {
            "by": "dhouston",
            "descendants": 71,
            "id": 8863,
            "kids": [8952, 9224, 8917, 8884, 8887, 8943, 8869, 8958, 9005, 9671, 9067, 8940, 8908, 9055, 8865, 8881,
                     8872, 8873, 8955, 10403, 8903, 8928, 9125, 8998, 8901, 8902, 8907, 8894, 8878, 8980, 8870, 8934,
                     8876],
            "score": 111,
            "time": 1175714200,
            "title": "My YC app: Dropbox - Throw away your USB drive",
            "type": "story",
            "url": "http://www.getdropbox.com/u/2/screencast.html"
        }
        story = Story(**data)
        assert story is not None
        assert isinstance(story, Story)
        assert story.id == 8863
        assert story.has_comments() == True
        assert story.title == "My YC app: Dropbox - Throw away your USB drive"

    def testCreatingFromDocument(self):
        document = {"_id": 14481296, "kids": [14482164, 14481838, 14482011, 14481688, 14481711, 14481806], "text": "",
                    "time": 1496580879, "by": "ingve", "id": 14481296, "descendants": 7,
                    "original_title": "The Wonderful WiFi232: BBSing Has Never Been Easier", "score": 62,
                    "url": "http://www.bytecellar.com/2017/05/30/the-wonderful-wifi232-bbsing-has-literally-never-been-easier/",
                    "translations": [], "comments": [{"kids": [],
                                                      "text": "For me, calling a BBS will always be a modem and modem tones.",
                                                      "time": 1496592233, "by": "chrissnell", "id": 14482164,
                                                      "parent": 14481296}, {"kids": [],
                                                                            "text": "Archive as the site is dead at the moment: ",
                                                                            "time": 1496587720, "by": "aw3c2",
                                                                            "id": 14481838, "parent": 14481296}]}

        story = Story.from_document(**document)
        assert story is not None
        assert isinstance(story, Story)
        assert story.id == 14481296
        assert story.title == "The Wonderful WiFi232: BBSing Has Never Been Easier"
        assert story.has_comments() == True
        assert len(story.comments) == 2

        comment = story.comments[0]
        assert isinstance(comment, Comment)
        assert comment.text == "For me, calling a BBS will always be a modem and modem tones."
