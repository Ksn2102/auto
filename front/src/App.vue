<template>
  <div id="app">
    <div class="ph"></div>
    <nav class="left">
      <router-link to="/"><img class="logotyp" src="@/assets/logo.svg" alt=""></router-link>
      <div class="fl">
      
      <router-link to="/katalog">Каталог</router-link>
      <router-link to="/tarif">Тарифы</router-link>
      <router-link to="/register" class="right">Регистрация</router-link>
      <router-link to="/lk">Личный кабинет</router-link>
      <router-link to="/about">О нас</router-link>
    </div>
    </nav>
    <router-view></router-view>
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
</style>