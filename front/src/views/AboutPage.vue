<template>
  <div class="dis">
    <img class="logotip" src="@/assets/logo.svg" alt="">
    <div>
      <h1 style="padding-bottom: 20px;">CarPoint - ваш пункт назначения в мире авто. Где каждый автомобиль - точка
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
</style>