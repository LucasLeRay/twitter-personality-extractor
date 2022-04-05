import pytest

from src.users.main import main as users_pipeline

TWEET_COUNT = 2
LANG = "en"

@pytest.mark.users
class TestUsersPipeline:
    @pytest.mark.parametrize("bio_only", [False, True])
    def test_users_pipeline(self, bio_only):
        users_pipeline(TWEET_COUNT, lang=LANG, bio_only=bio_only)
