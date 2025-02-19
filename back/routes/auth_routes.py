from flask import Blueprint, jsonify, request
from services.auth_service import AuthService
from core import db, mail

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    response, status_code = AuthService.register_user(data)
    if isinstance(response, dict) and 'error' in response:
        return jsonify(response), status_code

    db.session.add(response)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), status_code

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    response, status_code = AuthService.authenticate_user(data)
    return jsonify(response), status_code

@auth_bp.route('/api/forgot-password', methods=['POST'])
def request_password_reset():
    """Запрос на сброс пароля."""
    data = request.get_json()

    response, status_code = AuthService.forgot_password(data)
    return jsonify(response), status_code

@auth_bp.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    """Сброс пароля через токен."""
    data = request.get_json()
    new_password = data.get('new_password')

    user_id = AuthService.verify_reset_token(token)
    if not user_id:
        return jsonify({"error": "Invalid or expired token"}), 400

    response, status_code = AuthService.reset_password(user_id, new_password)
    return jsonify(response), status_code

