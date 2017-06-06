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

def translate(story, story_rep, translation_rep):
    print('pushada story {}'.format(story.id))

    story_rep.save(story)
    translator.translate(story, 'pt').subscribe(translation_rep.save)
    #translator.translate(story, 'it').subscribe(store_translation)

def check_translations(story_rep, translation_rep):
    def save_translation(translation):
        story_rep.update_translation(translation)
        translation_rep.save(translation)

    pending = translation_rep.find_pending()
    translator.check_translations(pending).subscribe(save_translation)

if __name__ == '__main__':
    app = create_app()
    db, _ = get_db(app)

    story_rep = StoryRepositoryMongo(db)
    translation_rep = TranslationRepositoryMongo(db)

    new_stories, old_stories = story_fetcher.story_stream.partition(lambda story: story_rep.find_one(story.id) is None)

    # translating new stories
    new_stories.subscribe(lambda story: translate(story, story_rep, translation_rep))
    # updating old stories
    old_stories.subscribe(story_rep.save)

    scheduler = schedule.NonBlockingScheduler()
    #scheduler.every(5).minutes.do(story_fetcher.fetch_stories)
    #scheduler.every().minute.do(lambda: check_translations(story_rep, translation_rep))

    #scheduler.run_continuously()

    story_fetcher.fetch_stories()

    app.run(use_reloader=False)
