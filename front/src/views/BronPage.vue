<template>
  <div class="bron-container">
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

      <div v-if="successMessage" class="success-message">
        {{ successMessage }}
      </div>
    </div>

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
    const carId = parseInt(this.$route.params.id);
    const response = await fetch(`http://localhost:5000/api/cars/${carId}`);
    this.car = await response.json();

    const user = JSON.parse(localStorage.getItem('user') || '{}');
    this.form.name = user.first_name ? `${user.first_name} ${user.last_name}`.trim() : '';
    this.form.email = user.email || '';
    this.form.phone = user.phone || '';
  },
  methods: {
    async submitBron() {
      try {
        const token = localStorage.getItem('access_token');
        
        if (!token) {
          alert(' Для бронирования необходимо войти в систему!');
          this.$router.push('/login');
          return;
        }

        const bookingData = {
          carId: this.car.id,
          carName: this.car.text,
          ...this.form
        };
        
        console.log(' Отправка брони с токеном:', token.substring(0, 30) + '...');

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
          this.successMessage = ` Бронирование "${this.car.text}" успешно создано!`;
          console.log(' Бронь создана:', data);

          this.form = { name: '', phone: '', email: '', date: '', time: '', comment: '' };

          setTimeout(() => {
            this.$router.push('/lk');
          }, 3000);
        } else {
          alert(data.error || ' Ошибка при бронировании');
        }
      } catch (error) {
        console.error(' Ошибка бронирования:', error);
        alert(' Произошла ошибка при отправке данных');
      }
    },
    goBack() {
      this.$router.push(`/katalog/${this.car.id}`);
    }
  }
};
</script>

<style scoped>
  @import '@/styles/tarif.css';

</style>