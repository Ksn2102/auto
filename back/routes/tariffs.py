# routes/tariffs.py
from flask import Blueprint, jsonify

tariffs_bp = Blueprint('tariffs', __name__)

@tariffs_bp.route('/api/tariffs', methods=['GET'])
def get_tariffs():
    return jsonify([
        {"id": 1, "name": "Эконом", "price": "1 500 ₽/сутки"},
        {"id": 2, "name": "Стандарт", "price": "2 500 ₽/сутки"},
        {"id": 3, "name": "Премиум", "price": "5 000 ₽/сутки"}
    ])