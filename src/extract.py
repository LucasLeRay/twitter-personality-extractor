import logging

from src.logging import setup as setup_logging


def extract(
    *,
    lang: str,
    user_count: int,
    tweet_count: int,
    description_only: bool,
    debug: str
):
    setup_logging(debug)
    logging.info("Running extractor...")
