from dotenv import load_dotenv, find_dotenv

try:
    load_dotenv(find_dotenv(raise_error_if_not_found=True))
except OSError:
    raise RuntimeError("'.env' file not found.")
