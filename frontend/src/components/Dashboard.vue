<template>
    <div>
        <Header />

        <template v-if="whatToLoad === 'tutor'">
            <RecommendedPosts />
            <SentOffers />
        </template>

        <template v-else>
            <div class="flex flex-row justify-evenly">
                <PostInput />
                <UpcomingMeetings />
            </div>
        </template>
    </div>
</template>

<script setup>
import { useUserStore } from '../stores/user';
import { onMounted, ref } from 'vue';
import PostInput from './PostInput.vue';
import UpcomingMeetings from './UpcomingMeetings.vue';
import Header from './Header.vue';
import RecommendedPosts from './Tutor/RecommendedPosts.vue';
import SentOffers from './Tutor/SentOffers.vue';

console.log(`rendering dashboard`)

const store = useUserStore();
const whatToLoad = ref('');

onMounted(() => {
    if (store.user.role === 'tutor') {
        whatToLoad.value = 'tutor';
    } else {
        whatToLoad.value = 'learner';
    }
});
</script>
