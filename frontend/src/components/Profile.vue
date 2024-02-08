<template>
    <div>
      <Header />
      <div class="container mx-auto mt-8">
        <h2 class="text-4xl font-bold mb-4">Profile</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Profile Image -->
          <div class="mb-4">
            <img src="https://picsum.photos/200" alt="Profile Image" class="rounded-full w-32 h-32 mx-auto">
            <div class="mt-4 flex justify-center space-x-4">
            <a href="#" class="text-blue-500 hover:text-blue-700"><i class="fab fa-facebook-square fa-2x">facebok</i></a>
            <a href="#" class="text-blue-500 hover:text-blue-700"><i class="fab fa-twitter-square fa-2x">twitter</i></a>
            <a href="#" class="text-blue-500 hover:text-blue-700"><i class="fab fa-linkedin fa-2x">instagram</i></a>
            <!-- Add more social media links as needed -->
          </div>
          </div>
          <!-- Profile Details -->
          <div class="p-6 bg-white rounded-md shadow-md">
            <div class="mb-4">
              <label class="text-lg font-semibold">First Name:</label>
              <span class="ml-2">{{ store.user.last_name }}</span>
            </div>
            <div class="mb-4">
              <label class="text-lg font-semibold">Last Name:</label>
              <span class="ml-2">{{ store.user.first_name }}</span>
            </div>
            <div class="mb-4">
              <label class="text-lg font-semibold">Username:</label>
              <span class="ml-2">{{ store.user.username }}</span>
            </div>
            <div class="mb-4">
              <label class="text-lg font-semibold">Email:</label>
              <span class="ml-2">{{ store.user.email }}</span>
            </div>
            <div class="mb-4">
              <label class="text-lg font-semibold">Role:</label>
              <span class="ml-2">{{ store.user.role }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import Header from './Header.vue';
    import { useUserStore } from '../stores/user';
    import { ref, onMounted, watch } from 'vue';

    const store = useUserStore();

  console.log(store.user)


  </script>
  
  <style scoped>
  /* Add custom styles here */
  /* Example: */
  .container {
    max-width: 800px;
    margin: 0 auto;
  }
  
  label {
    display: block;
    margin-bottom: 0.5rem;
  }
  </style>
  [
  
    {
        post_id: 1,
        title: "How to learn Python",
        description: "I want to learn Python, but I don't know where to start. Can someone help me?",
        user_id: 1,
        offers: [
            {
                offer_id: 1,
                user_id: 2,
                message: "I can help you with that. I have been using Python for 5 years now.",
                status: "accepted"
            },
            {
                offer_id: 2,
                user_id: 3,
                message: "I can help you with that. I have been using Python for 5 years now.",
                status: "pending"
            }
        ]
    }
  ]