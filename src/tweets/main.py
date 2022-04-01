import logging

from .fetch import fetch as fetch_tweets
from .filter import filter as filter_tweets

logger = logging.getLogger(__name__)


def get(count, *, users_ids):
    logger.debug("Fetching tweets...")
    tweets = fetch_tweets(count, users_ids=users_ids)
    logger.debug(f"Fetched {len(tweets)} tweets.")

    logger.debug("Filtering tweets...")
    filter_tweets(tweets)
    logger.debug(f"Remaining tweets: {len(tweets)}")
