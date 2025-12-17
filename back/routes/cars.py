from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.db import db
from models.car import Car

cars_bp = Blueprint('cars', __name__)

@cars_bp.route('/', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    return jsonify([car.to_dict() for car in cars])

@cars_bp.route('/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = Car.query.get_or_404(car_id)
    return jsonify(car.to_dict())

@cars_bp.route('/', methods=['POST'])
@jwt_required()
def create_car():
    if not request.is_json:
        return jsonify({'error': 'Missing JSON in request'}), 400
    
    data = request.get_json()
    
    car = Car(
        brand=data['brand'],
        model=data['model'],
        year=data.get('year'),
        color=data.get('color'),
        price=data['price'],
        daily_rate=data['daily_rate'],
        image_url=data.get('image_url'),
        description=data.get('description'),
        weight=data.get('weight'),
        availability=data.get('availability', True)
    )
    
    db.session.add(car)
    db.session.commit()
    
    return jsonify(car.to_dict()), 201

@cars_bp.route('/<int:car_id>', methods=['PUT'])
@jwt_required()
def update_car(car_id):
    car = Car.query.get_or_404(car_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(car, key):
            setattr(car, key, value)
    
    db.session.commit()
    return jsonify(car.to_dict())

@cars_bp.route('/<int:car_id>', methods=['DELETE'])
@jwt_required()
def delete_car(car_id):
    car = Car.query.get_or_404(car_id)
    db.session.delete(car)
    db.session.commit()
    return jsonify({'message': 'Car deleted'})