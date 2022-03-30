import pandas as pd

from tweepy import Cursor, Tweet

from src import twitter_api
from src.mbti import mbti
from src.schemas import User


def _search_cursor(*, count: int, lang: str):
    client = twitter_api.auth()
    return Cursor(
        client.search_tweets,
        q=twitter_api.search_tweet_query(mbti.types),
        lang=lang,
    ).items(count)


def _format_user(tweet: Tweet):
    return {
        User.BIO: tweet.user.description,
        User.ORIGIN_TWEET_ID: tweet.id,
        User.ORIGIN_TWEET_CONTENT: tweet.text,
        User.STATUSES_COUNT: tweet.user.statuses_count,
        User.FOLLOWERS_COUNT: tweet.user.followers_count,
        User.FOLLOWING_COUNT: tweet.user.friends_count,
        User.LISTED_COUNT: tweet.user.listed_count,
    }


def fetch(count: int, *, lang: str) -> pd.DataFrame:
    users = pd.DataFrame(columns=list(User)).set_index(User.ID)
    cursor = _search_cursor(count=count, lang=lang)

    for tweet in cursor:
        users.loc[tweet.user.id] = _format_user(tweet)

    return users
