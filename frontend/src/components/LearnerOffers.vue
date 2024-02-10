<template>
    <div>
      <Header />
      <Search />
      <h1 class="text-4xl font-bold mt-6">Posts with Offers</h1>
      <div class="flex flex-row flex-wrap justify-center">
        <div v-if="loading" class="card w-96 bg-blue-500 text-primary-content m-4">
          <div class="card-body">
            <div class="skeleton w-full h-8 mb-4"></div>
            <div class="skeleton w-full h-6 mb-4"></div>
            <div class="skeleton w-full h-6"></div>
          </div>
        </div>
        <div v-else v-for="res in results" :key="res.id" class="card w-96 bg-blue-600 text-primary-content m-4">
          <div class="card-body">
            <h2 class="card-title">{{ res.title }}</h2>
            <p>{{ res.description }}</p>
            <p> posted on {{ res.poste_date }}</p>
            <p>Current Number of Offers {{ res.offers.length }}</p>
            <button  class="btn btn-info text-white mt-2">
                    <router-link :to="{ name: 'OffersForOnePost', params: { id: res.id } }">
                        See All offers
                    </router-link>
            </button>
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
  
  const store = useUserStore();
  const results = ref([]);
  const currentPage = ref(1);
  const totalPages = ref(1);
  const perPage = 6;
  const loading = ref(false);
  
  const fetchresults = async () => {
    loading.value = true;
    try {
      const page = currentPage.value;
      const url = `http://localhost:8000/api/learner/${store.user.learner_id}/posts/received_offers?page=${page}&per_page=${perPage}`;
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'x-access-token': localStorage.getItem('token')
        }
      });
      const data = await response.json();
      console.log(data);
      results.value = data.results;
      totalPages.value = data.total_pages;
    } catch (error) {
      console.error('Error fetching results:', error);
    } finally {
      loading.value = false;
    }
  };
  onMounted(fetchresults);
  
  
  const changePage = (page) => {
    currentPage.value = page;
    fetchresults();
  };
  
  </script>
  