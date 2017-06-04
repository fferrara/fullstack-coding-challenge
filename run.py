import threading
import time
from app.entity.comment import Comment
from app.entity.story import Story
import app.scheduler as schedule
from app.db import get_db
from app.entity.repository import TranslationRepositoryMongo, StoryRepositoryMongo
from app.factory import create_app
from app.service.story_source import StoryFetcher
from app.service.translation import UnbabelTranslator

story_fetcher = StoryFetcher()
translator = UnbabelTranslator()

def translate(story, repository):
    print('pushada story {}'.format(story.id))

    translator.translate(story, 'pt-BR').subscribe(repository.save)
    #translator.translate(story, 'it').subscribe(store_translation)

if __name__ == '__main__':
    app = create_app()

    db, _ = get_db(app)

    story_rep = StoryRepositoryMongo(db)

    story_fetcher.story_stream.subscribe(story_rep.save)

    #story_fetcher.story_stream.subscribe(lambda story: translate(story, translation_rep))
    #translator.translation_stream.subscribe(store_story)

    #scheduler = schedule.NonBlockingScheduler()
    #scheduler.every(5).seconds.do(story_fetcher.fetch_stories)
    #scheduler.run_continuously()


    story_fetcher.fetch_stories()


    app.run(use_reloader=False)
