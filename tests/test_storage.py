from os import path, remove

import pandas as pd
import pytest

from src.directories import directories
from src.extract import FILES_NAME, _store_data
from src.schemas import User, Tweet


@pytest.mark.storage
@pytest.mark.parametrize("tweets, users", [
    [pd.DataFrame(columns=list(Tweet)), pd.DataFrame(columns=list(User))],
    [None, pd.DataFrame(columns=list(User))]
])
def test_storage(tweets, users):
    _store_data(users=users, tweets=tweets)

    users_output_path = directories.users_output / FILES_NAME
    assert path.exists(users_output_path)
    remove(users_output_path)

    tweets_output_path = directories.tweets_output / FILES_NAME
    if tweets is None:
        assert not path.exists(tweets_output_path)
    else:
        assert path.exists(tweets_output_path)
        remove(tweets_output_path)
