import logging
from requests import session
from requests.adapters import HTTPAdapter
from requests_futures.sessions import FuturesSession
from rx import Observable

from app.entity.comment import Comment
from app.entity.story import Story


__author__ = 'Flavio Ferrara'

from rx.subjects import Subject


def not_deleted_story(story_json):
    return story_json.get('deleted', False) is False


class StoryFetcher:
    def __init__(self):
        self.__subject = Subject()
        self.hn = HackernewsService()
        self.limit = 10

    @property
    def story_stream(self):
        return self.__subject.as_observable()

    def fetch_stories(self, limit=None):
        logging.info('Fetching stories from hacker news...')
        if limit is not None:
            self.limit = limit

        self.hn.get_all_stories_obs() \
            .map(lambda response: response.json()) \
            .subscribe(self.__handle_hn_stories)

    def __handle_hn_stories(self, stories_json):
        for story_id in stories_json[:self.limit]:
            self.hn.get_item_obs(story_id) \
                .map(lambda response: response.json()) \
                .filter(not_deleted_story) \
                .subscribe(self.__handle_hn_story)

    def __handle_hn_story(self, story_json):
        story = Story(**story_json)
        if story.has_comments():
            story.comments = self.__get_comments(story)

        # push the story to observers
        self.__subject.on_next(story)

    # This function is the only blocking one, due to the recursive structure of comments
    def __get_comments(self, item):
        futures = [self.hn.get_item(comment_id) for comment_id in item.kids]
        comments = []
        for future in futures:
            comment_data = future.result().json()  # this call waits for the future to finish
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
        self.session = FuturesSession(max_workers=50)

    def get_all_stories_obs(self):
        future = self.session.get('{}{}'.format(self.endpoint, 'topstories.json'))
        return Observable.from_future(future)

    def get_item_obs(self, item_id):
        future = self.get_item(item_id)
        return Observable.from_future(future)

    def get_item(self, item_id):
        return self.session.get('{}{}{}{}'.format(self.endpoint, 'item/', str(item_id), '.json'))


