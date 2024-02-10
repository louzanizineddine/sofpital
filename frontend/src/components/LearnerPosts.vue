<template>
    <Header />
    <Search />
    <h1 class="text-4xl font-bold mt-6">Posts</h1>
    <div class="flex flex-row flex-wrap justify-center">
        <!-- Show skeleton loading animation when loading is true -->
        <div v-if="loading" class="card w-96 bg-blue-500 text-primary-content m-4">
            <div class="card-body">
                <div class="skeleton w-full h-8 mb-4"></div>
                <div class="skeleton w-full h-6 mb-4"></div>
                <div class="skeleton w-full h-6"></div>
            </div>
        </div>
        <!-- Show posts when available -->
        <div v-else v-for="post in posts" :key="post.id" class="card w-96 bg-blue-600 text-primary-content m-4">
            <div class="card-body">
                <h2 class="card-title">{{ post.title }}</h2>
                <p>{{ post.description }}</p>
                <p>posted on {{ post.post_date }}</p>
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
</template>

<script setup>
import { useUserStore } from '../stores/user';
import { onMounted, ref, watch, computed } from 'vue';
import Header from './Header.vue';
import Search from './Search.vue';
const store = useUserStore();
const posts = ref([]);
const currentPage = ref(1);
let totalPages = ref(1);
const perPage = 6; // Set the number of posts per page
const loading = ref(false); // Loading state variable

onMounted(async () => {
    await fetchPosts();
});

const fetchPosts = async () => {
    const page = currentPage.value;
    loading.value = true; // Set loading to true before fetching
    const data = await fetch(`http://localhost:8000/api/learner/${store.user.learner_id}/posts?page=${page}&per_page=${perPage}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'x-access-token': localStorage.getItem('token')
        }
    });
    const response = await data.json();
    posts.value = response.posts;
    totalPages.value = response.total_pages;
    console.log('totalPages:', totalPages.value);
    loading.value = false; // Set loading to false after fetching
};

// Method to change the current page
const changePage = (page) => {
    console.log('Changing page to', page);
    currentPage.value = page;
    console.log('Current page is now', currentPage.value);
    fetchPosts();
};
</script>
