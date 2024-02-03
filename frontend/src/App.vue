<script>
import { RouterView } from 'vue-router';
import Home from './components/Home.vue';
import Login from './components/Login.vue';
import Navbar from './components/Navbar.vue';
import Register from './components/Register.vue';
import Space from './components/Space.vue';
import { useUserStore } from './stores/user';
</script>

<template>
  <main class="">
    <template v-if="!userState.loggedIn">
      <Navbar />
    </template>
    <template v-else>
      <Space />
    </template>
  </main>
  <!-- <RouterView /> -->
</template>

<script setup>
const userState = useUserStore();
// console.log({userState});
</script>
