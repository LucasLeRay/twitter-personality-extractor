import argparse

from src.extract import extract

DEFAULT_LANGUAGE = "en"
DEFAULT_USER_COUNT = 100
DEFAULT_TWEET_COUNT = 0

parser = argparse.ArgumentParser()
parser.add_argument("--lang", default=DEFAULT_LANGUAGE)
parser.add_argument("--user-count", default=DEFAULT_USER_COUNT, type=int)
parser.add_argument("--tweet-count", default=DEFAULT_TWEET_COUNT, type=int)
parser.add_argument("--bio-only", action="store_true")
parser.add_argument("--debug", action="store_true")


def main():
    args = parser.parse_args()
    extract(**vars(args))


if __name__ == "__main__":
    main()
