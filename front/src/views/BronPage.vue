<!-- front/src/pages/BronPage.vue -->
<template>
  <div class="bron-container">
    <!-- Информация о машине -->
    <div v-if="car" class="car-info-section">
      <h2>Бронирование: {{ car.text }}</h2>
      <div class="car-details">
        <img :src="require(`@/assets/${car.img}`)" :alt="car.text" class="bron-car-img">
        <div class="car-specs">
          <p><strong>Цвет:</strong> {{ car.color }}</p>
          <p><strong>Цена:</strong> {{ car.price }} ₽</p>
          <p><strong>Вес:</strong> {{ car.weight }}</p>
          <p><strong>Наличие:</strong> {{ car.availability }}</p>
        </div>
      </div>
    </div>

    <!-- Форма бронирования -->
    <div class="bron-form">
      <h3>Данные для бронирования</h3>
      
      <form @submit.prevent="submitBron">
        <div class="form-group">
          <label for="name">ФИО:</label>
          <input 
            v-model="form.name" 
            type="text" 
            id="name" 
            placeholder="Иванов Иван Иванович"
            required
          >
        </div>
        
        <div class="form-group">
          <label for="phone">Телефон:</label>
          <input 
            v-model="form.phone" 
            type="tel" 
            id="phone" 
            placeholder="+7 (999) 999-99-99"
            required
          >
        </div>
        
        <div class="form-group">
          <label for="email">Email:</label>
          <input 
            v-model="form.email" 
            type="email" 
            id="email" 
            placeholder="example@mail.ru"
            required
          >
        </div>
        
        <div class="form-group">
          <label for="date">Желаемая дата:</label>
          <input 
            v-model="form.date" 
            type="date" 
            id="date" 
            required
          >
        </div>
        
        <div class="form-group">
          <label for="time">Время:</label>
          <input 
            v-model="form.time" 
            type="time" 
            id="time" 
            required
          >
        </div>
        
        <div class="form-group">
          <label for="comment">Комментарий:</label>
          <textarea 
            v-model="form.comment" 
            id="comment" 
            placeholder="Дополнительные пожелания..."
            rows="4"
          ></textarea>
        </div>
        
        <button type="submit" class="submit-bron-btn">
          Подтвердить бронирование
        </button>
      </form>
      
      <!-- Сообщение об успехе -->
      <div v-if="successMessage" class="success-message">
        {{ successMessage }}
      </div>
    </div>
    
    <!-- Кнопка назад -->
    <button @click="goBack" class="back-btn">
      ← Вернуться к машине
    </button>
  </div>
</template>

<script>
export default {
  name: 'BronPage',
  data() {
    return {
      car: null,
      form: {
        name: '',
        phone: '',
        email: '',
        date: '',
        time: '',
        comment: ''
      },
      successMessage: ''
    };
  },
  async mounted() {
    // Загрузка машины
    const carId = parseInt(this.$route.params.id);
    const response = await fetch(`http://localhost:5000/api/cars/${carId}`);
    this.car = await response.json();
    
    // Автозаполнение формы данными пользователя
    const user = JSON.parse(localStorage.getItem('user') || '{}');
    this.form.name = user.first_name ? `${user.first_name} ${user.last_name}`.trim() : '';
    this.form.email = user.email || '';
    this.form.phone = user.phone || '';
  },
  methods: {
    async submitBron() {
      try {
        // 1. Получаем токен из localStorage
        const token = localStorage.getItem('access_token');
        
        if (!token) {
          alert('❌ Для бронирования необходимо войти в систему!');
          this.$router.push('/login');
          return;
        }
        
        // 2. Подготавливаем данные для отправки
        const bookingData = {
          carId: this.car.id,
          carName: this.car.text,
          ...this.form
        };
        
        console.log('📤 Отправка брони с токеном:', token.substring(0, 30) + '...');
        
        // 3. Отправляем запрос с токеном авторизации
        const response = await fetch('http://localhost:5000/api/bron', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(bookingData)
        });
        
        const data = await response.json();
        
        if (response.ok) {
          this.successMessage = `✅ Бронирование "${this.car.text}" успешно создано!`;
          console.log('✅ Бронь создана:', data);
          
          // Очистка формы
          this.form = { name: '', phone: '', email: '', date: '', time: '', comment: '' };
          
          // Автоматический переход через 3 секунды
          setTimeout(() => {
            this.$router.push('/lk');
          }, 3000);
        } else {
          alert(data.error || '❌ Ошибка при бронировании');
        }
      } catch (error) {
        console.error('❌ Ошибка бронирования:', error);
        alert('❌ Произошла ошибка при отправке данных');
      }
    },
    goBack() {
      this.$router.push(`/katalog/${this.car.id}`);
    }
  }
};
</script>

<style scoped>
.bron-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.car-info-section {
  background: #f8f9fa;
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 30px;
}

.car-details {
  display: flex;
  gap: 30px;
  align-items: center;
  margin-top: 20px;
}

.bron-car-img {
  width: 300px;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.car-specs {
  flex: 1;
}

.car-specs p {
  margin: 10px 0;
  font-size: 16px;
}

.bron-form {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 30px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.bron-form h3 {
  margin-bottom: 25px;
  color: #333;
  text-align: center;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #555;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 12px 15px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #7689bc;
  box-shadow: 0 0 0 2px rgba(118, 137, 188, 0.2);
}

.submit-bron-btn {
  width: 100%;
  padding: 15px;
  background: #7689bc;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 10px;
}

.submit-bron-btn:hover {
  background: #5a6e9c;
}

.success-message {
  background: #d4edda;
  color: #155724;
  padding: 15px;
  border-radius: 6px;
  margin-top: 20px;
  text-align: center;
}

.back-btn {
  background: #6c757d;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 6px;
  cursor: pointer;
  margin-top: 30px;
  transition: background-color 0.3s;
}

.back-btn:hover {
  background: #5a6268;
}

@media (max-width: 768px) {
  .car-details {
    flex-direction: column;
    text-align: center;
  }
  
  .bron-car-img {
    width: 100%;
    max-width: 400px;
  }
  
  .bron-container {
    padding: 15px;
  }
}
</style>