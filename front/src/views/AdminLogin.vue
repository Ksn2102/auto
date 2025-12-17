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
          
          // Сохраняем токен и данные пользователя
          localStorage.setItem('access_token', data.access_token);
          localStorage.setItem('user', JSON.stringify(data.user));
          
          // Переходим в админ-панель
          this.$router.push('/admin');
        } else {
          this.error = data.error || 'Неверные данные';
          alert('Ошибка входа: ' + this.error);
        }
      } catch (error) {
        console.error('❌ Ошибка входа:', error);
        alert('Ошибка соединения с сервером');
      }
    }
  }
};
</script>

<style scoped>
.admin-login {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;

  padding: 20px;
}

.login-box {
  background: white;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 400px;
  text-align: center;
}

.login-box h2 {
  margin-bottom: 10px;
  color: #333;
}

.login-box p {
  color: #666;
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 20px;
  text-align: left;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  color: #555;
  font-weight: 500;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 16px;
  box-sizing: border-box;
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
}

.login-btn {
  width: 100%;
  padding: 14px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
  margin-top: 10px;
}

.login-btn:hover {
  background: #5a6fd8;
}

.credentials {
  margin: 25px 0;
  padding: 15px;
  background: #f8f9fa;
  border-radius: 8px;
  text-align: left;
}

.credentials h4 {
  margin-top: 0;
  color: #333;
}

.credentials p {
  margin: 8px 0;
  color: #555;
}

.back-link {
  display: inline-block;
  margin-top: 20px;
  color: #667eea;
  text-decoration: none;
  font-weight: 500;
}

.back-link:hover {
  text-decoration: underline;
}
</style>