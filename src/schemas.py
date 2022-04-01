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
