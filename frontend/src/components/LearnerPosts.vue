<template>
    <Header />

    <h1 class="text-4xl font-bold mt-6">Posts</h1>
    <div class="flex flex-row flex-wrap justify-center">
        <div class="card w-96 bg-blue-600 text-primary-content m-4" v-for="post in posts">
            <div class="card-body">
                <h2 class="card-title">{{ post.title }}</h2>
                <p>{{ post.description }}</p>
                <p>postd on {{ post.poste_date }}</p>
            </div>
        </div>
    </div>
</template>


<script setup>
import { useUserStore } from '../stores/user';
import { onMounted, ref } from 'vue';
import Header from './Header.vue';
const store = useUserStore();
console.log('posts component');

const posts = ref([]);
onMounted(async () => {
    const data = await fetch(`http://localhost:8000/api/learner/${store.user.learner_id}/posts`,
        {
            method: 'GET',
            headers: {
                contentType: 'application/json',
                'x-access-token': localStorage.getItem('token')
            }
        }
    )
    const response = await data.json();
    posts.value = response;
    console.log(response);
})

</script>