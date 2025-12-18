<template>
  <div class="admin-login">
    <div class="login-box">
      <h2> Вход в админ-панель</h2>
      
      <form @submit.prevent="login">
        <div class="form-group">
          <label>Email:</label>
          <input v-model="email" type="email" placeholder="admin@test.com" required>
        </div>
        
        <div class="form-group">
          <label>Пароль:</label>
          <input v-model="password" type="password" placeholder="admin123" required>
        </div>
        
        <button type="submit" class="login-btn">Войти как администратор</button>
      </form>

      
      <router-link to="/login" class="back-link">← Обычный вход</router-link>
    </div>
  </div>
</template>

<script>

export default {
  name: 'AdminLogin',
  data() {
    return {
      email: 'admin@test.com',
      password: 'admin123',
      error: ''
    };
  },
  methods: {
    async login() {
      try {
        console.log('Попытка входа как администратор...');
        
        const response = await fetch('http://localhost:5000/api/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: this.email,
            password: this.password
          })
        });
        
        const data = await response.json();
        
        if (response.ok) {
          console.log(' Вход успешен:', data);

          localStorage.setItem('access_token', data.access_token);
          localStorage.setItem('user', JSON.stringify(data.user));
          
          this.$router.push('/admin');
        } else {
          this.error = data.error || 'Неверные данные';
          alert('Ошибка входа: ' + this.error);
        }
      } catch (error) {
        console.error(' Ошибка входа:', error);
        alert('Ошибка соединения с сервером');
      }
    }
  }
};
</script>

<style scoped>
  @import '@/styles/admin.css';

</style>