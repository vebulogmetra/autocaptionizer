import secrets

from fastapi import APIRouter, File, UploadFile

router = APIRouter()


@router.post("/upload-photo")
def upload_photo(photo: UploadFile = File(...)):
    # TODO: проверки безопасности, например, проверить тип файла и размер
    fname, ext = photo.filename.split(".")
    unique_filename = f"{fname}_{secrets.token_hex(4)}.{ext}"
    return unique_filename
