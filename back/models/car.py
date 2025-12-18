from .db import db

class Car(db.Model):
    __tablename__ = 'cars'
    
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    color = db.Column(db.String(50))
    price = db.Column(db.Numeric(10, 2), nullable=False)
    daily_rate = db.Column(db.Numeric(10, 2), nullable=False)
    image_url = db.Column(db.String(500))
    description = db.Column(db.Text)
    weight = db.Column(db.String(50))
    availability = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    bookings = db.relationship('Booking', backref='car', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'color': self.color,
            'price': float(self.price),
            'daily_rate': float(self.daily_rate),
            'image_url': self.image_url,
            'description': self.description,
            'weight': self.weight,
            'availability': self.availability,
            'text': f"{self.brand} {self.model}",
            'opic': self.description or '',
            'button': 'Подробнее'
        }