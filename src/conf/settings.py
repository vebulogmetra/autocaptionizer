from dataclasses import dataclass
from os import PathLike, getenv, path
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger


@dataclass
class Config:
    load_dotenv(path.join(Path(__file__).parent, ".env"))
    development: bool = True
    base_dir: PathLike = Path(__file__).parent.parent.parent  # autocaptionizer
    app_host: str = "127.0.0.1"
    app_port: int = 8000
    app_version: str = "0.1.1"
    pretrained_model_name: str = "Salesforce/blip-image-captioning-large"
    conditional_text: str = "a photography of"
    uploaded_images_path: PathLike = "src/ml/uploaded_images"
    templates_path: PathLike = "src/ui/templates"
    allowed_extensions: tuple[str] = ("jpg", "png", "jpeg")
    translate_captions: bool = True

    telegram_token: str = getenv("TELEGRAM_TOKEN", None)
    captionizer_api_url = "http://127.0.0.1:8000/img/upload-photo"


config: Config = Config()

logger.add(
    path.join(Path(__file__).parent, "logs/app.log"),
    rotation="1 MB",
    retention="7 days",
    level="INFO",
)
