from flask import Blueprint, jsonify, request
# УДАЛЕНО: from numpy import var
from services.item_service import ItemService
from models.db import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from models.car import Car

from werkzeug.utils import secure_filename
import os


admin_bp = Blueprint('admin', __name__)

def is_admin(user_id):
    user = User.query.get(user_id)
    return user and user.is_admin  

@admin_bp.route('/api/items', methods=['GET'])
@jwt_required()
def get_items():
    current_user_id = get_jwt_identity()
    if not is_admin(current_user_id):
        return jsonify({"error": "Access denied"}), 403

    items = ItemService.get_all_items()
    return jsonify([item.to_dict() for item in items])

@admin_bp.route('/admin/items', methods=['POST'])
@jwt_required()
def add_item():
    current_user_id = get_jwt_identity()
    if not is_admin(current_user_id):
        return jsonify({"error": "Access denied"}), 403

    data = request.get_json()
    new_item = ItemService.create_item(data)
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

@admin_bp.route('/admin/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    current_user_id = get_jwt_identity()
    if not is_admin(current_user_id):
        return jsonify({"error": "Access denied"}), 403

    data = request.get_json()
    updated_item = ItemService.update_item(item_id, data)
    if not updated_item:
        return jsonify({"error": "Item not found"}), 404

    db.session.commit()
    return jsonify(updated_item.to_dict())


@admin_bp.route('/admin/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    current_user_id = get_jwt_identity()
    if not is_admin(current_user_id):
        return jsonify({"error": "Access denied"}), 403

    deleted_item = ItemService.delete_item(item_id)
    if not deleted_item:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(deleted_item)
    db.session.commit()
    return jsonify({"message": "Item deleted"})