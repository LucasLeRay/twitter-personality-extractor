from functools import partial

import pandas as pd

from src.mbti import mbti
from src.schemas import User

TMP_PERSONALITY_COL = "tmp_personality"


def _mbti_from_text(text: str) -> str:
    possible_types = mbti.types
    mentions = [p for p in possible_types if p.lower() in text.lower()]
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


def _get_axis_col(users: pd.DataFrame, *, axis_initial: str):
    return users[TMP_PERSONALITY_COL].str.contains(axis_initial)


def add_personality(users: pd.DataFrame, *, bio_only: bool) -> pd.DataFrame:
    get_personality = partial(_mbti_from_user, bio_only=bio_only)

    users[TMP_PERSONALITY_COL] = users.apply(get_personality, axis=1)

    for axis in mbti.axis:
        users[axis.name] = _get_axis_col(users, axis_initial=axis.initial)

    return users.drop(columns=[TMP_PERSONALITY_COL])
