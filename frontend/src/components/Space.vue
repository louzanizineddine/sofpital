<script setup>
import Header from './Header.vue';
import PostInput from './PostInput.vue';
import UpcomingMeetings from './UpcomingMeetings.vue';
import TutorSpace from './TutorSpace.vue';
import LearnerSpace from './LearnerSpace.vue';
import { useUserStore } from '../stores/user';
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';
import 'flowbite/dist/flowbite.js';

const router = useRouter()
const userState = useUserStore();
console.log(userState.user)
userState.getToken();

const loaded = ref(false);

onMounted(async () => {
    console.log('personal space')
    console.log('mounted')
    if (!userState.loggedIn) {
        router.push({ name: 'Login' });
    }
    // check if user info is available
    if (userState.user === null) {
        console.log('fetching user info another time')
        const res = await userState.fetchUserInfo(userState.token.sub);
        if (res === null) {
            router.push({ name: 'Login' });
        }
        console.log(userState.user);
        loaded.value = true;
    }
})


</script>

<template>
    <div class="container mx-auto">
        <template v-if="loaded && userState.user.role === 'learner'">
          
            <LearnerSpace />
        </template>
        <template v-if="loaded && userState.user.role === 'tutor'">
            <TutorSpace />
        </template>
    </div>
</template>