<template>
    <router-view />
</template>
<script setup>
import { onBeforeMount } from 'vue';

onBeforeMount(() => {
    console.log('admin start mounted')
})
</script>