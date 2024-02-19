<template>
    <div>
        <Header />

        <template v-if="whatToLoad === 'tutor'">
        
        </template>

        <template v-else>
            <h1 class="text-4xl font-bold mt-6">Dashboard</h1>
            <div class="flex flex-row justify-center mb-8">
                <PostInput />
            </div>
        </template>
    </div>
</template>

<script setup>
import { useUserStore } from '../stores/user';
import { onMounted, ref } from 'vue';
import { RouterView } from 'vue-router';
import PostInput from './PostInput.vue';
import Header from './Header.vue';
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
