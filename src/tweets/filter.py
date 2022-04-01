import pandas as pd


def _filter_duplicates(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[~tweets.index.duplicated(keep="first")]


def filter(tweets: pd.DataFrame) -> pd.DataFrame:
    return (
        tweets
        .pipe(_filter_duplicates)
    )
