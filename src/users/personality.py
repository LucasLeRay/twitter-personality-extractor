from functools import partial

import pandas as pd

from src.mbti import mbti
from src.schemas import User

TMP_TYPE_COL = "tmp_mbti_type"


def _mbti_from_text(text: str) -> str:
    mentions = [p for p in mbti.types if p.lower() in text.lower()]
    # When several personalities are present, we can't choose
    if len(mentions) > 1 or len(mentions) == 0:
        return None
    return mentions[0]


def _mbti_from_user(user: pd.DataFrame, *, bio_only: bool) -> pd.DataFrame:
    origin_tweet = user[User.ORIGIN_TWEET_CONTENT]
    bio = user[User.BIO]

    if personality := _mbti_from_text(bio):
        return personality
    return None if bio_only else _mbti_from_text(origin_tweet)


def _add_axis_cols(users: pd.DataFrame):
    for axis in mbti.axis:
        users[axis.name] = users[TMP_TYPE_COL].str.contains(axis.initial)
    return users


def add_personality(users: pd.DataFrame, *, bio_only: bool) -> pd.DataFrame:
    get_personality = partial(_mbti_from_user, bio_only=bio_only)

    users[TMP_TYPE_COL] = users.apply(get_personality, axis=1)
    users = _add_axis_cols(users)

    return users.drop(columns=[TMP_TYPE_COL])
