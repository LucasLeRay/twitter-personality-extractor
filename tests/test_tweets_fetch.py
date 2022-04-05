import requests
from types import SimpleNamespace

import pytest
from tweepy import errors as api_errors
from unittest.mock import patch

from src.schemas import Tweet
from src.tweets import fetch
from src.twitter_api import TWEET_SOURCE_WEB

MOCK_TWEET_ID = "123abc"


@pytest.fixture
def tweet():
    return SimpleNamespace(
        id_str=MOCK_TWEET_ID,
        full_text="I am ENTJ omg :o",
        favorite_count=1,
        retweet_count=1,
        favorited=True,
        retweeted=False,
        possibly_sensitive=False,
        is_quote_status=False,
        source=TWEET_SOURCE_WEB,
        in_reply_to_status_id=None,
        lang="en",
        entities={
            "hashtags": ["a", "b", "c"],
            "urls": ["a", "b", "c"],
            "user_mentions": ["a", "b", "c"],
            "media": ["a", "b", "c"],
            "symbols": ["a", "b", "c"],
            "polls": ["a", "b", "c"],
        },
        user=SimpleNamespace(
            id="456def",
        )
    )


@pytest.mark.tweets
class TestTweetFetch:
    @pytest.mark.parametrize('is_rt', [False, True])
    def test_format_tweet(self, is_rt, tweet):
        if is_rt:
            status = SimpleNamespace(retweeted_status=tweet)
        else:
            status = tweet

        formatted = fetch._format_tweet(status)

        assert set(formatted.keys()) == set(list(Tweet))
        assert None not in formatted.values()
        assert formatted[Tweet.IS_RETWEET] == is_rt

    @patch("src.tweets.fetch._search_cursor")
    @pytest.mark.parametrize("protected", [False, True])
    def test_get_user_tweets(self, search_cursor, protected, tweet):
        if protected:
            search_cursor.side_effect = api_errors.Unauthorized(
                requests.Response()
            )
        else:
            tweets = [[tweet], [tweet]]
            search_cursor.return_value = tweets

        fetched = fetch._get_user_tweets(user_id="123", count=2)

        assert all(t.id_str == MOCK_TWEET_ID for t in fetched)
        if protected:
            assert len(fetched) == 0

    @pytest.mark.parametrize("tweet_count, expected_pages", [
        [0, 0], [1, 1], [200, 1], [300, 2], [400, 2], [500, 3],
    ])
    def test_pages_count(self, tweet_count, expected_pages):
        assert fetch._pages_count(tweet_count) == expected_pages
