<template>
    <div class="order-list">
      <h1>Список заказов</h1>
      <div class="filters">
        <button @click="filterOrders('new')">Новые</button>
        <button @click="filterOrders('confirmed')">Подтвержденные</button>
        <button @click="filterOrders('canceled')">Отмененные</button>
      </div>
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Таймстамп</th>
            <th>ФИО заказчика</th>
            <th>Количество товаров</th>
            <th>Статус</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(order, index) in filteredOrders" :key="order.id">
            <td>{{ index + 1 }}</td>
            <td>{{ order.timestamp }}</td>
            <td>{{ order.customerName }}</td>
            <td>{{ order.itemCount }}</td>
            <td :class="`status-${order.status}`">{{ order.status }}</td>
            <td>
              <button @click="confirmOrder(order.id)" v-if="order.status === 'new'">Подтвердить</button>
              <button @click="cancelOrder(order.id)" v-if="order.status === 'new'">Отменить</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    
  </template>
  
  <script>
  export default {
    data() {
      return {
        orders: [
          { id: 1, timestamp: '2023-10-01 12:00', customerName: 'Иванов Иван', itemCount: 3, status: 'new' },
          { id: 2, timestamp: '2023-10-02 14:30', customerName: 'Петров Петр', itemCount: 2, status: 'confirmed' },
          { id: 3, timestamp: '2023-10-03 16:45', customerName: 'Сидоров Сергей', itemCount: 1, status: 'canceled' }
        ],
        filter: 'all'
      };
    },
    computed: {
      filteredOrders() {
        if (this.filter === 'all') return this.orders;
        return this.orders.filter(order => order.status === this.filter);
      }
    },
    methods: {
      filterOrders(status) {
        this.filter = status;
      },
      confirmOrder(id) {
        const order = this.orders.find(o => o.id === id);
        if (order) {
          order.status = 'confirmed';
        }
      },
      cancelOrder(id) {
        const order = this.orders.find(o => o.id === id);
        if (order) {
          order.status = 'canceled';
        }
      }
    }
  };
  </script>
  
  <style>
/* Общие настройки */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: #f9fafb;
  color: #333;
  line-height: 1.6;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Шапка */
.header {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header__logo {
  font-size: 24px;
  font-weight: bold;
}

.header__logout {
  background-color: #ff4d4d;
  color: white;
  border: none;
  padding: 8px 16px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.header__logout:hover {
  background-color: #ff7575;
}

/* Сайдбар */
.sidebar {
  background-color: #ffffff;
  width: 250px;
  height: 100%;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.sidebar__menu {
  list-style: none;
  padding: 0;
}

.sidebar__menu li {
  margin-bottom: 10px;
}

.sidebar__menu li a {
  display: block;
  padding: 10px 15px;
  text-decoration: none;
  color: #333;
  border-radius: 4px;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.sidebar__menu li a.active,
.sidebar__menu li a:hover {
  background-color: #e0e0e0;
  color: #000;
}

.content {
  flex-grow: 1;
  padding: 20px;
  overflow-y: auto;
  background-color: #ffffff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-left: 30px;
  border-radius: 8px;
}

.content__title {
  font-size: 24px;
  margin-bottom: 20px;
  color: #2c3e50;
}

/* Форма добавления автомобиля */
.add-car form {
  margin-bottom: 20px;
}

.add-car label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.add-car input,
.add-car select,
.add-car textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

.add-car button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 4px;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}

.add-car button:hover {
  background-color: #45a049;
}

/* Таблица заказов */
.order-list table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.order-list th,
.order-list td {
  padding: 12px;
  border: 1px solid #ddd;
  text-align: left;
}

.order-list th {
  background-color: #f4f4f4;
  font-weight: bold;
  color: #333;
}

.order-list tr:nth-child(even) {
  background-color: #f9f9f9;
}

.order-list tr:hover {
  background-color: #f1f1f1;
}

.order-list .status-new {
  color: orange;
  font-weight: bold;
}

.order-list .status-confirmed {
  color: green;
  font-weight: bold;
}

.order-list .status-canceled {
  color: red;
  font-weight: bold;
}

.order-list button {
  background-color: #ff4d4d;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 4px;
  margin-right: 5px;
  transition: background-color 0.3s ease;
}

.order-list button.confirm {
  background-color: #4CAF50;
}

.order-list button.cancel {
  background-color: #ff4d4d;
}

.order-list button.confirm:hover {
  background-color: #45a049;
}

.order-list button.cancel:hover {
  background-color: #ff7575;
}

/* Фильтры */
.filters {
  margin-bottom: 20px;
  display: flex;
  gap: 10px;
}

.filters button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.filters button:hover {
  background-color: #0056b3;
}

/* Адаптивность */
@media (max-width: 768px) {
  .sidebar {
    width: 100%;
    margin-bottom: 20px;
  }

  .content {
    margin-left: 0;
  }

  .filters {
    flex-wrap: wrap;
  }
}
  </style>
