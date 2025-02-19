<template>
    <div>
      <h1>Продукт {{ productId }}</h1>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  
  export default {
    setup() {
      const route = useRoute();
      const productId = ref(route.params.id);
  
      onMounted(() => {
        console.log('ID продукта:', productId.value);
      });
  
      return { productId };
    },
  };
  </script>