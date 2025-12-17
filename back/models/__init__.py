# models/__init__.py
from .db import db

# Импортируйте ТЕ модели, которые у вас ЕСТЬ:
from .car import Car          # У вас есть car.py, а не car_model.py
from .user import User        # У вас есть user.py, а не user_model.py
from .item_model import Item  # Этот файл есть