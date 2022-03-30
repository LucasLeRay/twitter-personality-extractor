import logging

from .fetch import fetch
from .filter import filter
from .personality import add_personality

logger = logging.getLogger(__name__)


def main(count, *, lang, bio_only=False):
    logger.debug("Fetching users...")
    users = fetch(count, lang=lang)
    logger.debug(f"Fetched {len(users)} users...")

    logger.debug("Adding personality columns to users...")
    users = add_personality(users, bio_only=bio_only)

    logger.debug("Filtering users")
    users = filter(users)
    logger.debug(f"Remaining users: {len(users)}")
