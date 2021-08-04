from basedbin import app
from os import getenv
from slowapi import Limiter
from slowapi.util import get_remote_address

MAX_FILE_SIZE = 16  # Mb


class database(object):
    hostname = getenv("DB_HOST")
    port = getenv("DB_PORT")
    user = getenv("DB_USER")
    password = getenv("DB_PASSWORD")


# app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE * 1024 * 1024

limiter = Limiter(key_func=get_remote_address)
ALLOWED_MEDIA_TYPES = ["text", "image"]