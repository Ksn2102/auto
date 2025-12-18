from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.item_service import ItemService
from core import db
from models.item_model import Item

item_bp = Blueprint('item', __name__)

@item_bp.route('/items', methods=['GET'])
@jwt_required()
def get_items():
    items = ItemService.get_all_items()
    return jsonify([item.to_dict() for item in items])

@item_bp.route('/items/<int:item_id>', methods=['GET'])
@jwt_required()
def get_item(item_id):
    item = ItemService.get_item_by_id(item_id)
    if item:
        return jsonify(item.to_dict())
    return jsonify({"error": "Item not found"}), 404

@item_bp.route('/items', methods=['POST'])
@jwt_required()
def add_item():
    data = request.get_json()
    new_item = ItemService.create_item(data)
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

@item_bp.route('/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    data = request.get_json()
    updated_item = ItemService.update_item(item_id, data)
    if updated_item:
        db.session.commit()
        return jsonify(updated_item.to_dict())
    return jsonify({"error": "Item not found"}), 404

@item_bp.route('/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    deleted_item = ItemService.delete_item(item_id)
    if deleted_item:
        db.session.delete(deleted_item)
        db.session.commit()
        return jsonify({"message": "Item deleted"})
    return jsonify({"error": "Item not found"}), 404
