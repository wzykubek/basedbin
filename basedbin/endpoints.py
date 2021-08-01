from basedbin import app
from basedbin.config import limiter
from basedbin.database import db, allowed_media_types
from fastapi import File, UploadFile, Request, HTTPException
from fastapi.responses import Response
from bson.objectid import ObjectId
from bson.errors import InvalidId
from base64 import b64decode, b64encode


@app.post("/upload")
@limiter.limit("1/second")
async def upload_file(request: Request, file: UploadFile = File(...)):
    content_type = file.content_type
    if content_type in allowed_media_types:
        file_content = file.file.read()
        if content_type.startswith("image/"):
            file_content = b64encode(bytes(file_content))
        obj = {"content_type": content_type, "file_content": file_content}
        paste_id = db.files.insert_one(obj).inserted_id
        return {
            "paste_id": str(paste_id),
            "paste_url": f"{request.base_url}paste/{str(paste_id)}",
        }
    else:
        raise HTTPException(415, "Invalid file type")


@app.get("/paste/{paste_id}")
async def get_paste(paste_id: str, file_format: str = "image"):
    try:
        paste = db.files.find_one({"_id": ObjectId(paste_id)})
        if paste:
            paste_content = paste["file_content"]
            if file_format not in ["image", "base64"]:
                raise HTTPException(400, detail="Invalid file format")
            elif file_format == "image":
                image = b64decode(paste_content)
                content_type = paste["content_type"]
                file_ext = content_type.split("/")[1]
                return Response(image, media_type=content_type)
            else:
                return {"file_content": paste_content.decode("utf-8")}
        else:
            raise HTTPException(404, "Paste not found")
    except InvalidId:
        raise HTTPException(415, detail="Invalid paste ID")
