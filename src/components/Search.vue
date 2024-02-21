<template>
    <div>
        <div class="flex flex-row justify-center mt-2 p-8">
            <div class="basis-2/4 p-3 w-full shadow-xl">
                <div class="flex flex-row justify-evenly">
                    <input class="w-5/6 h-12 px-4 text-base placeholder-gray-600 border rounded-lg focus:shadow-outline"
                        type="text" v-model="searchQuery" placeholder="Search for anything" />
                    <button class="btn bg-blue-500 text-white" @click="handleSearch">Search</button>
                </div>
                <div v-if="loading">Loading...</div>
            </div>
        </div>
        <!-- Dialog for search results -->
        <div v-if="showDialog"
            class="fixed z-10 top-0 left-0 right-0 bottom-0 flex justify-center items-center bg-gray-800 bg-opacity-50">
            <div class="bg-white p-6 rounded-lg shadow-xl">
                <h2 class="text-lg font-semibold mb-4">Post Results</h2>
                <div v-if="postsSearchResults.length > 0">
                    <div v-for="post in postsSearchResults" :key="post.id" class="mb-4">
                        <p class="text-base font-semibold">{{ post.title }}</p>
                        <p class="text-sm text-gray-700">{{ post.description }}</p>
                    </div>
                </div>

                <h2 class="text-lg font-semibold mb-4">Offer Results</h2>
                <div v-if="offersSearchResults.length > 0">
                    <div v-for="offer in offersSearchResults" :key="offer.id" class="mb-4">
                        <p class="text-base font-semibold">{{ offer.title }}</p>
                        <p class="text-sm text-gray-700">{{ offer.description }}</p>
                    </div>
                </div>
                <div v-else>No results found.</div>
                <button class="btn bg-blue-500 text-white mt-4" @click="closeDialog">Close</button>
            </div>
        </div>
    </div>
</template>
  
<script setup>
import { ref } from 'vue';

const searchQuery = ref('');
const postsSearchResults = ref([]);
const offersSearchResults = ref([]);
import {apiURL} from '../config'

const loading = ref(false);
const showDialog = ref(false);

const search = async () => {
    loading.value = true;
    try {
        // Fetch search results from the server
        const response = await fetch(`${apiURL}search?query=${searchQuery.value}`);
        const data = await response.json();
        console.log('Search results:', data.results);

        if (!data.results) {
            return;
        }
        if (data.results.posts != undefined) {
            postsSearchResults.value = data.results.posts;
        } else {
            postsSearchResults.value = [];
        }

        if (data.results.offers != undefined) {
            offersSearchResults.value = data.results.offers;
        } else {
            offersSearchResults.value = [];
        }
        showDialog.value = true; // Show the dialog with search results
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
        offersSearchResults.value = [];
        showDialog.value = false; // Hide the dialog if no search query is entered
    }
};

const closeDialog = () => {
    showDialog.value = false; // Close the dialog
};
</script>
  