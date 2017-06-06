import app.scheduler as schedule
from app.db import get_db
from app.entity.repository import TranslationRepositoryMongo, StoryRepositoryMongo
from app.factory import create_app
from app.service.story_source import StoryFetcher
from app.service.translation import UnbabelTranslator

import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def translate(story):
    def add_translation(translation):
        story.translations.append(translation)
        story_rep.save(story)

    translator.translate(story, 'pt').subscribe(add_translation)
    translator.translate(story, 'it').subscribe(add_translation)


def check_translations():
    pending = translation_rep.find_pending()

    if not pending:
        return
    translator.check_translations(pending).subscribe(translation_rep.save)

if __name__ == '__main__':
    story_fetcher = StoryFetcher()
    translator = UnbabelTranslator()
    app = create_app()
    db, _ = get_db()

    story_rep = StoryRepositoryMongo(db)
    translation_rep = TranslationRepositoryMongo(db)

    # translating new stories
    story_fetcher.story_stream\
        .filter(lambda story: story_rep.find_one(story.id) is None)\
        .subscribe(translate)
    # updating all stories
    story_fetcher.story_stream.subscribe(story_rep.save)

    scheduler = schedule.NonBlockingScheduler()
    scheduler.every(10).minutes.do(story_fetcher.fetch_stories)
    scheduler.every().minute.do(check_translations)

    scheduler.run_continuously()

    story_fetcher.fetch_stories()

    app.run(use_reloader=False)
