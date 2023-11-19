from os import PathLike
from pathlib import Path


class Config:
    development: bool = True
    base_dir: PathLike = Path(__file__).parent.parent.parent  # autocaptionizer
    app_host: str = "127.0.0.1"
    app_port: int = 8000
    app_workers_count: int = 1
    app_version: str = "0.1.0"
    pretrained_model_name: str = "Salesforce/blip-image-captioning-large"
    conditional_text: str = "a photography of"
    uploaded_images_path: PathLike = "src/ml/uploaded_images"
    templates_path: PathLike = "src/ui/templates"
    allowed_extensions: tuple[str] = ("jpg", "png", "jpeg")
    translate_captions: bool = True
