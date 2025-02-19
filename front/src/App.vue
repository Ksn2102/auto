<template>
  <div id="app">
    <nav class="left">
      <!-- <router-link to="/"></router-link> | --><img class="logo" src="@/assets/logo.svg" alt="">
      <router-link to="/">Главная</router-link>
      <router-link to="/about">О нас</router-link>
      <router-link to="/korzina">Корзина</router-link>
      <router-link to="/katalog">Каталог</router-link>
      <router-link to="/pokypka">Покупка онлайн</router-link>
      <router-link to="/where">Где найти?</router-link>
      <router-link to="/register" class="right">Регистрация</router-link>
    </nav>
    <router-view>
    </router-view>
    <!-- <div class="photo">
            <img class="sss" src="../photo/backk.png" alt="">
             <span class="text">Выберите автомобиль мечты!</span>
             <button class="text1">Подробнее</button>
        </div> -->
    <footer>
      <div class="cont">
        <div>
          <ul>
            <li class="zag">Выбор и покупка</li>
            <li class="etc">Модельный ряд</li>
            <li class="etc">Тест драйв</li>
            <li class="etc">Автомобили с пробегом</li>
            <li class="etc">BMW Premium Selection</li>
            <li class="etc">Финансовые сервисы</li>
            <li class="etc">Корпоративные продажи</li>
          </ul>
        </div>
        <div>
          <ul>
            <li class="zag">Сервис и аксессуары</li>
            <li class="etc">Запись на сервис</li>
            <li class="etc">Магазин Аксессуаров BMW</li>
            <li class="etc">Программа помощи на дорогах</li>
            <li class="etc">BMW Lifestyle</li>
          </ul>
        </div>
        <div>
          <ul>
            <li class="zag">BMW Россия</li>
            <li class="etc">Контакты</li>
            <li class="etc">Обратная связь</li>
            <li class="etc">FAQ</li>
            <li class="etc">Дилерская сеть</li>
            <li class="etc">Стать партнером по качеству</li>
          </ul>
        </div>
        <div>
          <ul>
            <li class="zag">BMW Group</li>
            <li class="etc">BMW.com</li>
            <li class="etc">BMW Group</li>
            <li class="etc">BMW M Driving Experience</li>
            <li class="etc">BMW Motorrad</li>
            <li class="etc">MINI</li>
            <li class="etc">Brand Experience Centre</li>
            <li class="etc">BMW Excellence Club</li>
          </ul>
        </div>
      </div>
    </footer>
  </div>
</template>


<script>
export default {
  name: 'App',
};
</script>

<style>
@import '@/styles/style.css';

.text {
  position: absolute;
  top: 40%;
  left: 40%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 54px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
}

.right {
  text-align: left;
}

nav {
  padding: 20px;
  background-color: #000000;
}

nav a {
  margin-right: 10px;
  text-decoration: none;
  color: #ffffff;
}

nav a.router-link-active {
  font-weight: bold;
  color: #4842b9;
}

footer {
  background-color: #eeeeee;
}

.cont {
  display: flex;
  margin: 0 auto;
  width: 100%;
  max-width: 1100px;
  justify-content: space-around;
  padding-top: 10px;
}

.zag{
  font-weight: bold;
  padding-bottom: 10px;
}

.etc{
  padding-bottom: 5px;
}
</style>