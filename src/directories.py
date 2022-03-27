import logging
from pathlib import Path


class _Directories:
    def __init__(self):
        self.project = Path(__file__).parents[1].resolve()
        logging.info(f"Setting up directories at {self.project}...")

        self.output = self.project / "output"
        self.users_output = self.output / "users"
        self.tweets_output = self.output / "tweets"

        for dir_path in vars(self).values():
            try:
                dir_path.mkdir(exist_ok=True, parents=True)
            except Exception:
                logging.error(f"Cannot create directory {dir_path}")


directories = _Directories()
