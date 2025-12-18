<template>
  <div class="admin-panel">
    <header class="admin-header">
      <h1> Панель администратора</h1>
      <div class="admin-info">
        <span>Администратор: {{ adminEmail }}</span>
        <button @click="logout" class="logout-btn">Выйти</button>
      </div>
    </header>

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

    <main class="admin-content">
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

    <div v-if="editingBooking" class="modal-overlay">
      <div class="modal">
        <h3>Редактирование брони #{{ editingBooking.id }}</h3>
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

      bookings: [],
      bookingFilter: '',
      bookingStatusFilter: '',

      cars: [],
      showAddCarModal: false,
      newCar: {
        brand: '',
        model: '',
        description: '',
        price: '',
        color: ''
      },

      users: [],
      userSearch: '',

      tariffs: [
        { id: 1, name: 'Эконом', price: '1 500 ₽', period: '/сутки', features: ['До 200 км/сутки', 'Базовая страховка'] },
        { id: 2, name: 'Стандарт', price: '2 500 ₽', period: '/сутки', features: ['Безлимитный пробег', 'Полная страховка'] },
        { id: 3, name: 'Премиум', price: '5 000 ₽', period: '/сутки', features: ['Безлимитный пробег', 'Премиум сервис'] }
      ],
      showAddTariffModal: false,

      editingBooking: null,
      editingCar: null,
      editingTariff: null,
      
      tabs: [
        { id: 'bookings', name: 'Бронирования' },
        { id: 'cars', name: 'Автопарк' },
        { id: 'users', name: 'Клиенты' },
        { id: 'finances', name: 'Финансы' }
      ]
    };
  },
  computed: {
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
      return this.completedBookings.length * 5000;
    },

    availableCars() {
      return this.cars.filter(c => c.availability === 'В наличии');
    },
    
    rentedCars() {
      return this.cars.filter(c => c.availability !== 'В наличии');
    },

    filteredUsers() {
      if (!this.userSearch) return this.users;
      
      const search = this.userSearch.toLowerCase();
      return this.users.filter(u => 
        u.email.toLowerCase().includes(search) ||
        (u.first_name + ' ' + u.last_name).toLowerCase().includes(search)
      );
    },

    averageBookingValue() {
      if (this.completedBookings.length === 0) return 0;
      return Math.round(this.totalRevenue / this.completedBookings.length);
    }
  },
  async mounted() {
    await this.checkAdminAuth();

    await this.loadAllData();
  },
  methods: {
    async checkAdminAuth() {
      const token = localStorage.getItem('access_token');
      const user = JSON.parse(localStorage.getItem('user') || '{}');

      if (!token || user.email !== 'admin@test.com') {
        alert('Доступ только для администраторов!');
        this.$router.push('/login');
      }
    },
    
    async loadAllData() {
      try {

        const bookingsResponse = await fetch('http://localhost:5000/api/debug/all-bookings');
        const bookingsData = await bookingsResponse.json();
        this.bookings = bookingsData.bookings || [];

        const carsResponse = await fetch('http://localhost:5000/api/cars');
        this.cars = await carsResponse.json();

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

        const booking = this.bookings.find(b => b.id === bookingId);
        if (booking) {
          booking.status = newStatus;
          
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
    },
    
    async addNewCar() {
      try {

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
  @import '@/styles/admin.css';

</style>