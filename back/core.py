from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_jwt_extended import JWTManager

# Инициализация базы данных
db = SQLAlchemy()

# Инициализация Flask-Mail
mail = Mail()

# Инициализация JWT
jwt = JWTManager()