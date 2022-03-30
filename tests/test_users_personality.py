import itertools

import pandas as pd
import pytest

from src.mbti import mbti
from src.schemas import User
import src.users.personality as personality

MOCK_MBTI_TYPE_1 = "ENTJ"
MOCK_MBTI_TYPE_2 = "ISFP"
FAKE_MBTI_TYPE = "LLBG"


@pytest.fixture
def users():
    return pd.DataFrame({
        User.ORIGIN_TWEET_CONTENT: ["", "", MOCK_MBTI_TYPE_1, MOCK_MBTI_TYPE_1],
        User.BIO: ["", MOCK_MBTI_TYPE_2, MOCK_MBTI_TYPE_2, ""]
    })


@pytest.mark.users
class TestUsersPersonality:
    @pytest.mark.parametrize("mbti_type", mbti.types)
    def test_single_mbti_from_text(self, mbti_type):
        text = f"BlAbLa {mbti_type} BlAbLa"
        assert personality._mbti_from_text(text) == mbti_type
        
    @pytest.mark.parametrize("mbti_types", itertools.combinations(mbti.types, 2))
    def test_multiple_mbti_from_text(self, mbti_types):
        text = f"BlAbLa {mbti_types[0]} BlAbLa {mbti_types[1]}"
        assert personality._mbti_from_text(text) == None
    
    def test_no_mbti_from_text(self):
        text = "BlAbLa"
        assert personality._mbti_from_text(text) == None

    @pytest.mark.parametrize("axis_value", ["initial", "opposite"])
    def test_valid_mbti_axis(self, axis_value):
        mbti_type = "".join([getattr(p, axis_value) for p in mbti.axis])
        user = pd.DataFrame({personality.TMP_TYPE_COL: [mbti_type]})
        enriched_user = personality._add_axis_cols(user)
        assert sum(enriched_user.isnull().any()) == 0

    def test_null_mbti_axis(self):
        user = pd.DataFrame({personality.TMP_TYPE_COL: [None]})
        enriched_user = personality._add_axis_cols(user)
        assert sum(enriched_user.isnull().any()) > 0

    @pytest.mark.parametrize("bio_only", [True, False])
    def test_mbti_from_text_and_from_bio(self, bio_only):
        user = pd.Series({
            User.BIO: MOCK_MBTI_TYPE_1,
            User.ORIGIN_TWEET_CONTENT: MOCK_MBTI_TYPE_2
        })
        res = personality._mbti_from_user(user, bio_only=bio_only)
        assert res == MOCK_MBTI_TYPE_1

    @pytest.mark.parametrize("bio_only", [True, False])
    def test_mbti_from_text_only(self, bio_only):
        user = pd.Series({
            User.BIO: "",
            User.ORIGIN_TWEET_CONTENT: MOCK_MBTI_TYPE_1
        })
        res = personality._mbti_from_user(user, bio_only=bio_only)
        assert res == None if bio_only else res == MOCK_MBTI_TYPE_1

    @pytest.mark.parametrize("bio_only", [True, False])
    def test_mbti_from_bio_only(self, bio_only):
        user = pd.Series({
            User.BIO: MOCK_MBTI_TYPE_1,
            User.ORIGIN_TWEET_CONTENT: ""
        })
        res = personality._mbti_from_user(user, bio_only=bio_only)
        assert res == MOCK_MBTI_TYPE_1

    @pytest.mark.parametrize("bio_only", [True, False])
    def test_no_mbti_from_user(self, bio_only):
        user = pd.Series({
            User.BIO: "",
            User.ORIGIN_TWEET_CONTENT: ""
        })
        res = personality._mbti_from_user(user, bio_only=bio_only)
        assert res == None

    @pytest.mark.parametrize("bio_only, expected_mbti", [
        [True, [None, False, False, None]],
        [False, [None, False, False, True]]
    ])
    def test_correct_mbti_add_personality(self, bio_only, expected_mbti, users):
        enriched = personality.add_personality(users, bio_only=bio_only)

        assert enriched[User.EXTRAVERSION].equals(pd.Series(expected_mbti))
        assert enriched[User.INTUITION].equals(pd.Series(expected_mbti))
        assert enriched[User.THINKING].equals(pd.Series(expected_mbti))
        assert enriched[User.JUDGING].equals(pd.Series(expected_mbti))

    def test_columns_add_personality(self, users):
        enriched = personality.add_personality(users, bio_only=False)

        assert personality.TMP_TYPE_COL not in enriched.columns

