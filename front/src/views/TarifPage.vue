<template>
  <div class="tarifs-page">
    <!-- Хедер (используйте свой компонент Header) -->
    <!-- <Header /> -->
    
    <main class="main-content">
      <!-- Заголовок страницы -->
      <section class="hero-section">
        <h1 class="page-title">Тарифы и цены</h1>
        <p class="page-subtitle">Выберите оптимальный тариф для аренды автомобиля</p>
      </section>
      
      <!-- Сетка тарифов -->
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
      
      <!-- Дополнительная информация -->
      <section class="additional-info">
        <div class="info-card">
          <h3>Что включено во все тарифы?</h3>
          <div class="included-list">
            <div class="included-item">
              <span class="icon">🛡️</span>
              <div>
                <h4>Страховка</h4>
                <p>Полная страховка от ущерба и угона</p>
              </div>
            </div>
            <div class="included-item">
              <span class="icon">⛽</span>
              <div>
                <h4>Топливо</h4>
                <p>Полный бак при получении автомобиля</p>
              </div>
            </div>
            <div class="included-item">
              <span class="icon">📞</span>
              <div>
                <h4>Круглосуточная поддержка</h4>
                <p>Техническая помощь 24/7</p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="info-card faq">
          <h3>Частые вопросы</h3>
          <div class="faq-item">
            <div class="faq-question" @click="toggleFaq(0)">
              <span>Можно ли изменить тариф после бронирования?</span>
              <span class="faq-icon">{{ activeFaq === 0 ? '−' : '+' }}</span>
            </div>
            <div class="faq-answer" v-if="activeFaq === 0">
              <p>Да, вы можете изменить тариф за 24 часа до начала аренды без дополнительных комиссий.</p>
            </div>
          </div>
          <div class="faq-item">
            <div class="faq-question" @click="toggleFaq(1)">
              <span>Есть ли ограничения по пробегу?</span>
              <span class="faq-icon">{{ activeFaq === 1 ? '−' : '+' }}</span>
            </div>
            <div class="faq-answer" v-if="activeFaq === 1">
              <p>В тарифе "Эконом" есть ограничение 200 км в сутки. В остальных тарифах пробег не ограничен.</p>
            </div>
          </div>
          <div class="faq-item">
            <div class="faq-question" @click="toggleFaq(2)">
              <span>Нужен ли залог?</span>
              <span class="faq-icon">{{ activeFaq === 2 ? '−' : '+' }}</span>
            </div>
            <div class="faq-answer" v-if="activeFaq === 2">
              <p>Да, залог составляет 10 000 ₽. Возвращается в течение 3 дней после завершения аренды.</p>
            </div>
          </div>
        </div>
      </section>
      
      <!-- Калькулятор стоимости -->
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
    
    <!-- Футер (используйте свой компонент Footer) -->
    <!-- <Footer /> -->
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
          image: require('@/assets/1.png'), // Замените на свои изображения
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
        {
          id: 4,
          name: 'Бизнес',
          price: '3 500 ₽',
          period: '/сутки',
          image: require('@/assets/4.png'),
          features: [
            'Безлимитный пробег',
            'Бизнес-класс автомобилей',
            'Полная страховка',
            'Дополнительный водитель',
            'Wi-Fi в автомобиле',
            'Помощь с багажом'
          ]
        }
      ],
      activeFaq: null,
      calcTarif: 2, // Стандарт по умолчанию
      calcDays: 3,
      calcCar: 'comfort'
    }
  },
  methods: {
    selectTarif(tarif) {
      alert(`Вы выбрали тариф "${tarif.name}"!`);
      // Можно добавить логику выбора тарифа
      // Например, сохранение в store или переход к бронированию
    },
    toggleFaq(index) {
      this.activeFaq = this.activeFaq === index ? null : index;
    },
    calculateTotal() {
      const tarif = this.tarifs.find(t => t.id === this.calcTarif);
      const price = parseInt(tarif.price.replace(/\D/g, ''));
      let multiplier = 1;
      
      // Множитель в зависимости от класса авто
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
.tarifs-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  width: 100%;
}

/* Герой-секция */
.hero-section {
  text-align: center;
  padding: 40px 20px;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  border-radius: 15px;
  margin-bottom: 40px;
}

.page-title {
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 10px;
}

.page-subtitle {
  font-size: 1.2rem;
  color: #7f8c8d;
  max-width: 600px;
  margin: 0 auto;
}

/* Сетка тарифов */
.tarifs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
  margin-bottom: 50px;
}

.tarif-card {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
}

.tarif-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.tarif-header {
  background: #7689bc;
  color: white;
  padding: 20px;
  text-align: center;
}

.tarif-name {
  font-size: 1.5rem;
  margin: 0 0 10px 0;
}

.tarif-price {
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 5px;
}

.price {
  font-size: 2rem;
  font-weight: bold;
}

.period {
  font-size: 1rem;
  opacity: 0.9;
}

.tarif-image {
  height: 180px;
  overflow: hidden;
}

.tarif-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.tarif-card:hover .tarif-image img {
  transform: scale(1.05);
}

.tarif-features {
  padding: 20px;
  flex: 1;
}

.tarif-features ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.tarif-features li {
  padding: 8px 0;
  display: flex;
  align-items: center;
  color: #555;
}

.check-icon {
  color: #4CAF50;
  font-weight: bold;
  margin-right: 10px;
  font-size: 1.2rem;
}

.tarif-footer {
  padding: 20px;
  border-top: 1px solid #eee;
}

.select-btn {
  width: 100%;
  padding: 15px;
  background: #7689bc;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.select-btn:hover {
  background: #5a6e9c;
}

/* Дополнительная информация */
.additional-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-bottom: 50px;
}

.info-card {
  background: white;
  border-radius: 15px;
  padding: 30px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
}

.info-card h3 {
  color: #2c3e50;
  margin-bottom: 20px;
  font-size: 1.5rem;
}

.included-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.included-item {
  display: flex;
  align-items: flex-start;
  gap: 15px;
}

.included-item .icon {
  font-size: 1.5rem;
  flex-shrink: 0;
}

.included-item h4 {
  margin: 0 0 5px 0;
  color: #34495e;
}

.included-item p {
  margin: 0;
  color: #7f8c8d;
  font-size: 0.95rem;
}

/* FAQ */
.faq-item {
  border-bottom: 1px solid #eee;
  margin-bottom: 15px;
}

.faq-question {
  padding: 15px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  font-weight: 500;
  color: #2c3e50;
}

.faq-question:hover {
  color: #7689bc;
}

.faq-icon {
  font-size: 1.2rem;
  font-weight: bold;
  color: #7689bc;
}

.faq-answer {
  padding: 0 0 15px 0;
  color: #7f8c8d;
  line-height: 1.6;
}

/* Калькулятор */
.calculator-section {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  border-radius: 15px;
  padding: 40px;
  margin-bottom: 50px;
}

.calculator-section h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #2c3e50;
}

.calculator {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
}

.calc-inputs {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.input-group label {
  font-weight: 500;
  color: #555;
}

.input-group select,
.input-group input {
  padding: 12px 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.input-group select:focus,
.input-group input:focus {
  outline: none;
  border-color: #7689bc;
  box-shadow: 0 0 0 2px rgba(118, 137, 188, 0.2);
}

.calc-result {
  display: flex;
  align-items: center;
  justify-content: center;
}

.result-card {
  background: white;
  border-radius: 15px;
  padding: 30px;
  text-align: center;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 300px;
}

.result-card h4 {
  margin-bottom: 20px;
  color: #555;
}

.total-price {
  font-size: 2.5rem;
  font-weight: bold;
  color: #7689bc;
  margin-bottom: 25px;
}

.book-btn {
  width: 100%;
  padding: 15px;
  background: #4CAF50;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.book-btn:hover {
  background: #45a049;
}

/* Адаптивность */
@media (max-width: 768px) {
  .calculator {
    grid-template-columns: 1fr;
  }
  
  .page-title {
    font-size: 2rem;
  }
  
  .additional-info {
    grid-template-columns: 1fr;
  }
  
  .tarifs-grid {
    grid-template-columns: 1fr;
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
  }
}

@media (max-width: 480px) {
  .main-content {
    padding: 15px;
  }
  
  .hero-section {
    padding: 30px 15px;
  }
  
  .calculator-section {
    padding: 25px;
  }
}
</style>