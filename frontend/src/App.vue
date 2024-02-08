<template>
  <div id="app">
    <RouterView />
  </div>
</template>

<script setup>
import { useUserStore } from './stores/user';
import { onBeforeMount, ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const userState = useUserStore();
const loaded = ref(false);

// Use navigation guards to handle redirection and user authentication
router.beforeEach(async (to, from, next) => {
  if (!loaded.value) {
    userState.getToken();
    loaded.value = true;
  }
  // If the route requires authentication
  if (to.meta.requiresAuth) {
    if (!userState.loggedIn) {
      // If not logged in, redirect to Home
      console.log('User not logged in');
      next({ name: 'Home' });
    } else if (!userState.user) {
      // If user info not fetched, fetch it
      console.log('Fetching user info');
      userState.getToken();
      const res = await userState.fetchUserInfo(userState.token.sub);
      if (res === null) {
        // If user info not available, redirect to Home
        console.log('User info not available');
        next({ name: 'Home' });
      }
    }
  }
  // Continue to the next route
  next();
});
</script>
