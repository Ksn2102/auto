<template>
  <div class="photo">
    <img class="sss" src="@/assets/backk.png" alt="Background">
    <span class="text">Выберите автомобиль мечты!</span>
    <button class="text1">Подробнее</button>
  </div>
  <div class="onc">
    <h1 class="centre">Vorsprung durch Technik</h1>
    <p class="centre2">Это наши автомобили!</p>
    <div class="news">
      <div class="raz">
        <img class="razmere" src="@/assets/1.png" alt="">
        <div>
          <h1 class="nazv">Переосмысление: думать о конце с самого начала</h1>
          <p>Согласно принципу «Переосмысление», компоненты на этапе разработки концепции уже проектируются с учетом
            возможности вторичной переработки.</p>
        </div>

      </div>
      <div class="dva">
        <img class="razmere" src="@/assets/2.png" alt="">
        <div>
          <h1 class="nazv">Устойчивое развитие как тогда, так и сейчас: “Audi следует правильным путем”.</h1>
          <p>Посол бренда Audi Феликс Нойройтер и Рюдигер Рекнагель, глава отдела охраны окружающей среды Audi Group,
            рассказывают об экологичных автомобилях-первопроходцах, привлекательности электромобилей и будущем
            экологичного производства в музее Audi.</p>
        </div>

      </div>
      <div class="three">
        <img class="razmere" src="@/assets/3.png" alt="">
        <div>
          <h1 class="nazv">Миссия: Нулевая</h1>
          <p>Audi сокращает воздействие на окружающую среду при производстве и логистике с помощью экологической
            программы Mission:Zero.</p>
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
</style>