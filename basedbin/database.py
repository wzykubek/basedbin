from pymongo import MongoClient
from basedbin import app

host = app.config["DATABASE"]

client = MongoClient(
    host.hostname, int(host.port), username=host.user, password=host.password
)
database = client["basedbin"]


class db(object):
    files = database["files"]


allowed_media_types = ["image/png", "image/jpeg"]
