<template>
    <Header />

    <h1 class="text-4xl font-bold mt-6">Received Offers</h1>
    <div class="flex flex-row flex-wrap justify-center">
        <div class="card w-96 bg-blue-600 text-primary-content m-4" v-for="post in receivedOffers">
            <div class="card-body">
                <h2 class="card-title">{{ post.title }}</h2>
                <p>{{ post.description }}</p>
                <p>postd on {{ post.poste_date }}</p>
                <p>Numbers of offers {{ post.offers === undefined ? '0' : post.offers.length}}</p>
                <div class="card-actions justify-end">
                    <button class="btn">See Details</button>
                </div>
            </div>
        </div>
    </div>
</template>


<script setup>
import { useUserStore } from '../stores/user';
import { onMounted, ref } from 'vue';
import Header from './Header.vue';
const store = useUserStore();
console.log('received offers component');

const receivedOffers = ref([]);
onMounted(async () => {
    const data = await fetch(`http://localhost:8000/api/learner/${store.user.learner_id}/posts/received_offers`,
        {
            method: 'GET',
            headers: {
                contentType: 'application/json',
                'x-access-token': localStorage.getItem('token')
            }
        }
    )
    const response = await data.json();
    receivedOffers.value = response;
    console.log(response);
})

</script>