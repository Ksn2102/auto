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
/* Базовые стили */
@import '@/styles/style.css';

.text {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 2rem; /* Используем rem для масштабируемости */
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
}

.right {
  text-align: left;
}

.left  {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 80px;
  background-color: #000000;
}

nav a {
  margin-right: 10px;
  text-decoration: none;
  color: #ffffff;
  font-size: 1rem;
}

nav a.router-link-active {
  font-weight: bold;
  color: #4842b9;
}

.logotyp {
  height: 90px; /* Фиксированная высота логотипа */
}

footer {
  background-color: #eeeeee;
  padding: 20px 0;
}

.cont {
  display: flex;
  flex-wrap: wrap; /* Добавляем возможность переноса элементов */
  margin: 0 auto;
  width: 90%; /* Уменьшаем ширину для лучшей адаптивности */
  max-width: 1100px;
  justify-content: space-around;
}

.zag {
  font-weight: bold;
  padding-bottom: 10px;
  font-size: 1.2rem;
}

.etc {
  padding-bottom: 5px;
  font-size: 0.9rem;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
  nav {
    flex-direction: column; /* Меняем направление навигации на вертикальное */
    align-items: flex-start;
  }

  nav a {
    margin: 5px 0; /* Увеличиваем отступ между ссылками */
  }

  .logo {
    margin-bottom: 10px; /* Отступ под логотип */
  }

  .cont {
    flex-direction: column; /* Переводим колонки в футере в столбец */
    align-items: center;
  }

  .cont div {
    width: 100%; /* Ширина каждого блока в футере становится 100% */
    text-align: center;
  }
}

/* Адаптивность для маленьких экранов */
@media (max-width: 480px) {
  .text {
    font-size: 1.5rem; /* Уменьшаем размер текста */
  }

  nav a {
    font-size: 0.9rem; /* Уменьшаем размер шрифта в навигации */
  }

  .zag {
    font-size: 1rem; /* Уменьшаем размер заголовков в футере */
  }

  .etc {
    font-size: 0.8rem; /* Уменьшаем размер обычного текста в футере */
  }
}
</style>