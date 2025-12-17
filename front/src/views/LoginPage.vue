<template>
  <div class="register-page">
    <h2>Вход</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="password">Пароль:</label>
        <input
          type="password"
          id="password"
          placeholder=" (минимум 6 символов)"
          minlength="6"
          v-model="password"
          required
        />
        <router-link to="/recovery">Забыли пароль?</router-link>
      </div>
      <button class="otst" type="submit">Войти</button>
    </form>
    <p>
      Нет аккаунта?
      <router-link to="/register">Зарегистрироваться</router-link>
    </p>
  </div>
</template>

<script>
import apiClient from 'axios';

export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: '',
      errors: {
        name: null,
        surname: null,
        login: null,
        email: null,
        password: null,
        password_confirm: null,
        terms: null,
      },
    };
  },
  computed: {
    hasErrors() {
      return Object.values(this.errors).some((error) => error);
    },
  },
  methods: {
    validateEmail() {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!this.email || !regex.test(this.email)) {
        this.errors.email = 'Некорректный email';
      } else {
        this.errors.email = null;
      }
    },
    validatePassword() {
      if (this.password.length < 6) {
        this.errors.password = 'Пароль должен быть не менее 6 символов';
      } else {
        this.errors.password = null;
      }
    },
  
    async handleLogin() {
      if (this.hasErrors) {
        alert('Пожалуйста, исправьте ошибки в форме');
        return;
      }

      try {
        console.log('Отправка данных для входа...');
        
        // 🔧 ИСПРАВЛЕНИЕ: правильный URL и сохранение данных
        const response = await apiClient.post('http://localhost:5000/api/login', {
          email: this.email,
          password: this.password,
        });
        
        console.log('Ответ от сервера:', response.data);
        
        if(response.data.access_token) {
          // ✅ Сохраняем токен
          localStorage.setItem('access_token', response.data.access_token);
          
          // ✅ Сохраняем данные пользователя
          if (response.data.user) {
            localStorage.setItem('user', JSON.stringify(response.data.user));
          }
          
          // ✅ Переходим в личный кабинет
          this.$router.push('/lk');
          alert('✅ Вы успешно вошли в систему!');
        }
      } catch (error) {
        console.error('Ошибка входа:', error);
        alert(error.response?.data?.error || 'Произошла ошибка входа');
      }
    },
  },
  // УДАЛИТЕ эти строки (они вне компонента и вызывают ошибку):
  // localStorage.setItem('access_token', response.data.access_token);
  // localStorage.setItem('user', JSON.stringify(response.data.user));
};
</script>

<style scoped>
.otst {
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