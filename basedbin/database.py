from pymongo import MongoClient
from basedbin import app
from basedbin.config import database as host

client = MongoClient(
    host.hostname, int(host.port), username=host.user, password=host.password
)
database = client["basedbin"]


class db(object):
    files = database["files"]


allowed_media_types = ["text/plain", "image/png", "image/jpeg"]
