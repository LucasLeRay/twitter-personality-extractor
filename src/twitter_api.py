import os
from typing import List

import tweepy as tw

ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")

TWEET_SOURCE_WEB = "Twitter Web App"
TWEET_SOURCE_IPHONE = "Twitter for iPhone"
TWEET_SOURCE_ANDROID = "Twitter for Android"


def search_tweet_query(term: List[str]) -> str:
    query = " OR ".join(term)
    return f"{query} -filter:retweets"


def auth():
    twitter_auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tw.API(twitter_auth, wait_on_rate_limit=True)
