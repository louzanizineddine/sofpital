<template>  
    <div class="flex flex-row justify-center mt-2 p-8">
        <div class="basis-2/4 p-3 w-full shadow-xl">
            <div class="flex flex-row justify-evenly">
                <input
                    class="w-5/6 h-12 px-4 text-base placeholder-gray-600 border rounded-lg focus:shadow-outline"
                    type="text" 
                    v-model="searchQuery" 
                    placeholder="Search for anything"
                >
                <button class="btn bg-blue-500 text-white" @click="handleSearch">
                    Search
                </button>
            </div>
            <div v-if="loading">Loading...</div>
            <div v-else>
                <div v-for="post in postsSearchResults" :key="post.id">
                    <p>{{ post.title }}</p>
                    <p>{{ post.description }}</p>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script setup>
import { ref } from 'vue';

const searchQuery = ref('');
const postsSearchResults = ref([]);
const loading = ref(false);

const search = async () => {
    loading.value = true;
    try {
        // Fetch search results from the server
        const response = await fetch(`http://localhost:8000/api/search?query=${searchQuery.value}`);
        const data = await response.json();
        postsSearchResults.value = data.results.posts;
    } catch (error) {
        console.error('Error searching:', error);
    } finally {
        loading.value = false;
    }
};

const handleSearch = () => {
    if (searchQuery.value.trim() !== '') {
        search();
    } else {
        postsSearchResults.value = [];
    }
};
</script>
