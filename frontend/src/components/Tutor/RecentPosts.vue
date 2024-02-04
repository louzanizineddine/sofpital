<script setup>
import { onMounted } from 'vue';
import { useUserStore } from '../../stores/user';
import { ref } from 'vue';

const store = useUserStore();
let recommended_posts = ref([]);
let dataLoaded = ref(false);

onMounted(async () => {
    console.log(`Recents post component mounted`);
    const data = await fetch(`http://localhost:8000/api/tutor/${store.user.tutor_id}/recommended_posts`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'x-access-token': localStorage.getItem('token'),
        }
    });
    const response = await data.json();
    console.log(response);
    recommended_posts.value = response;
    dataLoaded.value = true;
});
</script>

<template>
    <div class="mt-8">
        <h1 class="text-2xl font-bold text-gray-900">Recommended Posts</h1>
        <ul role="list" class="divide-y divide-gray-100">
            <template v-if="dataLoaded">
                <li v-for="post in recommended_posts" :key="post.id" class="flex justify-between gap-x-6 py-5">
                    <div class="flex min-w-0 gap-x-4">
                        <img class="h-12 w-12 flex-none rounded-full bg-gray-50"
                            src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                            alt="">
                        <div class="min-w-0 flex-auto">
                            <p class="text-sm font-semibold leading-6 text-gray-900">{{ post.title }}</p>
                            <p class="text-sm leading-6 text-gray-500">{{ post.description }}</p>
                        </div>
                    </div>
                    <div class="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
                        <p class="text-sm leading-6 text-gray-900">{{ post.status }}</p>
                        <p class="mt-1 text-xs leading-5 text-gray-500">{{ post.poste_date }}</p>
                    </div>
                </li>
            </template>
        </ul>
    </div>
</template>
