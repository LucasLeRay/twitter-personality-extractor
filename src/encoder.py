from collections import defaultdict
import re

from src.twitter_api import (
  TWEET_SOURCE_WEB,
  TWEET_SOURCE_IPHONE,
  TWEET_SOURCE_ANDROID
)

TWEET_HASHTAG_TOKEN = "#HASHTAG"
TWEET_USER_TOKEN = "@USER"
TWEET_URL_TOKEN = "URL"


def tokenize_tweet_entities(text):
    res = re.sub(r"http\S+", TWEET_HASHTAG_TOKEN, text)
    res = re.sub(r"@\S+", TWEET_USER_TOKEN, res)
    res = re.sub(r"#\S+", TWEET_URL_TOKEN, res)
    return res


tweet_source_mapper = defaultdict(
  lambda: 3, {
    TWEET_SOURCE_WEB: 0,
    TWEET_SOURCE_IPHONE: 1,
    TWEET_SOURCE_ANDROID: 2
  }
)
