import os
import secrets
from typing import Optional

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from src.conf import config, logger
from src.ml.v2 import get_caption

router = APIRouter()


@router.post("/upload-photo")
def upload_photo(photo: UploadFile = File(...), photo_filename: Optional[str] = None):
    # TODO: проверки безопасности, например, проверить тип файла и размер
    # При отправке через tg бота
    if photo.filename == "upload" or photo_filename:
        if photo_filename:
            photo.filename = photo_filename
        else:
            photo.filename = secrets.token_urlsafe(4)
    fname, ext = photo.filename.split(".")
    if ext not in config.allowed_extensions:
        logger.error(f"File extension must be: {config.allowed_extensions}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"File extension must be: {config.allowed_extensions}",
        )
    unique_filename = f"api_{fname}_{secrets.token_hex(4)}.{ext}"
    photo_save_path = os.path.join(
        config.base_dir,
        config.uploaded_images_path,
        unique_filename,
    )
    try:
        contents: bytes = photo.file.read()
        with open(photo_save_path, "wb") as f:
            f.write(contents)
    except Exception as e:
        logger.error("Uploading error:\n", {e})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="There was an error uploading the file",
        )
    finally:
        photo.file.close()

    logger.info(f"Successfully uploaded {photo.filename}")

    caption: str = get_caption(
        image_path=photo_save_path, transl=config.translate_captions
    )

    logger.info(f"Generated caption: '{caption}' filename: {photo.filename}")

    return {f"{photo.filename}": caption}
