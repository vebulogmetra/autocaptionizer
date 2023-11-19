from os import PathLike

import cv2
from cv2.typing import MatLike
from transformers import BlipProcessor  # noqa
from transformers import BlipForConditionalGeneration, PreTrainedModel

from src.conf import config
from src.utils import translate


def get_caption(image_path: PathLike, transl: bool = False) -> str:
    processor: BlipProcessor = BlipProcessor.from_pretrained(
        pretrained_model_name_or_path=config.pretrained_model_name
    )
    model: PreTrainedModel = BlipForConditionalGeneration.from_pretrained(
        pretrained_model_name_or_path=config.pretrained_model_name
    )

    raw_image: MatLike = cv2.imread(image_path)
    raw_image: MatLike = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)

    inputs = processor(raw_image, config.conditional_text, return_tensors="pt")

    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    if transl is True:
        caption = translate(text=caption, src="en", dest="ru")

    return caption
