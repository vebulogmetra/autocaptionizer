# AutoCaptionizer

## Требования к веб-приложению

- Пользователи должны иметь возможность загружать фотографии.

- После загрузки фотографии, приложение должно использовать текстовую модель для автоматической генерации подписи к изображению.

- Возвращать подпись в виде словаря {"picture_name.jpg": "Сгенерированная подпись"}

## Архитектура приложения

#### Backend (FastAPI):

- Эндпоинт для загрузки и обработки фотографий.
- Разработка механизма сохранения загруженных фотографий на сервере.

#### Текстовая модель:

- Интегрирация модели для генерации подписей.

#### Хранение данных:

- Использование базы данных для хранения информации о загруженных фотографиях и их подписях.

#### Безопасность:

- Механизм аутентификации пользователей.
- Валидация загружаемых файлов и фильтрацию потенциально опасных элементов.

### Frontend:

- Страница регистрации.
- Страница авторизации. 
- Страница для загрузки фотографий.
- Механизм отправки файлов на сервер и вывод ответа или сообщения при ошибках.
