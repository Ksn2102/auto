# routes/user.py
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    return jsonify({
        "id": user_id,
        "email": "user@example.com",
        "name": "Иван Иванов"
    })

@user_bp.route('/bookings', methods=['GET'])
@jwt_required()
def get_user_bookings():
    return jsonify([])