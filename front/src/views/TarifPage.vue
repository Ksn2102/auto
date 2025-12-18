<template>
  <div class="tarifs-page">
    <main class="main-content">
      <section class="hero-section">
        <h1 class="page-title">Тарифы и цены</h1>
        <p class="page-subtitle">Выберите оптимальный тариф для аренды автомобиля</p>
      </section>
      <section class="tarifs-grid">
        <div class="tarif-card" v-for="tarif in tarifs" :key="tarif.id">
          <div class="tarif-header">
            <h3 class="tarif-name">{{ tarif.name }}</h3>
            <div class="tarif-price">
              <span class="price">{{ tarif.price }}</span>
              <span class="period">{{ tarif.period }}</span>
            </div>
          </div>
          
          <div class="tarif-image">
            <img :src="tarif.image" :alt="tarif.name" />
          </div>
          
          <div class="tarif-features">
            <ul>
              <li v-for="feature in tarif.features" :key="feature">
                <span class="check-icon">✓</span> {{ feature }}
              </li>
            </ul>
          </div>
          
          <div class="tarif-footer">
            <button class="select-btn" @click="selectTarif(tarif)">
              Выбрать тариф
            </button>
          </div>
        </div>
      </section>

      <section class="calculator-section">
        <h2>Рассчитайте стоимость аренды</h2>
        <div class="calculator">
          <div class="calc-inputs">
            <div class="input-group">
              <label>Тариф:</label>
              <select v-model="calcTarif">
                <option v-for="tarif in tarifs" :value="tarif.id" :key="tarif.id">
                  {{ tarif.name }} - {{ tarif.price }}
                </option>
              </select>
            </div>
            <div class="input-group">
              <label>Количество дней:</label>
              <input type="number" v-model="calcDays" min="1" max="30" />
            </div>
            <div class="input-group">
              <label>Автомобиль:</label>
              <select v-model="calcCar">
                <option value="economy">Эконом-класс</option>
                <option value="comfort">Комфорт</option>
                <option value="business">Бизнес</option>
                <option value="premium">Премиум</option>
              </select>
            </div>
          </div>
          <div class="calc-result">
            <div class="result-card">
              <h4>Итоговая стоимость:</h4>
              <div class="total-price">{{ calculateTotal() }} ₽</div>
              <button class="book-btn" @click="goToBooking">Забронировать</button>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: 'TarifsPage',
  data() {
    return {
      tarifs: [
        {
          id: 1,
          name: 'Эконом',
          price: '1 500 ₽',
          period: '/сутки',
          image: require('@/assets/1.png'), 
          features: [
            'До 200 км в сутки',
            'Эконом-класс автомобилей',
            'Базовая страховка',
            'Бесплатная отмена за 24 часа'
          ]
        },
        {
          id: 2,
          name: 'Стандарт',
          price: '2 500 ₽',
          period: '/сутки',
          image: require('@/assets/2.png'),
          features: [
            'Безлимитный пробег',
            'Комфорт-класс автомобилей',
            'Полная страховка',
            'Дополнительный водитель',
            'Бесплатный детское кресло'
          ]
        },
        {
          id: 3,
          name: 'Премиум',
          price: '5 000 ₽',
          period: '/сутки',
          image: require('@/assets/3.png'),
          features: [
            'Безлимитный пробег',
            'Премиум-класс автомобилей',
            'Расширенная страховка',
            'Личный менеджер',
            'Доставка автомобиля',
            'Приоритетная поддержка'
          ]
        },
    
      ],
      activeFaq: null,
      calcTarif: 2, 
      calcDays: 3,
      calcCar: 'comfort'
    }
  },
  methods: {
    selectTarif(tarif) {
      alert(`Вы выбрали тариф "${tarif.name}"!`);

    },
    toggleFaq(index) {
      this.activeFaq = this.activeFaq === index ? null : index;
    },
    calculateTotal() {
      const tarif = this.tarifs.find(t => t.id === this.calcTarif);
      const price = parseInt(tarif.price.replace(/\D/g, ''));
      let multiplier = 1;

      const carMultipliers = {
        'economy': 1,
        'comfort': 1.2,
        'business': 1.5,
        'premium': 2
      };
      
      multiplier = carMultipliers[this.calcCar] || 1;
      
      const total = price * this.calcDays * multiplier;
      return total.toLocaleString('ru-RU');
    },
    goToBooking() {
      this.$router.push('/katalog');
    }
  }
}
</script>

<style scoped>
  @import '@/styles/tarif.css';

</style>