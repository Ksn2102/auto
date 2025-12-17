from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from flask import jsonify


db = SQLAlchemy()

mail = Mail()


jwt = JWTManager()

def init_jwt(app):
    """Инициализация JWTManager и настройка обработчиков ошибок"""
    jwt.init_app(app)

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return {"message": "Missing Authorization Header", "error": "authorization_required"}, 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return {"message": "Invalid token provided", "error": "invalid_token"}, 422

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return {"message": "The token has expired", "error": "token_expired"}, 401