import logging

from dotenv import load_dotenv, find_dotenv

LOGGING_FORMAT = "[%(asctime)s] %(levelname)s: %(message)s"

logging.basicConfig(format=LOGGING_FORMAT)

try:
    load_dotenv(find_dotenv(raise_error_if_not_found=True))
except OSError:
    raise RuntimeError("'.env' file not found.")
