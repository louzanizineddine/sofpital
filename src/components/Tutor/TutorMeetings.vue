<template>
  <Header />
  <div v-if="dataLoaded">
    <div class="mt-8 dark:text-white">
      <h1 class="text-3xl font-bold mt-4 mb-4">Your meetings</h1>
      <!-- Filter buttons -->
      <div class="flex justify-center mt-4 mb-4 space-x-4">
        <button @click="filterMeetings('all')"
          :class="{ 'p-2 rounded bg-blue-500 text-white': currentFilter === 'all' }">All</button>
        <button @click="filterMeetings('done')"
          :class="{ 'p-2 rounded bg-green-500 text-white': currentFilter === 'done' }">Done</button>
        <button @click="filterMeetings('upcoming')"
          :class="{ 'p-2 rounded bg-red-500 text-white': currentFilter === 'upcoming' }">Upcoming</button>
      </div>
      <div class="overflow-x-auto">
        <table class="table">
          <!-- head -->
          <thead>
            <tr>
              <th>Meeting with</th>
              <th>Meeting Date</th>
              <th>Post Title</th>
              <th>Meeting Status</th>
              <th>Action</th> <!-- New column for action buttons -->
            </tr>
          </thead>
          <tbody v-if="filteredMeetings.length > 0">
            <!-- use v-for to loop through the filteredMeetings array -->
            <tr v-for="(meet, index) in filteredMeetings" :key="index">
              <!-- Table rows -->
              <td>
                <div class="flex items-center gap-3">
                  <div class="avatar">
                    <div class="mask mask-squircle w-12 h-12">
                      <img class="h-full w-full object-cover md:w-48" :src="getAvatar(meet.learner.avatar)" alt="Avatar">
                    </div>
                  </div>
                  <!-- {{ meet.learner.first_name }} {{ meet.learner.last_name }} -->
                  {{ meet.learner.email }}
                </div>
              </td>
              <td>{{ formatDate(meet.date) }}</td>
              <td>{{ meet.postTitle }}</td>
              <td>{{ meet.done ? 'done' : 'not done' }}</td>
              <td>
                <!-- Button to mark meeting as done -->
                <button v-if="!meet.done" @click="markMeetingDone(meet)" class="p-2 rounded bg-green-500 text-white">
                  Mark as Done
                </button>
                <button v-else class="p-2 rounded bg-gray-300 text-gray-500" disabled>
                  Marked as Done
                </button>
              </td>
              <td>
                <div class="flex justifybetween items-center bg-blue-500 text-white p-2 rounded cursor-pointer" v-if="!meet.done">
                  <img src="./video-call-1.png" alt="Icon" class="w-6 h-6 mx-1">
                  <a @click="startMeeting(meet.learner.email)">Start Meeting</a>
                </div>
                <div class="flex justifybetween items-center bg-gray-500 text-white p-2 rounded cursor-not-allowed" v-else>
                  <img src="./video-call-1.png" alt="Icon" class="w-6 h-6 mx-1">
                  <span>Start Meeting</span>
                </div>
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
import { apiURL } from '../../config';

const store = useUserStore();
const dataLoaded = ref(false);
const meetings = ref([]);
const currentFilter = ref('all'); // Default filter

// Function to get the avatar URL with fallback
const getAvatar = (avatar) => avatar || 'https://picsum.photos/2010';

// Function to fetch tutor's sent offers
const getTutormeetings = async () => {
  const response = await fetch(`${apiURL}meeting/tutor/${store.user.tutor_id}`, {
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
    meetings.value = await getTutormeetings();
    console.log(meetings.value);
    for (const meet of meetings.value) {
      meet.learner = await getLearnerInfo(meet.learner_id);
      const post = await getPostInfo(meet.learner_id, meet.post_id);
      meet.postTitle = post.title;
    }
    dataLoaded.value = true;
    console.log('meetings:', meetings.value);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});

// Computed property to filter offers based on their status
const filteredMeetings = computed(() => {
  if (currentFilter.value === 'all') {
    return meetings.value;
  } else {
    return meetings.value.filter(meet => meet.done ? currentFilter.value === 'done' : currentFilter.value === 'upcoming');
  }
});

// Function to filter offers based on status
const filterMeetings = (status) => {
  currentFilter.value = status;
};

const markMeetingDone = async (meeting) => {
  try {
    // Perform an API call to update the meeting status
    const response = await fetch(`${apiURL}meeting/${meeting.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'x-access-token': localStorage.getItem('token'),
      },
    });

    const data = response.json();
    if (data.status = "success") {
      // Update the local meeting object
      meeting.done = true;
    } else {
      console.error('Failed to mark meeting as done');
    }
  } catch (error) {
    console.error('Error marking meeting as done:', error);
  }
};

const startMeeting = (learnerEmail) => {
  navigator.clipboard.writeText(learnerEmail)
    .then(() => {
      console.log('Email copied to clipboard:', learnerEmail);
      // redirect to the video call page on a new tab
      window.open('https://meet.google.com/new?hs=180&amp;authuser=0', '_blank');
    })
    .catch(err => {
      console.error('Failed to copy email to clipboard:', err);
      window.open('https://meet.google.com/new?hs=180&amp;authuser=0', '_blank');
    });
}
</script>
