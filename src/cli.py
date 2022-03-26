import argparse

DEFAULT_LANGUAGE = "en"
DEFAULT_USER_COUNT = 100
DEFAULT_TWEET_COUNT = 0

parser = argparse.ArgumentParser()
parser.add_argument("--lang", default=DEFAULT_LANGUAGE)
parser.add_argument("--user-count", default=DEFAULT_USER_COUNT, type=int)
parser.add_argument("--tweet-count", default=DEFAULT_TWEET_COUNT, type=int)
parser.add_argument("--description-only", action="store_true")


def main():
    parser.parse_args()


if __name__ == "__main__":
    main()
