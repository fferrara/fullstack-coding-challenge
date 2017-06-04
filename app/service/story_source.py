from requests_futures.sessions import FuturesSession

from app.entity.comment import Comment
from app.entity.story import Story


__author__ = 'Flavio Ferrara'

from rx.subjects import Subject


class StoryFetcher:
    def __init__(self):
        self.__subject = Subject()
        self.hn = HackernewsService()
        self.limit = 10

    @property
    def story_stream(self):
        return self.__subject.as_observable()

    def fetch_stories(self, limit=None):
        print('Fetching stories from hacker news...')
        if limit is not None:
            self.limit = limit

        self.hn.get_all_stories(self.__handle_hn_stories)

    def __handle_hn_stories(self, session, response):
        data = response.json()
        for story_id in data[:self.limit]:
            self.hn.get_item(story_id, self.__handle_hn_story)

    def __handle_hn_story(self, session, response):
        data = response.json()
        if data.get('deleted', False):
            return

        story = Story(**data)
        if story.has_comments():
            story.comments = self.__get_comments(story)

        # push the story to observers
        self.__subject.on_next(story)

    def __get_comments(self, item):
        futures = [self.hn.get_item(comment_id) for comment_id in item.kids]
        comments = []
        for future in futures:
            comment_data = future.result().json()
            if comment_data.get('deleted', False):
                continue
            c = Comment(**comment_data)
            if c.has_comments():
                c.comments = self.__get_comments(c)

            comments.append(c)

        return comments


class HackernewsService:
    def __init__(self):
        self.endpoint = 'https://hacker-news.firebaseio.com/v0/'

    def get_all_stories(self, callback=None):
        session = FuturesSession(max_workers=10)
        return session.get('{}{}'.format(self.endpoint, 'topstories.json'), background_callback=callback)

    def get_item(self, story_id, callback=None):
        session = FuturesSession(max_workers=10)
        return session.get('{}{}{}{}'.format(self.endpoint, 'item/', str(story_id), '.json'), background_callback=callback)


