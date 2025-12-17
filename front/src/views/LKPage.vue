<template>
  <div class="lk-simple">
    <h1> МОИ БРОНИРОВАНИЯ</h1>


    
    <div v-if="allBookings.length > 0" class="all-bookings">
      <h3> ВСЕ брони в системе:</h3>
      <div v-for="booking in allBookings" :key="booking.id" 
           :class="['booking-card', booking.user_id == myUserId ? 'my-booking' : 'other-booking']">
        <h4>{{ booking.car_name }} (ID: {{ booking.id }})</h4>
        <p><strong>User ID:</strong> {{ booking.user_id || 'гость' }}</p>
        <p><strong>Клиент:</strong> {{ booking.customer_name }}</p>
        <p><strong>Дата:</strong> {{ booking.date }} {{ booking.time }}</p>
        <p><strong>Статус:</strong> {{ booking.status }}</p>
        <p v-if="booking.user_id == myUserId" class="my-label"> ЭТО МОЯ БРОНЬ!</p>
      </div>
    </div>
    
    <div v-if="myBookings.length > 0" class="my-bookings">
      <h3> МОИ брони (user_id = {{ myUserId }}):</h3>
      <div v-for="booking in myBookings" :key="booking.id" class="my-booking-card">
        <h4> {{ booking.car_name }}</h4>
        <p> {{ booking.date }} в {{ booking.time }}</p>
        <p> {{ booking.phone }}</p>
        <p> {{ booking.comment || 'Без комментария' }}</p>
        <p> ID брони: {{ booking.id }}</p>
      </div>
    </div>
    
    <div v-else class="no-bookings">
      <h3> У вас нет бронирований</h3>
      <p>Попробуйте:</p>
      <ol>
        <li>Залогиньтесь</li>
        <li>Обновите страницу</li>
      </ol>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LKSimple',
  data() {
    return {
      allBookings: [],
      myBookings: [],
      myUserId: null,
      token: null
    };
  },
  async mounted() {
    await this.loadData();
  },
  methods: {
    async loadData() {
      // 1. Получаем токен
      this.token = localStorage.getItem('access_token');
      
      // 2. Если есть токен, получаем user_id
      if (this.token) {
        try {
          const response = await fetch('http://localhost:5000/api/user/profile', {
            headers: { 'Authorization': `Bearer ${this.token}` }
          });
          if (response.ok) {
            const data = await response.json();
            this.myUserId = data.user?.id;
          }
        } catch (error) {
          console.error('Ошибка загрузки профиля:', error);
        }
      }
      
      // 3. Загружаем ВСЕ брони
      await this.loadAllBookings();
      
      // 4. Фильтруем свои брони
      if (this.myUserId) {
        this.myBookings = this.allBookings.filter(b => b.user_id == this.myUserId);
      }
    },
    
    async loadAllBookings() {
      try {
        const response = await fetch('http://localhost:5000/api/debug/all-bookings');
        const data = await response.json();
        this.allBookings = data.bookings || [];
        console.log('Все брони:', this.allBookings);
      } catch (error) {
        console.error('Ошибка загрузки броней:', error);
      }
    },
    
    async loadMyBookings() {
      if (!this.token) {
        alert('Сначала войдите в систему!');
        return;
      }
      
      try {
        const response = await fetch('http://localhost:5000/api/bookings', {
          headers: { 'Authorization': `Bearer ${this.token}` }
        });
        const data = await response.json();
        this.myBookings = data.bookings || [];
        console.log('Мои брони:', this.myBookings);
      } catch (error) {
        console.error('Ошибка загрузки моих броней:', error);
      }
    },
    
    async createTestBooking() {
      if (!this.token) {
        alert('Сначала войдите в систему!');
        return;
      }
      
      const bookingData = {
        carId: 3,
        carName: "BMW Тестовая",
        name: "Тестовый Пользователь",
        phone: "+79998887766",
        email: "test@test.com",
        date: "2024-12-25",
        time: "12:00",
        comment: "Тестовая бронь создана из ЛК"
      };
      
      try {
        const response = await fetch('http://localhost:5000/api/bron', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${this.token}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(bookingData)
        });
        
        const result = await response.json();
        
        if (response.ok) {
          alert(` Тестовая бронь создана! ID: ${result.booking.id}`);
          await this.loadData(); // Обновляем данные
        } else {
          alert(` Ошибка: ${result.error}`);
        }
      } catch (error) {
        console.error('Ошибка создания брони:', error);
        alert(' Ошибка создания брони');
      }
    }
  }
};
</script>

<style scoped>
.lk-simple {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.controls {
  display: flex;
  gap: 10px;
  margin: 20px 0;
  flex-wrap: wrap;
}

.controls button {
  padding: 10px 15px;
  background: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.controls button:hover {
  background: #45a049;
}

.debug-info {
  background: #f5f5f5;
  padding: 15px;
  border-radius: 8px;
  margin: 20px 0;
}

.booking-card {
  border: 1px solid #ddd;
  padding: 15px;
  margin: 10px 0;
  border-radius: 8px;
}

.my-booking {
  border-left: 5px solid #4CAF50;
  background: #f0f9f0;
}

.other-booking {
  border-left: 5px solid #ccc;
  background: #f9f9f9;
}

.my-label {
  color: #4CAF50;
  font-weight: bold;
  margin-top: 10px;
}

.my-booking-card {
  background: #e8f5e9;
  border: 2px solid #4CAF50;
  padding: 20px;
  margin: 15px 0;
  border-radius: 10px;
}

.no-bookings {
  text-align: center;
  padding: 40px;
  background: #fff3cd;
  border-radius: 10px;
  margin-top: 20px;
}
</style>