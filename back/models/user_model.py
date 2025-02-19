from . import db
from passlib.hash import bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)  # Заменяем username на login
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(100), nullable=False)  # Имя
    surname = db.Column(db.String(100), nullable=False)   # Фамилия
    patronimyc = db.Column(db.String(100))                 # Отчество (опционально)
    email = db.Column(db.String(100))                 # Отчество (опционально)

    def set_password(self, password):
        self.password_hash = bcrypt.hash(password)

    def check_password(self, password):
        return bcrypt.verify(password, self.password_hash)

    def to_dict(self):
        return {
            "id": self.id,
            "login": self.login,
            "name": self.name,
            "surname": self.surname,
            "patronimyc": self.patronimyc,
            "email":self.email
        }