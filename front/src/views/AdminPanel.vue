<template>
  <div class="admin-panel">
    <!-- Шапка админки -->
    <header class="admin-header">
      <h1> Панель администратора</h1>
      <div class="admin-info">
        <span>Администратор: {{ adminEmail }}</span>
        <button @click="logout" class="logout-btn">Выйти</button>
      </div>
    </header>

    <!-- Навигация -->
    <nav class="admin-nav">
      <button 
        v-for="tab in tabs" 
        :key="tab.id"
        :class="{ active: activeTab === tab.id }"
        @click="activeTab = tab.id"
        class="nav-btn"
      >
        {{ tab.icon }} {{ tab.name }}
      </button>
    </nav>

    <!-- Основной контент -->
    <main class="admin-content">
      <!-- Управление бронированиями -->
      <section v-if="activeTab === 'bookings'" class="tab-content">
        <div class="tab-header">
          <h2> Управление бронированиями</h2>
          <div class="controls">
            <input v-model="bookingFilter" placeholder="Поиск по клиенту или машине..." class="search-input">
            <select v-model="bookingStatusFilter" class="filter-select">
              <option value="">Все статусы</option>
              <option value="pending">Ожидает</option>
              <option value="confirmed">Подтверждено</option>
              <option value="cancelled">Отменено</option>
              <option value="completed">Завершено</option>
            </select>
          </div>
        </div>

        <div class="stats-cards">
          <div class="stat-card">
            <div class="stat-value">{{ bookings.length }}</div>
            <div class="stat-label">Всего броней</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ pendingBookings.length }}</div>
            <div class="stat-label">Ожидают</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ confirmedBookings.length }}</div>
            <div class="stat-label">Подтверждены</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ totalRevenue }}</div>
            <div class="stat-label">Выручка</div>
          </div>
        </div>

        <div class="table-container">
          <table class="admin-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Клиент</th>
                <th>Машина</th>
                <th>Дата/Время</th>
                <th>Телефон</th>
                <th>Статус</th>
                <th>Действия</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="booking in filteredBookings" :key="booking.id">
                <td>#{{ booking.id }}</td>
                <td>
                  <div>{{ booking.customer_name }}</div>
                  <small>{{ booking.email }}</small>
                </td>
                <td>{{ booking.car_name }}</td>
                <td>
                  <div>{{ booking.date }}</div>
                  <small>{{ booking.time }}</small>
                </td>
                <td>{{ booking.phone }}</td>
                <td>
                  <span :class="'status-' + booking.status" class="status-badge">
                    {{ getStatusText(booking.status) }}
                  </span>
                </td>
                <td>
                  <div class="action-buttons">
                    <button @click="changeBookingStatus(booking.id, 'confirmed')" 
                            v-if="booking.status === 'pending'" 
                            class="btn-success">
                      Подтвердить
                    </button>
                    <button @click="changeBookingStatus(booking.id, 'cancelled')" 
                            v-if="booking.status !== 'cancelled'" 
                            class="btn-danger">
                      Отменить
                    </button>
                    <button @click="editBooking(booking)" class="btn-edit">
                      
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Управление автопарком -->
      <section v-if="activeTab === 'cars'" class="tab-content">
        <div class="tab-header">
          <h2> Управление автопарком</h2>
          <button @click="showAddCarModal = true" class="btn-primary">
            + Добавить авто
          </button>
        </div>

        <div class="stats-cards">
          <div class="stat-card">
            <div class="stat-value">{{ cars.length }}</div>
            <div class="stat-label">Всего авто</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ availableCars.length }}</div>
            <div class="stat-label">Доступно</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ rentedCars.length }}</div>
            <div class="stat-label">В аренде</div>
          </div>
        </div>

        <div class="cards-grid">
          <div v-for="car in cars" :key="car.id" class="car-card">
            <div class="car-image">
              <img :src="require(`@/assets/${car.img}`)" :alt="car.text">
              <span :class="car.availability === 'В наличии' ? 'status-available' : 'status-unavailable'" 
                    class="car-status">
                {{ car.availability }}
              </span>
            </div>
            <div class="car-info">
              <h3>{{ car.text }}</h3>
              <p class="car-price">{{ car.price }} ₽</p>
              <p>Цвет: {{ car.color }}</p>
              <p>Вес: {{ car.weight }}</p>
              <div class="car-actions">
                <button @click="editCar(car)" class="btn-edit">Редактировать</button>
                <button @click="toggleCarAvailability(car)" 
                        :class="car.availability === 'В наличии' ? 'btn-disable' : 'btn-enable'">
                  {{ car.availability === 'В наличии' ? 'Снять с продажи' : 'Вернуть в продажу' }}
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Управление клиентами -->
      <section v-if="activeTab === 'users'" class="tab-content">
        <div class="tab-header">
          <h2> Управление клиентами</h2>
          <input v-model="userSearch" placeholder="Поиск по email или имени..." class="search-input">
        </div>

        <div class="table-container">
          <table class="admin-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Имя</th>
                <th>Email</th>
                <th>Телефон</th>
                <th>Дата регистрации</th>
                <th>Кол-во броней</th>
                <th>Действия</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in filteredUsers" :key="user.id">
                <td>#{{ user.id }}</td>
                <td>{{ user.first_name }} {{ user.last_name }}</td>
                <td>{{ user.email }}</td>
                <td>{{ user.phone || 'Не указан' }}</td>
                <td>{{ formatDate(user.created_at) }}</td>
                <td>{{ getUserBookingsCount(user.id) }}</td>
                <td>
                  <button @click="viewUserDetails(user)" class="btn-view">
                    Просмотр
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Финансы и тарифы -->
      <section v-if="activeTab === 'finances'" class="tab-content">
        <div class="tab-header">
          <h2> Финансы и тарифы</h2>
          <button @click="showAddTariffModal = true" class="btn-primary">
            + Добавить тариф
          </button>
        </div>

        <div class="stats-cards">
          <div class="stat-card">
            <div class="stat-value">{{ totalRevenue }} ₽</div>
            <div class="stat-label">Общая выручка</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ completedBookings.length }}</div>
            <div class="stat-label">Завершенных броней</div>
          </div>
          <div class="stat-card">
            <div class="stat-value">{{ averageBookingValue }} ₽</div>
            <div class="stat-label">Средний чек</div>
          </div>
        </div>

        <div class="tariffs-section">
          <h3> Текущие тарифы</h3>
          <div class="tariffs-grid">
            <div v-for="tariff in tariffs" :key="tariff.id" class="tariff-card">
              <h4>{{ tariff.name }}</h4>
              <div class="tariff-price">{{ tariff.price }}</div>
              <div class="tariff-period">{{ tariff.period }}</div>
              <ul class="tariff-features">
                <li v-for="feature in tariff.features" :key="feature">{{ feature }}</li>
              </ul>
              <div class="tariff-actions">
                <button @click="editTariff(tariff)" class="btn-edit">Редактировать</button>
                <button @click="deleteTariff(tariff.id)" class="btn-danger">Удалить</button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- Модальное окно добавления авто -->
    <div v-if="showAddCarModal" class="modal-overlay">
      <div class="modal">
        <h3>Добавить новый автомобиль</h3>
        <form @submit.prevent="addNewCar">
          <div class="form-row">
            <div class="form-group">
              <label>Марка *</label>
              <input v-model="newCar.brand" required>
            </div>
            <div class="form-group">
              <label>Модель *</label>
              <input v-model="newCar.model" required>
            </div>
          </div>
          
          <div class="form-group">
            <label>Описание</label>
            <textarea v-model="newCar.description" rows="3"></textarea>
          </div>
          
          <div class="form-row">
            <div class="form-group">
              <label>Цена (₽) *</label>
              <input v-model="newCar.price" type="number" required>
            </div>
            <div class="form-group">
              <label>Цвет</label>
              <input v-model="newCar.color">
            </div>
          </div>
          
          <div class="form-buttons">
            <button type="submit" class="btn-primary">Добавить</button>
            <button type="button" @click="showAddCarModal = false" class="btn-cancel">Отмена</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Модальное окно редактирования брони -->
    <div v-if="editingBooking" class="modal-overlay">
      <div class="modal">
        <h3>Редактирование брони #{{ editingBooking.id }}</h3>
        <!-- Форма редактирования -->
        <button @click="editingBooking = null" class="btn-cancel">Закрыть</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminPanel',
  data() {
    return {
      activeTab: 'bookings',
      adminEmail: 'admin@test.com',
      
      // Бронирования
      bookings: [],
      bookingFilter: '',
      bookingStatusFilter: '',
      
      // Автомобили
      cars: [],
      showAddCarModal: false,
      newCar: {
        brand: '',
        model: '',
        description: '',
        price: '',
        color: ''
      },
      
      // Пользователи
      users: [],
      userSearch: '',
      
      // Тарифы
      tariffs: [
        { id: 1, name: 'Эконом', price: '1 500 ₽', period: '/сутки', features: ['До 200 км/сутки', 'Базовая страховка'] },
        { id: 2, name: 'Стандарт', price: '2 500 ₽', period: '/сутки', features: ['Безлимитный пробег', 'Полная страховка'] },
        { id: 3, name: 'Премиум', price: '5 000 ₽', period: '/сутки', features: ['Безлимитный пробег', 'Премиум сервис'] }
      ],
      showAddTariffModal: false,
      
      // Редактирование
      editingBooking: null,
      editingCar: null,
      editingTariff: null,
      
      // Вкладки
      tabs: [
        { id: 'bookings', name: 'Бронирования', icon: '' },
        { id: 'cars', name: 'Автопарк', icon: '' },
        { id: 'users', name: 'Клиенты', icon: '' },
        { id: 'finances', name: 'Финансы', icon: '' }
      ]
    };
  },
  computed: {
    // Фильтрация бронирований
    filteredBookings() {
      let filtered = [...this.bookings];
      
      if (this.bookingFilter) {
        const search = this.bookingFilter.toLowerCase();
        filtered = filtered.filter(b => 
          b.customer_name.toLowerCase().includes(search) ||
          b.car_name.toLowerCase().includes(search) ||
          b.email.toLowerCase().includes(search)
        );
      }
      
      if (this.bookingStatusFilter) {
        filtered = filtered.filter(b => b.status === this.bookingStatusFilter);
      }
      
      return filtered.sort((a, b) => b.id - a.id);
    },
    
    // Статистика бронирований
    pendingBookings() {
      return this.bookings.filter(b => b.status === 'pending');
    },
    
    confirmedBookings() {
      return this.bookings.filter(b => b.status === 'confirmed');
    },
    
    completedBookings() {
      return this.bookings.filter(b => b.status === 'completed');
    },
    
    totalRevenue() {
      // Простой расчет (можно улучшить)
      return this.completedBookings.length * 5000;
    },
    
    // Автомобили
    availableCars() {
      return this.cars.filter(c => c.availability === 'В наличии');
    },
    
    rentedCars() {
      return this.cars.filter(c => c.availability !== 'В наличии');
    },
    
    // Пользователи
    filteredUsers() {
      if (!this.userSearch) return this.users;
      
      const search = this.userSearch.toLowerCase();
      return this.users.filter(u => 
        u.email.toLowerCase().includes(search) ||
        (u.first_name + ' ' + u.last_name).toLowerCase().includes(search)
      );
    },
    
    // Финансы
    averageBookingValue() {
      if (this.completedBookings.length === 0) return 0;
      return Math.round(this.totalRevenue / this.completedBookings.length);
    }
  },
  async mounted() {
    // Проверка авторизации администратора
    await this.checkAdminAuth();
    
    // Загрузка данных
    await this.loadAllData();
  },
  methods: {
    async checkAdminAuth() {
      const token = localStorage.getItem('access_token');
      const user = JSON.parse(localStorage.getItem('user') || '{}');
      
      // Простая проверка - можно улучшить
      if (!token || user.email !== 'admin@test.com') {
        alert('Доступ только для администраторов!');
        this.$router.push('/login');
      }
    },
    
    async loadAllData() {
      try {
        
        
        // Загрузка бронирований
        const bookingsResponse = await fetch('http://localhost:5000/api/debug/all-bookings');
        const bookingsData = await bookingsResponse.json();
        this.bookings = bookingsData.bookings || [];
        
        // Загрузка автомобилей (пока из вашего JSON)
        const carsResponse = await fetch('http://localhost:5000/api/cars');
        this.cars = await carsResponse.json();
        
        // Загрузка пользователей
        const usersResponse = await fetch('http://localhost:5000/api/debug/users');
        const usersData = await usersResponse.json();
        this.users = usersData.users || [];
        
      } catch (error) {
        console.error('Ошибка загрузки данных:', error);
      }
    },
    
    getStatusText(status) {
      const statusMap = {
        'pending': 'Ожидает',
        'confirmed': 'Подтверждено',
        'cancelled': 'Отменено',
        'completed': 'Завершено'
      };
      return statusMap[status] || status;
    },
    
    async changeBookingStatus(bookingId, newStatus) {
      try {
        
        // В реальном приложении здесь будет вызов API
        const booking = this.bookings.find(b => b.id === bookingId);
        if (booking) {
          booking.status = newStatus;
          
          // Здесь должен быть вызов к бэкенду для сохранения изменений
          // await fetch(`/api/bookings/${bookingId}/status`, {
          //   method: 'PUT',
          //   headers: { 'Authorization': `Bearer ${token}` },
          //   body: JSON.stringify({ status: newStatus })
          // });
          
          alert(`Статус брони #${bookingId} изменен на "${this.getStatusText(newStatus)}"`);
        }
      } catch (error) {
        console.error('Ошибка изменения статуса:', error);
        alert('Ошибка при изменении статуса');
      }
    },
    
    editBooking(booking) {
      this.editingBooking = { ...booking };
    },
    
    toggleCarAvailability(car) {
      car.availability = car.availability === 'В наличии' ? 'Не доступно' : 'В наличии';
      // Здесь должен быть вызов API для сохранения изменений
    },
    
    async addNewCar() {
      try {
        
        // Создаем новый автомобиль
        const newCarData = {
          ...this.newCar,
          id: this.cars.length + 1,
          img: 'default-car.jpg',
          text: `${this.newCar.brand} ${this.newCar.model}`,
          availability: 'В наличии',
          weight: '2 т',
          button: 'Подробнее',
          opic: this.newCar.description
        };
        
        // Здесь должен быть вызов API для создания автомобиля
        // await fetch('/api/admin/cars', {
        //   method: 'POST',
        //   headers: { 'Authorization': `Bearer ${token}` },
        //   body: JSON.stringify(newCarData)
        // });
        
        this.cars.push(newCarData);
        this.showAddCarModal = false;
        this.newCar = { brand: '', model: '', description: '', price: '', color: '' };
        
        alert('Автомобиль успешно добавлен!');
        
      } catch (error) {
        console.error('Ошибка добавления автомобиля:', error);
        alert('Ошибка при добавлении автомобиля');
      }
    },
    
    getUserBookingsCount(userId) {
      return this.bookings.filter(b => b.user_id === userId).length;
    },
    
    formatDate(dateString) {
      if (!dateString) return '—';
      return new Date(dateString).toLocaleDateString('ru-RU');
    },
    
    viewUserDetails(user) {
      alert(`Детали пользователя:\n\nИмя: ${user.first_name} ${user.last_name}\nEmail: ${user.email}\nТелефон: ${user.phone || 'Не указан'}\nБроней: ${this.getUserBookingsCount(user.id)}`);
    },
    
    editTariff(tariff) {
      this.editingTariff = { ...tariff };
    },
    
    deleteTariff(tariffId) {
      if (confirm('Удалить этот тариф?')) {
        this.tariffs = this.tariffs.filter(t => t.id !== tariffId);
      }
    },
    
    logout() {
      localStorage.removeItem('access_token');
      localStorage.removeItem('user');
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
.admin-panel {
  min-height: 100vh;
  background: #f5f7fa;
}

.admin-header {
  color: white;
  padding: 20px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.admin-info {
  display: flex;
  align-items: center;
  gap: 20px;
}

.logout-btn {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
}

.logout-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}

.admin-nav {
  background: white;
  padding: 15px 30px;
  display: flex;
  gap: 10px;
  border-bottom: 1px solid #eaeaea;
}

.nav-btn {
  padding: 12px 24px;
  background: none;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-btn:hover {
  background: #f5f5f5;
}

.nav-btn.active {
  background: #667eea;
  color: white;
  border-color: #667eea;
}

.admin-content {
  padding: 30px;
}

.tab-content {
  background: white;
  border-radius: 12px;
  padding: 25px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.tab-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
  flex-wrap: wrap;
  gap: 15px;
}

.search-input {
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  min-width: 250px;
}

.filter-select {
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: white;
}

.stats-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin: 25px 0;
}

.stat-card {
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  padding: 20px;
  border-radius: 10px;
  text-align: center;
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
  color: #2c3e50;
}

.stat-label {
  color: #7f8c8d;
  margin-top: 5px;
}

.table-container {
  overflow-x: auto;
  margin-top: 20px;
}

.admin-table {
  width: 100%;
  border-collapse: collapse;
}

.admin-table th {
  background: #f8f9fa;
  padding: 15px;
  text-align: left;
  border-bottom: 2px solid #eaeaea;
  font-weight: 600;
  color: #555;
}

.admin-table td {
  padding: 15px;
  border-bottom: 1px solid #eee;
}

.status-badge {
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 500;
}

.status-pending { background: #fff3cd; color: #856404; }
.status-confirmed { background: #d4edda; color: #155724; }
.status-cancelled { background: #f8d7da; color: #721c24; }
.status-completed { background: #cce5ff; color: #004085; }

.action-buttons {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.btn-success, .btn-danger, .btn-edit, .btn-primary, .btn-cancel {
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
}

.btn-success { background: #28a745; color: white; }
.btn-danger { background: #dc3545; color: white; }
.btn-edit { background: #ffc107; color: #333; }
.btn-primary { background: #007bff; color: white; }
.btn-cancel { background: #6c757d; color: white; }

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 25px;
  margin-top: 25px;
}

.car-card {
  border: 1px solid #eaeaea;
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.3s, box-shadow 0.3s;
}

.car-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.car-image {
  position: relative;
  height: 180px;
  overflow: hidden;
}

.car-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.car-status {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 5px 10px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.status-available { background: #28a745; color: white; }
.status-unavailable { background: #dc3545; color: white; }

.car-info {
  padding: 20px;
}

.car-price {
  font-size: 1.5rem;
  font-weight: bold;
  color: #28a745;
  margin: 10px 0;
}

.car-actions {
  display: flex;
  gap: 10px;
  margin-top: 15px;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  background: white;
  padding: 30px;
  border-radius: 12px;
  max-width: 500px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
}

.form-row {
  display: flex;
  gap: 15px;
  margin-bottom: 15px;
}

.form-group {
  flex: 1;
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
  color: #555;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 16px;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
}

.form-buttons {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
  margin-top: 25px;
}

.tariffs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.tariff-card {
  border: 1px solid #eaeaea;
  border-radius: 10px;
  padding: 20px;
  text-align: center;
}

.tariff-price {
  font-size: 2rem;
  font-weight: bold;
  color: #28a745;
  margin: 10px 0;
}

.tariff-period {
  color: #7f8c8d;
  margin-bottom: 15px;
}

.tariff-features {
  list-style: none;
  padding: 0;
  text-align: left;
  margin: 15px 0;
}

.tariff-features li {
  padding: 5px 0;
  border-bottom: 1px solid #f5f5f5;
}

.tariff-actions {
  margin-top: 20px;
  display: flex;
  gap: 10px;
  justify-content: center;
}

.btn-view {
  background: #17a2b8;
  color: white;
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-disable {
  background: #ffc107;
  color: #333;
}

.btn-enable {
  background: #28a745;
  color: white;
}

@media (max-width: 768px) {
  .admin-header {
    flex-direction: column;
    text-align: center;
    gap: 15px;
  }
  
  .admin-nav {
    overflow-x: auto;
    flex-wrap: nowrap;
    padding: 10px;
  }
  
  .tab-header {
    flex-direction: column;
    align-items: stretch;
  }
  
  .search-input {
    min-width: 100%;
  }
  
  .form-row {
    flex-direction: column;
  }
}
</style>