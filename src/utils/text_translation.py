from googletrans import Translator


def translate(text: str, src: str = "en", dest: str = "ru") -> str:
    translator = Translator(service_urls=["translate.googleapis.com"])
    result = translator.translate(text=text, src=src, dest=dest)
    return result.text
