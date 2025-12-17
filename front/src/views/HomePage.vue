<template>
  <div class="photo">
    <img class="sss" src="@/assets/backk.png" alt="Background">
    <span class="text">Выберите автомобиль мечты!</span>
    <button class="text1">Подробнее</button>
  </div>
  <div class="onc">
    <p class="centre2">Это наши автомобили!</p>
    <div class="news">
      <div class="raz">
        <img class="razmere" src="@/assets/1.png" alt="">
        <div>
          <h1 class="nazv">Переосмысление: думать о конце с самого начала</h1>
          
        </div>

      </div>
      <div class="dva">
        <img class="razmere" src="@/assets/2.png" alt="">
        <div>
          <h1 class="nazv">Устойчивое развитие как тогда, так и сейчас: “Audi следует правильным путем”.</h1>
          
        </div>

      </div>
      <div class="three">
        <img class="razmere" src="@/assets/3.png" alt="">
        <div>
          <h1 class="nazv">Миссия: Нулевая</h1>
          
        </div>

      </div>
    </div>
    <div class="mews">
      <img class="pop" src="@/assets/4.png" alt="">
      <div>
        <h1 class="otsy">Устойчивость</h1>
        <p class="otsy">Audi берет на себя экономическую, экологическую и социальную ответственность и сделала устойчивое развитие
          бизнеса неотъемлемой частью всех своих решений и продуктов. Узнайте больше о том, как Audi формирует
          мобильность будущего на основе четкой стратегии.</p>
        <button class="dix">Подробнее</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>
<style>
@import '@/styles/style.css';

.centre {
  text-align: center;
  padding-bottom: 18px;
  font-size: 55px;
}

.centre2 {
  text-align: center;
  padding-bottom: 18px;
  font-size: 30px;
}

.onc {
  padding-top: 60px;
  padding-bottom: 60px;
}

.news {
  display: flex;
  justify-content: space-evenly;
}

.razmere {
  width: 400px;
}

.raz,
.dva,
.three {
  width: 400px;
}

.nazv {
  font-size: 22px;
}

.mews {
  display: flex;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  gap: 50px;
  padding-top: 50px;
  align-items: center;
}

.pop {
  width: 600px;
}

.otsy{
  padding-bottom: 20px;
}

.dix{
  background: inherit;
  color: black;
  border: 1px solid;
  padding: 15px 65px;
}

/* Общие стили */
.centre {
  text-align: center;
  padding-bottom: 18px;
  font-size: 55px;
}

.centre2 {
  text-align: center;
  padding-bottom: 18px;
  font-size: 30px;
}

.onc {
  padding-top: 60px;
  padding-bottom: 60px;
}

.news {
  display: flex;
  justify-content: space-evenly;
  gap: 20px; /* Добавляем отступ между элементами */
  flex-wrap: wrap; /* Разрешаем перенос строк */
}

.razmere {
  width: 100%; /* Изображения будут занимать всю доступную ширину */
  height: auto; /* Сохраняем пропорции */
}

.raz,
.dva,
.three {
  width: calc(33.33% - 20px); /* Три блока в строке с учетом отступов */
  box-sizing: border-box;
}

.nazv {
  font-size: 22px;
}

.mews {
  display: flex;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  gap: 50px;
  padding-top: 50px;
  align-items: center;
  flex-wrap: wrap; /* Разрешаем перенос строк */
}

.pop {
  width: 100%; /* Изображение занимает всю доступную ширину */
  height: auto; /* Сохраняем пропорции */
}

.otsy {
  padding-bottom: 20px;
}

.dix {
  background: inherit;
  color: black;
  border: 1px solid;
  padding: 15px 65px;
}

/* Медиа-запросы */

/* Для экранов меньше 1024px (планшеты) */
@media (max-width: 1024px) {
  .centre {
    font-size: 40px; /* Уменьшаем размер заголовка */
  }

  .centre2 {
    font-size: 24px; /* Уменьшаем размер текста */
  }

  .news {
    flex-direction: column; /* Переводим в вертикальную ориентацию */
    align-items: center; /* Центрируем содержимое */
  }

  .raz,
  .dva,
  .three {
    width: 100%; /* Блоки занимают всю доступную ширину */
    margin-bottom: 20px; /* Добавляем отступ снизу */
  }

  .mews {
    flex-direction: column; /* Переводим в вертикальную ориентацию */
    align-items: center; /* Центрируем содержимое */
    text-align: center; /* Выравниваем текст по центру */
  }
}

/* Для экранов меньше 768px (мобильные устройства) */
@media (max-width: 768px) {
  .centre {
    font-size: 30px; /* Дополнительно уменьшаем размер заголовка */
  }

  .centre2 {
    font-size: 20px; /* Дополнительно уменьшаем размер текста */
  }

  .nazv {
    font-size: 18px; /* Уменьшаем размер заголовков новостей */
  }

  .dix {
    padding: 10px 40px; /* Уменьшаем размер кнопки */
  }
}

/* Для экранов меньше 480px (очень маленькие мобильные устройства) */
@media (max-width: 480px) {
  .centre {
    font-size: 24px; /* Дополнительно уменьшаем размер заголовка */
  }

  .centre2 {
    font-size: 16px; /* Дополнительно уменьшаем размер текста */
  }

  .nazv {
    font-size: 16px; /* Дополнительно уменьшаем размер заголовков новостей */
  }

  .dix {
    padding: 8px 30px; /* Дополнительно уменьшаем размер кнопки */
    font-size: 14px; /* Уменьшаем размер шрифта */
  }
}
</style>