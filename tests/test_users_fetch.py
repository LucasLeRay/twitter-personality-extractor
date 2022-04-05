import copy
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from src.schemas import User
from src.users import fetch

FETCH_COUNT = 2
FETCH_LANG = "en"


@pytest.fixture
def tweets():
    tweet = SimpleNamespace(
      id="123abc",
      full_text="I am ENTJ omg :o",
      user=SimpleNamespace(
        id="456def",
        description="I am Lucas ;)",
        statuses_count=123,
        followers_count=456,
        friends_count=789,
        listed_count=0
      )
    )
    tweet2 = copy.deepcopy(tweet)
    tweet2.user.id = "789ghi"
    return [tweet, tweet2]


@pytest.mark.users
class TestUserFetch:
    def test_format_user(self, tweets):
        expected_keys = set(list(User)) - set([
            User.EXTRAVERSION,
            User.INTUITION,
            User.THINKING,
            User.JUDGING,
            User.ID
        ])

        formatted = fetch._format_user(tweets[0])

        assert set(formatted.keys()) == expected_keys
        assert None not in formatted.values()

    @patch("src.users.fetch._search_cursor")
    def test_fetch_user(self, _search_cursor, tweets):
        _search_cursor.return_value = tweets
        expected_cols = set(list(User)) - set([User.ID])

        users = fetch.fetch(FETCH_COUNT, lang=FETCH_LANG)

        assert len(users) == FETCH_COUNT
        assert set(users.columns) == expected_cols
