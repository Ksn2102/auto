<template>
    <div class="register-page">
        <h2 style="text-align: center;">Регистрация</h2>
        <form @submit.prevent="register">
            <div class="form-group">
                <label for="name">Имя пользователя:</label>
                <input class="input" type="text" id="name" v-model="name" required placeholder="Введите имя"
                    @input="validateName" />
                    <span v-if="errors.name" class="error">{{ errors.name }}</span>
            </div>
            <div class="form-group">
                <label for="surname">Фамилия пользователя:</label>
                <input class="input" type="text" id="surname" v-model="surname" required  @input="validateSurname" />
                <span v-if="errors.surname" class="error">{{ errors.surname }}</span>
            </div>
            <div class="form-group">
                <label for="patronimyc">Отчество пользователя:</label>
                <input class="input" type="text" id="patronimyc" v-model="patronimyc" />
            </div>
            <div class="form-group">
                <label for="login">Логин:</label>
                <input class="input" type="text" id="login" v-model="login" required  @input="validateLogin"/>
                <span v-if="errors.login" class="error">{{ errors.login }}</span>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input class="input" type="email" id="email" v-model="email" required @input="validateEmail"/>
                <span v-if="errors.email" class="error">{{ errors.email }}</span>
            </div>

            <div class="form-group">
                <label for="password">Пароль:</label>
                <input class="input" type="password" id="password" placeholder=" (минимум 6 символов)" minlength="6"
                    v-model="password" required @input="validatePassword"/>
                    <span v-if="errors.password" class="error">{{ errors.password }}</span>
            </div>
            <div class="form-group">
                <label for="password_confirm">Повторный пароль:</label>
                <input class="input" type="password" id="password_confirm" placeholder=" (минимум 6 символов)"
                    minlength="6" v-model="password_confirm"  @input="validatePasswordConfirm" required />
                    <span v-if="errors.password_confirm" class="error">{{
          errors.password_confirm
        }}</span>
            </div>
            <div class="left1">
                <input type="checkbox" id="check"
          v-model="termsAccepted"
          @change="validateTerms">
                <label for="check">Я согласен с правилами платформы</label>
                <span v-if="errors.terms" class="error">{{ errors.terms }}</span>
            </div>
            <button class="otst" type="submit" :disabled="hasErrors">Зарегистрироваться</button>
        </form>
        <p>
            Уже есть аккаунт?
            <router-link to="/login">Войти</router-link>
        </p>
    </div>
</template>

<script>
import apiClient from 'axios';

export default {
  data() {
    return {
      name: '',
      surname: '',
      patronimyc: '',
      login: '',
      email: '',
      password: '',
      password_confirm: '',
      termsAccepted: false,
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
    validateName() {
      const regex = /^[а-яА-ЯёЁ]+$/;
      if (!this.name || !regex.test(this.name)) {
        this.errors.name = 'Имя должно содержать только кириллические символы';
      } else {
        this.errors.name = null;
      }
    },
    validateSurname() {
      const regex = /^[а-яА-ЯёЁ]+$/;
      if (!this.surname || !regex.test(this.surname)) {
        this.errors.surname = 'Фамилия должна содержать только кириллические символы';
      } else {
        this.errors.surname = null;
      }
    },
    validatePatronimyc() {
      const regex = /^[а-яА-ЯёЁ]*$/;
      if (this.patronimyc && !regex.test(this.patronimyc)) {
        this.errors.patronimyc = 'Отчество может содержать только кириллические символы';
      } else {
        this.errors.patronimyc = null;
      }
    },
    validateLogin() {
      const regex = /^[a-zA-Z0-9-]+$/;
      if (!this.login || !regex.test(this.login)) {
        this.errors.login = 'Логин должен содержать только латинские буквы, цифры и тире';
      } else {
        this.errors.login = null;
      }
    },
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
    validatePasswordConfirm() {
      if (this.password !== this.password_confirm) {
        this.errors.password_confirm = 'Пароли не совпадают';
      } else {
        this.errors.password_confirm = null;
      }
    },
    validateTerms() {
      if (!this.termsAccepted) {
        this.errors.terms = 'Вы должны согласиться с правилами регистрации';
      } else {
        this.errors.terms = null;
      }
    },
    async register() {
      if (this.hasErrors) {
        alert('Пожалуйста, исправьте ошибки в форме');
        return;
      }

      try {
        const response = await apiClient.post('/register', {
          name: this.name,
          surname: this.surname,
          patronimyc: this.patronimyc,
          login: this.login,
          email: this.email,
          password: this.password,
        });
        alert(response.data.message);
      } catch (error) {
        alert(error.response?.data?.message || 'Произошла ошибка при регистрации');
      }
    },
  },
};

</script>

<style>
.error {
  color: red;
  font-size: 0.8em;
}

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

.left1 {
    display: flex;
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

.input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
}

.otst:hover {
    background-color: #38a169;
}
</style>