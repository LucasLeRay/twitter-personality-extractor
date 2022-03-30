import logging

from src.directories import directories
from src.logging import setup as setup_logging
from src.users import get as get_users
from src.tweets import get as get_tweets
from src import io

logger = logging.getLogger(__name__)


def _setup(debug):
    setup_logging(debug)


def _get_users(count, *, lang, bio_only):
    logger.info("Getting users...")
    users = get_users(count, lang=lang, bio_only=bio_only)

    logger.info(f"Extracted {len(users)} users")
    return users


def _get_tweets(count, *, users):
    logger.info("Getting tweets...")
    user_indexes = users.index
    tweets = get_tweets(count, users_indexes=user_indexes)

    logger.info(f"Extracted {len(tweets)} tweets")
    return tweets


def _store_data(*, users, tweets):
    logger.info("Storing users...")
    io.store(users, path=directories.users_output)

    logger.info("Storing tweets...")
    io.store(tweets, path=directories.tweets_output)


def extract(*, lang, user_count, tweet_count, bio_only, debug):
    _setup(debug)
    logger.info("Running extractor...")

    users = _get_users(user_count, lang=lang, bio_only=bio_only)
    tweets = _get_tweets(tweet_count, users=users)

    _store_data(users=users, tweets=tweets)

    logger.info("Extraction completed.")
