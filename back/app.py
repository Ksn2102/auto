from flask import Flask, jsonify, request
from flask_cors import CORS
import bcrypt
import jwt
import datetime

app = Flask(__name__)
CORS(app)

# ========== ВРЕМЕННЫЕ БАЗЫ ДАННЫХ ==========
users_db = []
bookings_db = []
user_counter = 1
booking_counter = 1

# ========== ВАШИ 12 МАШИН ==========
CARS = [
    {
        "id": 1, "img": "211.jpg", "text": "Машина синяя", 
        "price": "1 900 890 ", "color": "Синий", "weight": "2 т",
        "opic": "Люкс в каждом детале. Mercedes-Benz E-Class — это воплощение элегантности и технологического совершенства.",
        "button": "Подробнее", "availability": "В наличии"
    },
    {
        "id": 2, "img": "213.jpg", "text": "Mercedes", 
        "price": "11 000 790 ", "color": "Белый", "weight": "2 т",
        "opic": "Идеальное сочетание комфорта и надёжности. Toyota Camry — автомобиль для тех, кто ценит стабильность.",
        "button": "Подробнее", "availability": "В наличии"
    },
    {
        "id": 3, "img": "214.webp", "text": "BMW", 
        "price": "1 000 183 ", "color": "Красный", "weight": "1 т",
        "opic": "Компактный кроссовер с характером. Volkswagen Tiguan предлагает идеальный баланс.",
        "button": "Подробнее", "availability": "В наличии"
    },
    {
        "id": 4, "img": "215.jpg", "text": "Reno", 
        "price": "600 500 ", "color": "Черный", "weight": "2 т",
        "opic": "Городской помощник с амбициями. Hyundai Tucson сочетает стильный внешний вид.",
        "button": "Подробнее", "availability": "В наличии"
    },
    {
        "id": 5, "img": "21.jpg", "text": "Jeep", 
        "price": "5 099 000 ", "color": "Голубой", "weight": "2 т",
        "opic": "Малыш с большим сердцем. Kia Rio — практичный и доступный компаньон для города.",
        "button": "Подробнее", "availability": "В наличии"
    },
    {
        "id": 6, "img": "22.webp", "text": "Pedjo", 
        "price": "500 222 ", "color": "Синий", "weight": "5 т",
        "opic": "Премиум-кроссовер для уверенных людей. BMW X5 объединяет мощь, комфорт и инновации.",
        "button": "Подробнее", "availability": "В наличии"
    },
    {
        "id": 7, "img": "24.webp", "text": "Touota camry", 
        "price": "1 200 000 ", "color": "Белый", "weight": "2 т",
        "opic": "Стильный компактный кроссовер с премиальными амбициями. Audi Q3 предлагает современный дизайн.",
        "button": "Подробнее", "availability": "В наличии"
    },
    {
        "id": 8, "img": "25.webp", "text": "Машина голубая", 
        "price": "8 000 000", "color": "Черный", "weight": "2 т",
        "opic": "Баланс мощи и комфорта. Lexus RX — это премиальный кроссовер.",
        "button": "Подробнее", "availability": "В наличии"
    },
    {
        "id": 9, "img": "26.jpg", "text": "Джип", 
        "price": "2 000 861 ", "color": "Серебрянный", "weight": "2 т",
        "opic": "Драйвовая управляемость и практичность. Ford Focus — это автомобиль для тех, кто любит контролировать.",
        "button": "Подробнее", "availability": "В наличии"
    },
    {
        "id": 10, "img": "28.webp", "text": "Nissan", 
        "price": "1 900 890 ", "color": "Черный", "weight": "2 т",
        "opic": "Умный выбор для активной жизни. Nissan Qashqai предлагает идеальный баланс.",
        "button": "Подробнее", "availability": "В наличии"
    },
    {
        "id": 11, "img": "29.jpeg", "text": "Wolfsfagen", 
        "price": "800 000 ", "color": "Белый", "weight": "2 т",
        "opic": "Спортивный характер в компактном кузове. Porsche Macan — это кроссовер с гоночной душой.",
        "button": "Подробнее", "availability": "В наличии"
    },
    {
        "id": 12, "img": "27.webp", "text": "Citrouen", 
        "price": "4 000 000", "color": "Черный", "weight": "10 т",
        "opic": "Люкс в каждом детале. Mercedes-Benz E-Class — это воплощение элегантности.",
        "button": "Подробнее", "availability": "В наличии"
    }
]

# ========== СОЗДАНИЕ ТЕСТОВОГО ПОЛЬЗОВАТЕЛЯ ПРИ ЗАПУСКЕ ==========
# Создаем тестового пользователя для проверки
test_user_password = bcrypt.hashpw("test123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
test_user = {
    "id": 1,
    "email": "test@example.com",
    "password_hash": test_user_password,
    "first_name": "Иван",
    "last_name": "Иванов",
    "phone": "+79991234567",
    "created_at": datetime.datetime.now(datetime.UTC).isoformat()
}
users_db.append(test_user)
user_counter = 2

# Создаем тестовую бронь
test_booking = {
    "id": 1,
    "user_id": 1,
    "car_id": 3,
    "car_name": "BMW",
    "customer_name": "Иван Иванов",
    "phone": "+79991234567",
    "email": "test@example.com",
    "date": "2024-12-20",
    "time": "14:00",
    "comment": "Тестовая бронь для демонстрации",
    "status": "confirmed",
    "created_at": datetime.datetime.now(datetime.UTC).isoformat()
}
bookings_db.append(test_booking)
booking_counter = 2

# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==========

def verify_token():
    """Проверка JWT токена с подробной отладкой"""
    auth_header = request.headers.get('Authorization', '')
    
    if not auth_header:
        print("  Нет заголовка Authorization")
        return None
    
    if not auth_header.startswith('Bearer '):
        print(f" Заголовок не начинается с 'Bearer ': {auth_header[:50]}...")
        return None
    
    token = auth_header.replace('Bearer ', '').strip()
    
    if not token:
        print("  Пустой токен после 'Bearer '")
        return None
    
    print(f" Проверка токена: {token[:30]}...")
    
    try:
        payload = jwt.decode(token, "car-rental-secret-key", algorithms=["HS256"])
        print(f" Токен валиден! user_id: {payload.get('user_id')}")
        return payload
    except jwt.ExpiredSignatureError:
        print(" Токен истек")
        return None
    except jwt.InvalidTokenError as e:
        print(f" Невалидный токен: {str(e)}")
        return None
    except Exception as e:
        print(f" Ошибка при проверке токена: {str(e)}")
        return None

# ========== АУТЕНТИФИКАЦИЯ ==========

@app.route('/api/register', methods=['POST'])
def register():
    """Регистрация нового пользователя"""
    try:
        data = request.json
        print(f" Регистрация: {data.get('email')}")
        
        # Валидация
        if not data.get('email') or '@' not in data.get('email', ''):
            return jsonify({"error": "Некорректный email"}), 400
        
        if not data.get('password') or len(data.get('password', '')) < 6:
            return jsonify({"error": "Пароль должен быть не менее 6 символов"}), 400
        
        # Проверка существующего пользователя
        if any(u['email'] == data['email'] for u in users_db):
            return jsonify({"error": "Email уже зарегистрирован"}), 409
        
        # Хеширование пароля
        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        global user_counter
        user = {
            "id": user_counter,
            "email": data['email'],
            "password_hash": hashed,
            "first_name": data.get('first_name', ''),
            "last_name": data.get('last_name', ''),
            "phone": data.get('phone', ''),
            "created_at": datetime.datetime.now(datetime.UTC).isoformat()
        }
        
        users_db.append(user)
        user_counter += 1
        
        # Создание токена
        token = jwt.encode(
            {
                "user_id": user["id"],
                "email": user["email"],
                "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=24)
            },
            "car-rental-secret-key",
            algorithm="HS256"
        )
        
        print(f" Пользователь зарегистрирован: {user['email']} (ID: {user['id']})")
        
        return jsonify({
            "success": True,
            "message": "Регистрация успешна!",
            "user": {
                "id": user["id"],
                "email": user["email"],
                "first_name": user["first_name"],
                "last_name": user["last_name"],
                "phone": user["phone"]
            },
            "access_token": token
        }), 201
        
    except Exception as e:
        print(f" Ошибка регистрации: {str(e)}")
        return jsonify({"error": "Ошибка сервера"}), 500

@app.route('/api/login', methods=['POST'])
def login():
    """Вход пользователя"""
    try:
        data = request.json
        print(f" Вход: {data.get('email')}")
        
        user = next((u for u in users_db if u['email'] == data.get('email')), None)
        
        if not user:
            print(f" Пользователь не найден: {data.get('email')}")
            return jsonify({"error": "Неверный email или пароль"}), 401
        
        # Проверка пароля
        if not bcrypt.checkpw(
            data['password'].encode('utf-8'),
            user['password_hash'].encode('utf-8')
        ):
            print(f" Неверный пароль для: {data.get('email')}")
            return jsonify({"error": "Неверный email или пароль"}), 401
        
        # Создание токена
        token = jwt.encode(
            {
                "user_id": user["id"],
                "email": user["email"],
                "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=24)
            },
            "car-rental-secret-key",
            algorithm="HS256"
        )
        
        print(f" Вход выполнен: {user['email']} (ID: {user['id']})")
        
        return jsonify({
            "success": True,
            "message": "Вход выполнен успешно!",
            "user": {
                "id": user["id"],
                "email": user["email"],
                "first_name": user["first_name"],
                "last_name": user["last_name"],
                "phone": user["phone"]
            },
            "access_token": token
        })
        
    except Exception as e:
        print(f" Ошибка входа: {str(e)}")
        return jsonify({"error": "Ошибка сервера"}), 500

@app.route('/api/user/profile', methods=['GET'])
def get_profile():
    """Получить профиль текущего пользователя"""
    print(" Запрос профиля пользователя")
    
    payload = verify_token()
    if not payload:
        return jsonify({"error": "Необходима авторизация"}), 401
    
    user_id = payload['user_id']
    user = next((u for u in users_db if u['id'] == user_id), None)
    
    if not user:
        print(f" Пользователь с ID {user_id} не найден в базе")
        return jsonify({"error": "Пользователь не найден"}), 404
    
    print(f" Профиль отправлен для: {user['email']}")
    
    return jsonify({
        "success": True,
        "user": {
            "id": user["id"],
            "email": user["email"],
            "first_name": user["first_name"],
            "last_name": user["last_name"],
            "phone": user["phone"],
            "created_at": user["created_at"]
        }
    })

# ========== МАШИНЫ ==========

@app.route('/api/cars', methods=['GET'])
def get_cars():
    """Получить список всех машин"""
    print(" Запрос списка машин")
    return jsonify(CARS)

@app.route('/api/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    """Получить информацию о конкретной машине"""
    print(f" Запрос машины ID: {car_id}")
    
    car = next((c for c in CARS if c['id'] == car_id), None)
    if car:
        return jsonify(car)
    
    print(f" Машина с ID {car_id} не найдена")
    return jsonify({"error": "Машина не найдена"}), 404

# ========== БРОНИРОВАНИЯ ==========

@app.route('/api/bron', methods=['POST'])
def create_bron():
    """Создание бронирования (ТОЛЬКО для авторизованных пользователей)"""
    try:
        data = request.json
        print(f" Создание брони: Машина {data.get('carId')}")
        
        #  ТРЕБУЕМ авторизацию
        payload = verify_token()
        if not payload:
            print(" Попытка бронирования без авторизации")
            return jsonify({
                "success": False,
                "error": "Для бронирования необходимо войти в систему"
            }), 401
        
        user_id = payload['user_id']
        print(f" Пользователь авторизован: user_id={user_id}")
        
        global booking_counter
        booking = {
            "id": booking_counter,
            "user_id": user_id,  
            "car_id": data.get('carId'),
            "car_name": data.get('carName', f"Машина {data.get('carId')}"),
            "customer_name": data.get('name', 'Не указано'),
            "phone": data.get('phone', 'Не указан'),
            "email": data.get('email', 'Не указан'),
            "date": data.get('date', 'Не указана'),
            "time": data.get('time', 'Не указано'),
            "comment": data.get('comment', ''),
            "status": "pending",
            "created_at": datetime.datetime.now(datetime.UTC).isoformat()
        }
        
        bookings_db.append(booking)
        booking_counter += 1
        
        print(f" Бронь создана! ID: {booking['id']}, Пользователь: {user_id}")
        
        return jsonify({
            "success": True,
            "message": " Бронирование успешно создано!",
            "booking": booking
        })
        
    except Exception as e:
        print(f" Ошибка при создании брони: {str(e)}")
        return jsonify({"error": "Ошибка при создании брони"}), 500

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    """Получить все брони текущего пользователя"""
    print(" Запрос списка броней")
    
    payload = verify_token()
    if not payload:
        print(" Нет авторизации для просмотра броней")
        return jsonify({"error": "Необходима авторизация"}), 401
    
    user_id = payload['user_id']
    user_bookings = [b for b in bookings_db if b['user_id'] == user_id]
    
    print(f" Найдено броней: {len(user_bookings)} для user_id={user_id}")
    
    return jsonify({
        "success": True,
        "count": len(user_bookings),
        "bookings": user_bookings
    })

# ========== ТАРИФЫ ==========

@app.route('/api/tarifs', methods=['GET'])
def get_tarifs():
    """Получить список тарифов"""
    print(" Запрос тарифов")
    return jsonify([
        {
            "id": 1, 
            "name": "Эконом", 
            "price": "1 500 ₽", 
            "period": "/сутки",
            "features": ["До 200 км в сутки", "Эконом-класс", "Базовая страховка"]
        },
        {
            "id": 2, 
            "name": "Стандарт", 
            "price": "2 500 ₽", 
            "period": "/сутки",
            "features": ["Безлимитный пробег", "Комфорт-класс", "Полная страховка", "Доп. водитель"]
        },
        {
            "id": 3, 
            "name": "Премиум", 
            "price": "5 000 ₽", 
            "period": "/сутки",
            "features": ["Безлимитный пробег", "Премиум-класс", "Расширенная страховка", "Доставка авто"]
        }
    ])

# ========== ОТЛАДОЧНЫЕ МАРШРУТЫ (только для разработки) ==========

@app.route('/api/debug/users', methods=['GET'])
def debug_users():
    """Отладка: посмотреть всех пользователей"""
    print(" Отладочный запрос: все пользователи")
    users_safe = []
    for user in users_db:
        users_safe.append({
            "id": user["id"],
            "email": user["email"],
            "first_name": user["first_name"],
            "last_name": user["last_name"],
            "phone": user["phone"],
            "created_at": user["created_at"]
        })
    
    return jsonify({
        "users_count": len(users_db),
        "users": users_safe,
        "bookings_count": len(bookings_db),
        "bookings": bookings_db
    })

@app.route('/api/test-auth', methods=['GET'])
def test_auth():
    """Тестирование авторизации"""
    print(" Тест авторизации")
    
    payload = verify_token()
    if payload:
        return jsonify({
            "success": True,
            "message": " Авторизация работает!",
            "user_id": payload.get('user_id'),
            "email": payload.get('email')
        })
    else:
        return jsonify({
            "success": False,
            "message": " Нет валидной авторизации"
        }), 401

# ========== ГЛАВНАЯ СТРАНИЦА ==========

@app.route('/')
def home():
    """Главная страница API"""
    return jsonify({
        "project": " Car Rental API",
        "status": " Работает!",
        "version": "1.0.0",
        "users_count": len(users_db),
        "bookings_count": len(bookings_db),
        "cars_count": len(CARS),
        "test_user": "test@example.com / test123",
        "endpoints": [
            "POST /api/register - Регистрация",
            "POST /api/login - Вход",
            "GET  /api/user/profile - Профиль пользователя",
            "GET  /api/cars - Каталог машин",
            "GET  /api/cars/:id - Страница машины",
            "POST /api/bron - Бронирование",
            "GET  /api/bookings - Мои брони",
            "GET  /api/tarifs - Тарифы",
            "GET  /api/test-auth - Тест авторизации",
            "GET  /api/debug/users - Отладка (все пользователи)"
        ]
    })

@app.route('/api/debug/all-bookings', methods=['GET'])
def debug_all_bookings():
    """Отладка: посмотреть ВСЕ брони (для разработки)"""
    return jsonify({
        "total_bookings": len(bookings_db),
        "bookings": bookings_db
    })

@app.route('/api/my-bookings', methods=['GET'])
def get_my_bookings_simple():
    """Упрощенный маршрут для броней (без проверки токена)"""
    # Для тестирования возвращаем все брони
    return jsonify(bookings_db)

# ========== ЗАПУСК СЕРВЕРА ==========

if __name__ == '__main__':
    print("=" * 60)
    print(" CAR RENTAL API ЗАПУЩЕН!")
    print(" Адрес: http://localhost:5000")
    print(" Фронтенд: http://localhost:8080")
    print("-" * 60)
    print(f" Тестовый пользователь: test@example.com / test123")
    print(f" Пользователей в базе: {len(users_db)}")
    print(f" Броней в базе: {len(bookings_db)}")
    print(f" Машин в каталоге: {len(CARS)}")
    print("=" * 60)
    print(" Логи запросов будут отображаться ниже:")
    print("=" * 60)
    app.run(debug=True, port=5000)