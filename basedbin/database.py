from pymongo import MongoClient
from basedbin import database_host as host

client = MongoClient(
    host.hostname, int(host.port), username=host.user, password=host.password
)
database = client["basedbin"]


class db(object):
    files = database["files"]


allowed_media_types = ["image/png", "image/jpeg"]
