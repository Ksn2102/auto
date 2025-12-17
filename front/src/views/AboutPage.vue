<template>
  <div class="dis">
    <img class="logotip" src="@/assets/logo.svg" alt="">
    <div>
      <h1 style="padding-bottom: 20px;">PrestigeRide - ваш пункт назначения в мире авто. Где каждый автомобиль - точка
        комфорта</h1>
      <p style="font-weight: bolder;">Из названия компании и подчеркиваем:</p>
      <ul>
        <li>- Точность выбора</li>
        <li>- Начало пути</li>
        <li>- Качество сервиса</li>
        <li>- Уверенность в решении</li>
      </ul>
    </div>
  </div>
  <div class="slider">
    <h1>Новинки компании:</h1>
    <SliderComponent />
    

  </div>
</template>

<script setup>
import SliderComponent from '@/components/SliderComponent.vue';

</script>
<style>

.dis {
  display: flex;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  gap: 50px;
  padding-top: 50px;
  align-items: center;
}

.logotip {
  width: 40%;
}

/* Общие стили */
.dis {
  display: flex;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  gap: 50px;
  padding-top: 50px;
  align-items: center;
  flex-wrap: wrap; /* Разрешаем перенос строк */
}

.logotip {
  width: 40%; /* Ширина логотипа */
  height: auto; /* Сохраняем пропорции */
}

.dis div {
  flex: 1; /* Блок с текстом занимает всю доступную ширину */
}

h1 {
  font-size: 36px; /* Размер заголовка */
  padding-bottom: 20px;
}

ul {
  list-style-type: disc; /* Стиль маркера списка */
  padding-left: 20px; /* Отступ для маркеров */
}

li {
  font-size: 18px; /* Размер пунктов списка */
  padding-bottom: 10px; /* Отступ между пунктами */
}

.slider {
  padding-top: 50px; /* Отступ сверху */
  text-align: center; /* Центрируем содержимое */
}

.slider h1 {
  font-size: 30px; /* Размер заголовка секции */
  margin-bottom: 20px;
}

/* Медиа-запросы */

/* Для экранов меньше 1024px (планшеты) */
@media (max-width: 1024px) {
  .dis {
    flex-direction: column; /* Переводим в вертикальную ориентацию */
    align-items: center; /* Центрируем содержимое */
    text-align: center; /* Выравниваем текст по центру */
  }

  .logotip {
    width: 60%; /* Увеличиваем размер логотипа */
    margin-bottom: 20px; /* Добавляем отступ снизу */
  }

  h1 {
    font-size: 30px; /* Уменьшаем размер заголовка */
  }

  li {
    font-size: 16px; /* Уменьшаем размер пунктов списка */
  }
}

/* Для экранов меньше 768px (мобильные устройства) */
@media (max-width: 768px) {
  .logotip {
    width: 80%; /* Дополнительно увеличиваем размер логотипа */
  }

  h1 {
    font-size: 24px; /* Дополнительно уменьшаем размер заголовка */
  }

  li {
    font-size: 14px; /* Дополнительно уменьшаем размер пунктов списка */
  }

  .slider h1 {
    font-size: 24px; /* Уменьшаем размер заголовка секции */
  }
}

/* Для экранов меньше 480px (очень маленькие мобильные устройства) */
@media (max-width: 480px) {
  h1 {
    font-size: 20px; /* Дополнительно уменьшаем размер заголовка */
  }

  li {
    font-size: 12px; /* Дополнительно уменьшаем размер пунктов списка */
  }

  .slider h1 {
    font-size: 20px; /* Дополнительно уменьшаем размер заголовка секции */
  }
}
</style>