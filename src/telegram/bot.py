import threading

import requests
from telebot import TeleBot
from telebot.types import File

from src.conf import config, logger

bot = TeleBot(token=config.telegram_token)


@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.reply_to(
        message,
        """\
Hi there, I am AutocaptionizerBot.
Send me the images and I will generate a description!\
""",
    )


@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    print(f"user_id: {message.from_user.id}")
    file_info: File = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    file_size: int = file_info.file_size
    print(f"file_size Kb: {file_size / 1024}")
    file_name: str = file_info.file_path.split("/")[1]
    downloaded_file: bytes = bot.download_file(file_path=file_info.file_path)
    thread = threading.Thread(
        target=send_photo, args=(downloaded_file, file_name, message)
    )
    thread.start()
    bot.reply_to(
        message, "The photo has been uploaded, you will receive the result soon."
    )


def send_photo(downloaded_file: bytes, file_name: str, message) -> dict:
    logger.info("Запрос к API")
    resp = requests.post(
        url=config.captionizer_api_url,
        files={"photo": downloaded_file},
        params={"photo_filename": file_name},
    )
    logger.info(f"Ответ API: {resp.json()}")

    bot.reply_to(
        message=message,
        text=f"<b>Photo caption: </b>{list(resp.json().values())[0]}",
        parse_mode="HTML",
    )


bot.polling(non_stop=True, interval=3)
