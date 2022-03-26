import logging

LOGGING_FORMAT = "[%(asctime)s] %(levelname)s: %(message)s"


def setup(debug: bool = False):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(format=LOGGING_FORMAT, level=level)
