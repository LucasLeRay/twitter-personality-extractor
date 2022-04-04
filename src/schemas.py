from src.enum import StrEnum
from src import mbti


class User(StrEnum):
    ID = "id"
    BIO = "bio"
    ORIGIN_TWEET_ID = "origin_tweet_id"
    ORIGIN_TWEET_CONTENT = "origin_tweet_content"
    STATUSES_COUNT = "statuses_count"
    FOLLOWERS_COUNT = "followers_count"
    FOLLOWING_COUNT = "following_count"
    LISTED_COUNT = "listed_count"
    EXTRAVERSION = mbti.EXTRAVERSION
    INTUITION = mbti.INTUITION
    THINKING = mbti.THINKING
    JUDGING = mbti.JUDGING


class Tweet(StrEnum):
    ID = "id"
    USER_ID = "user_id"
    TEXT = "text"
    LANG = "lang"
    LIKE_COUNT = "like_count"
    RETWEET_COUNT = "retweet_count"
    HASHTAGS_COUNT = "hashtags_count"
    URLS_COUNT = "urls_count"
    MENTIONS_COUNT = "mentions_count"
    MEDIA_COUNT = "media_count"
    SYMBOLS_COUNT = "symbols_count"
    POLLS_COUNT = "polls_count"
    FAVORITED_BY_SELF = "favorited_by_self"
    RETWEETED_BY_SELF = "retweeted_by_self"
    POSSIBLY_SENSITIVE = "possibly_sensitive"
    QUOTE_TWEET = "quote_tweet"
    SOURCE = "source"
    IS_RETWEET = "is_retweet"
    IS_REPLY = "is_reply"
