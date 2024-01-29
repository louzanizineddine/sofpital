<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
console.log('home page')
const user = ref();

onMounted(async () => {
    const data = await fetch('http://localhost:8000/api/auth/login');
    console.log(data);
});
</script>

<template>
    <div>home page</div>
</template>