<script setup>
import { useUserStore } from '../stores/user';
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';
import 'flowbite/dist/flowbite.js';
import Header from './Header.vue';
import RecentPosts from './Tutor/RecentPosts.vue';

const userState = useUserStore();
</script>

<template>
   <Header />

   <div class="flex flex-row">
      <div class="basis-3/4">
         <RecentPosts />
      </div>
   </div>
</template>