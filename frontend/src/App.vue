<script setup>
import { RouterView } from 'vue-router';
import Home from './components/Home.vue';
import Login from './components/Login.vue';
import Navbar from './components/Navbar.vue';
import Register from './components/Register.vue';
</script>

<template>
  <main class="dark">
    <Navbar></Navbar>
    <RouterView></RouterView>
  </main>
</template>