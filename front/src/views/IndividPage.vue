<template>
    <div class="conteiner19" v-if="car">
        <p class="zagolovok">{{ car.text }}</p>
        <div class="flex2">
            <img class="pic" :src="require(`@/assets/${car.img}`)" />
            <div>
                <p>Цвет: {{ car.color }}</p>
                <p>Габариты: 3 x 3 x 4 м</p>
                <p>Масса: {{ car.weight }}</p>
                <h1>{{ car.price }} ₽</h1>
                <p class="photo">
                     <button class="centerr" @click="goToBronPage(car)">Забронировать</button>
                </p>
            </div>
        </div>
        <div class="podrobno">
            <p class="dop">Описание</p>
            <p>{{ car.opic }}</p>
        </div>
    </div>
</template>

<script>
import cars from '@/mocks/cars.json';

export default {
  name: 'IndividPage',
  data() {
    return {
      car: null,
    };
  },
  mounted() {
    const carId = parseInt(this.$route.params.id);
    this.car = cars.find(car => car.id === carId);
  },
  methods: {
    goToBronPage() {
      const token = localStorage.getItem('access_token');
      
      if (!token) {
        alert(' Для бронирования необходимо войти в систему!');
        this.$router.push('/login');
        return;
      }
      this.$router.push(`/bron/${this.car.id}`);
    }
  }
};
</script>
<style>
@import '@/styles/katalog.css';



</style>