from models.user_model import User
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from core import mail  # Импортируем mail из core.py
from config import Config

class AuthService:
    @staticmethod
    def register_user(data):
        login = data.get('login')
        password = data.get('password')
        name = data.get('name')
        patronimyc = data.get('patronimyc')
        surname = data.get('surname')
        email = email.get('email')

        if not login or not password or not name or not surname:
            return {"error": "Login, password, first_name and last_name are required"}, 400

        existing_user = User.query.filter_by(login=login).first()
        if existing_user:
            return {"error": "User already exists"}, 409

        new_user = User(
            login=login,
            name=name,
            surname=surname,
            patronimyc=patronimyc,
            email=email
        )
        new_user.set_password(password)
        return new_user, 201

    @staticmethod
    def authenticate_user(data):
        login = data.get('login')
        password = data.get('password')

        user = User.query.filter_by(login=login).first()
        if not user or not user.check_password(password):
            return {"error": "Invalid credentials"}, 401

        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}, 200
    
    @staticmethod
    def forgot_password(data):
        email = data.get('email')

        user = User.query.filter_by(email=email).first()
        if not user:
            return {"error": "User not found"}, 404

        AuthService.send_password_reset_email(user)
        return {"message": "Password reset email sent"}, 200

    @staticmethod
    def generate_reset_token(user_id):
        """Генерирует временный токен для сброса пароля."""
        serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
        return serializer.dumps(user_id, salt='password-reset')

    @staticmethod
    def verify_reset_token(token, expiration=3600):
        """Проверяет токен для сброса пароля."""
        serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
        try:
            user_id = serializer.loads(token, salt='password-reset', max_age=expiration)
            return user_id
        except Exception:
            return None

    @staticmethod
    def send_password_reset_email(user):
        """Отправляет email с ссылкой для сброса пароля."""
        token = AuthService.generate_reset_token(user.id)
        reset_url = f"http://localhost:8080/reset-password/{token}"  # URL вашего фронтенда

        msg = Message("Сброс пароля", recipients=[user.email])
        msg.body = f"Чтобы сбросить пароль, перейдите по ссылке: {reset_url}"
        mail.send(msg)

    @staticmethod
    def reset_password(user_id, new_password):
        """Сбрасывает пароль пользователя."""
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        user.set_password(new_password)
        return {"message": "Password reset successfully"}, 200