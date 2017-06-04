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
    translation_rep = TranslationRepositoryMongo(db)

    new_stories = story_fetcher.story_stream\
        .filter(lambda story: story_rep.find_one(story.id) is None)

    new_stories.subscribe(lambda story: print('new {}'.format(story.id)))

    #new_stories.subscribe(story_rep.save)
    #new_stories.subscribe(lambda story: translate(story, translation_rep))
    #translator.translation_stream.subscribe(store_story)

    scheduler = schedule.NonBlockingScheduler()
    #scheduler.every(5).seconds.do(story_fetcher.fetch_stories)
    #scheduler.run_continuously()

    scheduler.every().minute.do(translator.check_translations)


    #story_fetcher.fetch_stories()


    app.run(use_reloader=False)
