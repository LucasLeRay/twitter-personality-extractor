import pandas as pd

from src.mbti import mbti


def _filter_invalid_personality(users: pd.DataFrame) -> pd.DataFrame:
    axis_cols = [axis.name for axis in mbti.axis]
    return users.dropna(subset=axis_cols)


def _filter_duplicates(users: pd.DataFrame) -> pd.DataFrame:
    return users[~users.index.duplicated(keep="first")]


def filter(users: pd.DataFrame) -> pd.DataFrame:
    return (
        users
        .pipe(_filter_invalid_personality)
        .pipe(_filter_duplicates)
    )
