from flask import Flask
from flask_cors import CORS
from config import Config
from core import db, mail, jwt  # Импортируем объекты из core.py
from routes import item_bp, auth_bp

app = Flask(__name__)

# Загружаем конфигурацию
app.config.from_object(Config)

# Инициализируем объекты
db.init_app(app)
mail.init_app(app)
jwt.init_app(app)

# Инициализация CORS
CORS(app)

# Регистрируем blueprints
app.register_blueprint(item_bp)
app.register_blueprint(auth_bp)

# Создание таблиц в базе данных
with app.app_context():
    db.create_all()

# Запуск приложения
if __name__ == '__main__':
    app.run()