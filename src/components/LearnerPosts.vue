<template>
    <div>
      <Header />
      <Search />
      <h1 class="text-4xl font-bold mt-6">Posts</h1>
      <div class="flex flex-row flex-wrap justify-center">
        <div v-if="loading" class="card w-96 bg-blue-500 text-primary-content m-4">
          <div class="card-body">
            <div class="skeleton w-full h-8 mb-4"></div>
            <div class="skeleton w-full h-6 mb-4"></div>
            <div class="skeleton w-full h-6"></div>
          </div>
        </div>
        <div v-else v-for="post in posts" :key="post.id" class="card w-96 bg-blue-600 text-primary-content m-4">
          <div class="card-body">
            <h2 class="card-title">{{ post.title }}</h2>
            <p>{{ post.description }}</p>
            <p> posted on {{ post.poste_date }}</p>
          </div>
        </div>
      </div>
      <!-- Pagination controls -->
      <div class="flex flex-row justify-center">
        <div class="pagination">
          <input v-for="page in totalPages" :key="page" 
            class="join-item btn btn-square" 
            type="radio" 
            name="options" 
            :aria-label="page" 
            @change="changePage(page)" 
            :checked="page === currentPage">
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useUserStore } from '../stores/user';
  import { onMounted, ref, computed } from 'vue';
  import Header from './Header.vue';
  import Search from './Search.vue';
  import {apiURL} from '../config'

  const store = useUserStore();
  const posts = ref([]);
  const currentPage = ref(1);
  const totalPages = ref(1);
  const perPage = 6;
  const loading = ref(false);
  
  const fetchPosts = async () => {
    loading.value = true;
    try {
      const page = currentPage.value;
      const url = `${apiURL}learner/${store.user.learner_id}/posts?page=${page}&per_page=${perPage}`;
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'x-access-token': localStorage.getItem('token')
        }
      });
      const data = await response.json();
      console.log(data);
      posts.value = data.posts;
      totalPages.value = data.total_pages;
    } catch (error) {
      console.error('Error fetching posts:', error);
    } finally {
      loading.value = false;
    }
  };


  onMounted(fetchPosts);
  
  const changePage = (page) => {
    console.log('page chaged to ', page)
    currentPage.value = page;
    fetchPosts();
  };
  
  </script>
  