import logging

from dotenv import load_dotenv, find_dotenv

LOGGING_FORMAT = "[%(asctime)s] %(levelname)s: %(message)s"

logging.basicConfig(format=LOGGING_FORMAT)
logger = logging.getLogger()

try:
    load_dotenv(find_dotenv(raise_error_if_not_found=True))
except OSError:
    logger.warn("'.env' file not found.")
