# AutoCaptionizer

Этот проект представляет собой систему генерации подписей к загруженным фотографиям с использованием предобученной модели [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large). В качестве интерфейса используется интерактивная документация FastAPI (v1), версия на Flask и Jinja (v2), а также версия интерфейса в виде телеграм бота.

## Установка

1. Склонируйте репозиторий:

```bash
git clone https://github.com/vebulogmetra/autocaptionizer.git
```

2. Перейдите в директорию проекта:

```bash
cd autocaptionizer
```

3. Установите зависимости:

```bash
pip install -U pip && pip install -r requirements.txt
```

## Запуск

### FastAPI

1. Запустите сервер FastAPI:

```bash
uvicorn src.api_v1.main:app --reload
```
Или просто:
```bash
python .
```

2. Откройте интерактивную документацию в браузере по адресу `http://localhost:8000/docs`.

### Flask и Jinja

1. Перейдите в директорию `src/api_v2`:

```bash
cd src/api_v2
```

2. Запустите сервер Flask:

```bash
python main.py
```

3. Откройте приложение в браузере по адресу `http://localhost:5000`.

### Телеграм бот

1. Установите токен вашего телеграм бота.
```bash
echo "your_bot_token" > src/conf/.env
```
2. Перейдите в директорию `telegram`:

```bash
cd src/telegram
```
3. Запустите бота:

```bash
python bot.py
```

## Использование

1. Загрузите фотографию в интерфейсе приложения или отправьте ее в телеграм бота.

2. Модель Salesforce/blip-image-captioning-large сгенерирует подпись к фотографии.

3. Подпись будет отображена в интерфейсе или отправлена вам в телеграм боте.

## Благодарности

Мы благодарим Salesforce за предоставленную предобученную модель [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large).

## FAQ

### Какие типы фотографий поддерживаются?

Система поддерживает различные типы фотографий, включая изображения людей, животных, предметов и пейзажей.

### Какую точность можно ожидать от модели?

Точность генерации подписей зависит от качества фотографии и сложности содержимого. Модель Salesforce/blip-image-captioning-large имеет хорошие показатели точности, но иногда может допускать ошибки или генерировать несвязные подписи.

### Можно ли использовать свою собственную модель для генерации подписей?

Да, вы можете использовать свою собственную модель для генерации подписей. Просто замените модель Salesforce/blip-image-captioning-large на свою модель в файле src/conf/settings.py и обновите соответствующие зависимости.