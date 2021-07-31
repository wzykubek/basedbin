from basedbin import app
from os import getenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


MAX_FILE_SIZE = 16  # Mb


class database(object):
    hostname = getenv("DB_HOST")
    port = getenv("DB_PORT")
    user = getenv("DB_USER")
    password = getenv("DB_PASSWORD")


app.config["DATABASE"] = database
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE * 1024 * 1024

limiter = Limiter(
    app, key_func=get_remote_address, default_limits=["200 per day", "50 per hour"]
)
