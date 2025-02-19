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
        <input type="password" id="password"  placeholder=" (минимум 6 символов)" minlength="6" v-model="password" required />
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
export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    handleLogin() {
      console.log('Вход:', {
        email: this.email,
        password: this.password,
      });
      alert('Вы успешно вошли!');
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