<!-- YourMainComponent.vue -->
<template>
    <div class="text-white mt-8 dark:text-white">
      <h1 class="text-2xl font-bold text-white-900">Recommended Posts</h1>
      <ul role="list" class="divide-y divide-gray-100">
        <template v-if="dataLoaded">
          <PostItem v-for="post in recommended_posts" :key="post.id" :post="post" />
        </template>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue';
  import { useUserStore } from '../../stores/user';
  import PostItem from './PostItem.vue';
    import { ref } from 'vue';
  
  const store = useUserStore();
  let recommended_posts = ref([]);
  let dataLoaded = ref(false);
  
  onMounted(async () => {
    console.log(`Recents post component mounted`);
    const data = await fetch(`http://localhost:8000/api/tutor/${store.user.tutor_id}/recommended_posts`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'x-access-token': localStorage.getItem('token'),
      }
    });
    const response = await data.json();
    console.log(response);
    recommended_posts.value = response.recommended_posts;
    dataLoaded.value = true;
  });
  </script>
  