<template>
    <div class="register-page">
      <h2>Восстановление пароля</h2>
      <form @submit.prevent="sendResetEmail">
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required />
          <span v-if="errors.email" class="error">{{ errors.email }}</span>
        </div>
  
        <div class="form-group">
          <label for="password">Пароль:</label>
          <input type="password" id="password"  placeholder=" (минимум 6 символов)" minlength="6" v-model="password" required />
        </div>
        <div class="form-group">
          <label for="password">Новый пароль:</label>
          <input type="password" id="password"  placeholder=" (минимум 6 символов)" minlength="6" v-model="password" required />
        </div>
  
        <button class="otst" type="submit">Войти</button>
      </form>

    </div>
  </template>
  
  <script>
//   export default {
//     name: 'LoginPage',
//     data() {
//       return {
//         email: '',
//         password: '',
//       };
//     },
//     methods: {
//       handleLogin() {
//         console.log('Вход:', {
//           email: this.email,
//           password: this.password,
//         });
//         alert('Вы успешно вошли!');
//       },
//     },
//   };
import apiClient from 'axios';

export default {
  data() {
    return {
      email: '',
      errors: {
        email: null,
      },
    };
  },
  methods: {
    async sendResetEmail() {
      if (!this.email) {
        this.errors.email = 'Email обязателен';
        return;
      }

      try {
        const response = await apiClient.post('/forgot-password', { email: this.email });
        alert(response.data.message);
      } catch (error) {
        alert(error.response?.data?.message || 'Произошла ошибка при отправке email');
      }
    },
  },
};
  </script>
  
  <style scoped>
  .otst{
    margin: 15px 0;
    width: 100%;
    padding: 10px;
    background-color: #42b983;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .register-page {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  
  .otst:hover {
    background-color: #38a169;
  }
  </style>