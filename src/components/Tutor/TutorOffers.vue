<template>
  <Header />
  <div v-if="dataLoaded">
    <div class="mt-8 dark:text-white">
      <h1 class="text-3xl font-bold mt-4 mb-4">Your offers</h1>
      <!-- Filter buttons -->
      <div class="flex justify-center mt-4 mb-4 space-x-4">
        <button @click="filterOffers('all')"
          :class="{ 'p-2 rounded bg-blue-500 text-white': currentFilter === 'all' }">All</button>
        <button @click="filterOffers('accepted')"
          :class="{ 'p-2 rounded  bg-green-500 text-white': currentFilter === 'accepted' }">Accepted</button>
        <button @click="filterOffers('rejected')"
          :class="{ 'p-2 rounded bg-red-500 text-white': currentFilter === 'rejected' }">Rejected</button>
        <button @click="filterOffers('pending')"
          :class="{ 'p-2 rounded  bg-yellow-500 text-white': currentFilter === 'pending' }">Pending</button>
      </div>
      <div class="overflow-x-auto">
        <table class="table">
          <!-- head -->
          <thead>
            <tr>
              <th>Offer To</th>
              <th>Offer Description</th>
              <th>Offer Date</th>
              <th>Post Title</th>
              <th>Offer Status</th>
            </tr>
          </thead>
          <tbody>
            <!-- use v-for to loop through the filteredOffers array -->
            <tr v-for="(offer, index) in filteredOffers" :key="index">
              <!-- Table rows -->
              <td>
                <div class="flex items-center gap-3">
                  <div class="avatar">
                    <div class="mask mask-squircle w-12 h-12">
                      <img class="h-full w-full object-cover md:w-48" :src="getAvatar(offer.learner.avatar)" alt="Avatar">
                    </div>
                  </div>
                  {{ offer.learner.first_name }} {{ offer.learner.last_name }}
                </div>
              </td>
              <td>
                {{ offer.title }}
                <br />
                <span class="badge badge-ghost badge-sm">{{ offer.description }}</span>
              </td>
              <td>{{ formatDate(offer.offer_date) }}</td>
              <td>{{ offer.postTitle }}</td>
              <td>
                <span v-if="offer.status === 'pending'" class="badge bg-yellow-500 text-white">Pending</span>
                <span v-else-if="offer.status === 'accepted'" class="badge badge-success text-white">Accepted</span>
                <span v-else-if="offer.status === 'rejected'" class="badge badge-error text-white">Rejected</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
  
<script setup>
import { onMounted } from 'vue';
import { useUserStore } from '../../stores/user';
import { ref, computed } from 'vue';
import Header from '../Header.vue';
import { getLearnerInfo, getPostInfo, formatDate } from '../../utils.js';
import { apiURL } from '../../config'


const store = useUserStore();
const dataLoaded = ref(false);
const sentOffers = ref([]);
const currentFilter = ref('all'); // Default filter

// Function to get the avatar URL with fallback
const getAvatar = (avatar) => avatar || 'https://picsum.photos/2010';

// Function to fetch tutor's sent offers
const getTutorSentOffers = async () => {
  const response = await fetch(`${apiURL}tutor/${store.user.tutor_id}/offers`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'x-access-token': localStorage.getItem('token'),
    }
  });
  return response.json();
};

// Fetch and process offers data on component mount
onMounted(async () => {
  try {
    sentOffers.value = await getTutorSentOffers();
    for (const offer of sentOffers.value) {
      offer.learner = await getLearnerInfo(offer.learner_id);
      const post = await getPostInfo(offer.learner_id, offer.post_id);
      offer.postTitle = post.title;
    }
    dataLoaded.value = true;
    console.log('Offers:', sentOffers.value);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});

// Computed property to filter offers based on their status
const filteredOffers = computed(() => {
  if (currentFilter.value === 'all') {
    return sentOffers.value;
  } else {
    return sentOffers.value.filter(offer => offer.status === currentFilter.value);
  }
});

// Function to filter offers based on status
const filterOffers = (status) => {
  currentFilter.value = status;
};
</script>
  