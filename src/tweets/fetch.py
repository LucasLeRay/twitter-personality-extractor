from itertools import chain
import math
from typing import List

import pandas as pd
from tweepy import Cursor, errors as api_errors, Tweet as APITweet

from src import twitter_api
from src.encoder import tokenize_tweet_entities, tweet_source_mapper
from src.schemas import Tweet


def _pages_count(tweet_count: int):
    return math.ceil(tweet_count / twitter_api.TWEET_PER_PAGE)


def _search_cursor(count: int, *, user_id: str):
    pages_to_fetch = _pages_count(count)
    client = twitter_api.auth()

    return Cursor(
        client.user_timeline,
        user_id=user_id,
        count=twitter_api.TWEET_PER_PAGE,
        include_rts=True,
        exclude_replies=True,
        tweet_mode="extended",
        trim_user=True,
    ).pages(pages_to_fetch)


def _get_user_tweets(user_id: str, *, count: int):
    try:
        pages = [page for page in _search_cursor(count, user_id=user_id)]
        return [item for sublist in pages for item in sublist]
    except api_errors.Unauthorized:
        # This error is raised if user is protected
        return []


def _format_tweet(tweet: APITweet):
    try:
        status = tweet.retweeted_status
        is_rt = True
    except AttributeError:
        status = tweet
        is_rt = False

    entities = status.entities

    return {
        Tweet.ID: status.id_str,
        Tweet.USER_ID: status.user.id,
        Tweet.TEXT: tokenize_tweet_entities(status.full_text).replace("\n", " "),  # noqa E501
        Tweet.LANG: status.lang,
        Tweet.LIKE_COUNT: status.favorite_count,
        Tweet.RETWEET_COUNT: status.retweet_count,
        Tweet.HASHTAGS_COUNT: len(entities["hashtags"]) if "hashtags" in entities else 0,  # noqa E501
        Tweet.URLS_COUNT: len(entities["urls"] or []) if "urls" in entities else 0,  # noqa E501
        Tweet.MENTIONS_COUNT: len(entities["user_mentions"] or []) if "user_mentions" in entities else 0,  # noqa E501
        Tweet.MEDIA_COUNT: len(entities["media"] or []) if "media" in entities else 0,  # noqa E501
        Tweet.SYMBOLS_COUNT: len(entities["symbols"] or []) if "symbols" in entities else 0,  # noqa E501
        Tweet.POLLS_COUNT: len(entities["polls"] or []) if "polls" in entities else 0,  # noqa E501
        Tweet.FAVORITED_BY_SELF: bool(status.favorited),
        Tweet.RETWEETED_BY_SELF: bool(status.retweeted),
        Tweet.POSSIBLY_SENSITIVE: hasattr(status, "possibly_sensitive") and status.possibly_sensitive,  # noqa E501
        Tweet.QUOTE_TWEET: bool(status.is_quote_status),
        Tweet.SOURCE: tweet_source_mapper[status.source],
        Tweet.IS_RETWEET: bool(is_rt),
        Tweet.IS_REPLY: bool(status.in_reply_to_status_id),
    }


def fetch(count: int, *, users_ids: List[str]):
    fetched = [_get_user_tweets(user_id, count=count) for user_id in users_ids]

    flatten = chain(*fetched)
    formatted = [_format_tweet(tweet) for tweet in flatten]

    tweets_df = pd.DataFrame(formatted).set_index(Tweet.ID)

    return tweets_df
