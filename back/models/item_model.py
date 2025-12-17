# models/item_model.py
from .db import db  # Корректный импорт

class Item(db.Model):  # Теперь db содержит Model
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    # ... остальные поля