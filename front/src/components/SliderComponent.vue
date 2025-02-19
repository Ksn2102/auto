<template>
    <div class="slider">
        <div class="slides">
            <template v-for="slide in slides" :key="slide.id">
        <div 
            class="slide"
            v-if="slide.id === current"
        ><img :src="require(`@/assets/${slide.img}`)" :alt="slide.title"></div>
            </template>
        </div>
        <button class="prev" @click="prevSlide()">&#10094;</button>
        <button class="next" @click="nextSlide()">&#10095;</button>
    </div>
</template>
<script setup>
import { ref } from 'vue';
const current = ref(1);
const slides = [
    {
        id: 1,
        img: '11.webp',
        title: 'Car 1'
    },
    {
        id: 2,
        img: '12.webp',
        title: 'Car 2'
    },
    {
        id: 3,
        img: '13.webp',
        title: 'Car 3'
    },
    {
        id: 4,
        img: '14.jpg',
        title: 'Car 4'
    },
    {
        id: 5,
        img: '15.webp',
        title: 'Car 5'
    }
]

const prevSlide = () => {
    if(current.value > 1) {
        current.value = current.value - 1
    }
}

const nextSlide = () => {
    if (current.value < slides.length) {
        current.value = current.value + 1;
    }
}
</script>
<style>
.slider {
  margin-top: 30px;
  position: relative;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  gap: 50px;
  padding-top: 50px;
  align-items: center;
}

.slides {
  display: flex;
  overflow: hidden;
  border-radius: 10px;
  padding: 20px 0 25px;
}

.slide {
  min-width: 100%;
  transition: 0.5s ease;
}

.slide img {
  width: 100%;
  vertical-align: middle;
  border-radius: 10px;
}

.prev,
.next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  border-radius: 5px;
  user-select: none;
}

.prev {
  left: 10px;
}

.next {
  right: 10px;
}

.prev:hover,
.next:hover {
  background-color: rgba(0, 0, 0, 0.8);
}
</style>