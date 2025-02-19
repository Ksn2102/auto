import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///items.db'  # Используем SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True  # Включаем режим отладки
    JWT_SECRET_KEY = 'your_jwt_secret_key'  # Секретный ключ для JWT
    SECRET_KEY = 'your_secret_key'


MAIL_SERVER = 'smtp.mail.ru'  # SMTP-сервер Mail.ru
MAIL_PORT = 587              # Порт для TLS
MAIL_USE_TLS = True          # Используем TLS
MAIL_USERNAME = 'www.Bezrukov-ksenia06@mail.ru'  # Ваш email на Mail.ru
MAIL_PASSWORD = '150100190-kykishka'  # Пароль от email
MAIL_DEFAULT_SENDER = 'www.Bezrukov-ksenia06@mail.ru'  # Отправитель