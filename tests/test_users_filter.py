import pandas as pd
import pytest

from src.schemas import User
import src.users.filter as filters


@pytest.fixture
def valid_user():
    return pd.DataFrame({
        User.EXTRAVERSION: False,
        User.INTUITION: True,
        User.THINKING: False,
        User.JUDGING: True,
    }, index=[1])


@pytest.fixture
def invalid_personality_user():
    return pd.DataFrame({
        User.EXTRAVERSION: None,
        User.INTUITION: True,
        User.THINKING: False,
        User.JUDGING: True,
    }, index=[2])


@pytest.mark.users
class TestUsersFilter:
    def test_filter(self, valid_user, invalid_personality_user):
        users = pd.concat([valid_user, valid_user, invalid_personality_user])
        filtered = filters.filter(users)
        pd.testing.assert_frame_equal(filtered, valid_user, check_dtype=False)

    def test_filter_duplicates(self, valid_user):
        users = pd.concat([valid_user, valid_user])
        filtered = filters._filter_duplicates(users)
        pd.testing.assert_frame_equal(filtered, valid_user, check_dtype=False)

    def test_filter_invalid_personality(
        self, valid_user, invalid_personality_user
    ):
        users = pd.concat([valid_user, invalid_personality_user])
        filtered = filters._filter_invalid_personality(users)
        pd.testing.assert_frame_equal(filtered, valid_user, check_dtype=False)
