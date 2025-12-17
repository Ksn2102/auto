from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.db import db
from models.booking import Booking
from models.car import Car
from datetime import datetime

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/', methods=['GET'])
@jwt_required()
def get_user_bookings():
    user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=user_id).all()
    return jsonify([booking.to_dict() for booking in bookings])

@bookings_bp.route('/', methods=['POST'])
@jwt_required()
def create_booking():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    # Проверка доступности автомобиля
    car = Car.query.get_or_404(data['car_id'])
    if not car.availability:
        return jsonify({'error': 'Car is not available'}), 400
    
    # Расчет стоимости
    start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')
    days = (end_date - start_date).days + 1
    total_price = days * float(car.daily_rate)
    
    # Создание бронирования
    booking = Booking(
        user_id=user_id,
        car_id=data['car_id'],
        tariff_id=data.get('tariff_id'),
        start_date=start_date,
        end_date=end_date,
        total_price=total_price,
        status='pending',
        pickup_location=data.get('pickup_location'),
        notes=data.get('notes')
    )
    
    db.session.add(booking)
    car.availability = False  # Помечаем как занятую
    db.session.commit()
    
    return jsonify(booking.to_dict()), 201

@bookings_bp.route('/<int:booking_id>', methods=['GET'])
@jwt_required()
def get_booking(booking_id):
    user_id = get_jwt_identity()
    booking = Booking.query.get_or_404(booking_id)
    
    if booking.user_id != int(user_id):
        return jsonify({'error': 'Unauthorized'}), 403
    
    return jsonify(booking.to_dict())

@bookings_bp.route('/<int:booking_id>/cancel', methods=['POST'])
@jwt_required()
def cancel_booking(booking_id):
    user_id = get_jwt_identity()
    booking = Booking.query.get_or_404(booking_id)
    
    if booking.user_id != int(user_id):
        return jsonify({'error': 'Unauthorized'}), 403
    
    # Освобождаем автомобиль
    car = Car.query.get(booking.car_id)
    if car:
        car.availability = True
    
    booking.status = 'cancelled'
    db.session.commit()
    
    return jsonify({'message': 'Booking cancelled'})