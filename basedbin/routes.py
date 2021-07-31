from basedbin import app
from basedbin.config import limiter
from basedbin.database import db, allowed_media_types
from basedbin.helpers import gen_html_error
from flask import request, jsonify, make_response
from bson.objectid import ObjectId
from base64 import b64decode, b64encode


@app.route("/")
def home():
    return "<h1>basedbin</h1>"


@app.route("/upload", methods=["POST"])
@limiter.limit("1/second")
def upload():
    input_file = request.files["file"]
    if input_file.mimetype in ["text/plain"]:
        file_content = input_file.read()
        paste_id = db.files.insert_one(
            {"file_type": "plain_text", "content": file_content}
        ).inserted_id
        return str(paste_id), 201
    elif input_file.mimetype in allowed_media_types:
        file_content = input_file.read()
        b64_image = b64encode(bytes(file_content))
        paste_id = db.files.insert_one(
            {"file_type": input_file.mimetype, "content": b64_image}
        ).inserted_id
        return str(paste_id), 201
    else:
        return gen_html_error(415, "Invalid file type"), 415


@app.route("/paste/<paste_id>", methods=["GET"])
def paste(paste_id: str):
    results = [x for x in db.files.find({"_id": ObjectId(paste_id)})]
    if len(results) == 1:
        paste = results[0]
        paste_content = paste["content"]
        image_format = request.args.get("image_format", default="image", type=str)
        if image_format not in ["image", "base64"]:
            return gen_html_error(400, "Invalid file format"), 400
        if (
            image_format != "base64"
            and "file_type" in paste.keys()
            and paste["file_type"] in allowed_media_types
        ):
            image = b64decode(paste_content)
            file_type = paste["file_type"]
            file_ext = file_type.split("/")[1]
            response = make_response(image)
            response.headers.set("Content-Type", file_type)
            response.headers.set(
                "Content-Disposition",
                "attachment",
                filename=f'{str(paste["_id"])}.{file_ext}',
            )
            return response
        else:
            return paste_content.decode("utf-8"), 200
