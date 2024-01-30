<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
console.log('home page')
const user = ref();
console.log(user.value);
// onMounted(async () => {
//     const data = await fetch('http://localhost:8000/api/auth/login');
//     console.log(data);
// });
</script>

<template>

<section class="bg-gray-50 dark:bg-gray-900">
</section>
</template>