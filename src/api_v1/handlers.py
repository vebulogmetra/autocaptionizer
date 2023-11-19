import os
import secrets

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from src.conf import Config
from src.ml.v2 import get_caption

router = APIRouter()


@router.post("/upload-photo")
def upload_photo(photo: UploadFile = File(...)):
    # TODO: проверки безопасности, например, проверить тип файла и размер
    fname, ext = photo.filename.split(".")
    if ext not in Config.allowed_extensions:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"File extension must be: {Config.allowed_extensions}",
        )
    unique_filename = f"{fname}_{secrets.token_hex(4)}.{ext}"
    photo_save_path = os.path.join(
        Config.base_dir,
        Config.uploaded_images_path,
        unique_filename,
    )
    try:
        contents: bytes = photo.file.read()
        with open(photo_save_path, "wb") as f:
            f.write(contents)
    except Exception as e:
        print("Uploading error:\n", {e})
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="There was an error uploading the file",
        )
    finally:
        photo.file.close()

    print(f"Successfully uploaded {photo.filename}")

    caption: str = get_caption(
        image_path=photo_save_path, transl=Config.translate_captions
    )

    return {f"{photo.filename}": caption}
