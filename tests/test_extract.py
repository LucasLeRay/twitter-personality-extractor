from os import path, remove

import pytest

from src.directories import directories
from src.extract import FILES_NAME, extract

USER_COUNT = 10


@pytest.mark.e2e
@pytest.mark.api_call
@pytest.mark.parametrize("lang", ["en", "fr"])
@pytest.mark.parametrize("tweet_count", [0, 2])
@pytest.mark.parametrize("bio_only", [False, True])
def test_extract(lang, tweet_count, bio_only):
    extract(
        lang=lang,
        user_count=USER_COUNT,
        tweet_count=tweet_count,
        bio_only=bio_only,
        debug=True
    )

    users_output_path = directories.users_output / FILES_NAME
    assert path.exists(users_output_path)
    remove(users_output_path)

    tweets_output_path = directories.tweets_output / FILES_NAME
    if tweet_count == 0:
        assert not path.exists(tweets_output_path)
    else:
        assert path.exists(tweets_output_path)
        remove(tweets_output_path)
