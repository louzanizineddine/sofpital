<template>
    <Header />
    <template v-if="!postLoaded">
        <div class="skeleton w-32 h-32"></div>
    </template>
    <template v-else>
        <h1 class="text-7xl mt-5">Your Post </h1>
        <div :class="CardBackground(post.status)" class="flex flex-col mt-5 w-1/3 p-8 text-white">
            <h1 class="text-5xl">{{ post.title }}</h1>
            <p class="text-xl">{{ post.description }}</p>
            <p> posed On {{ post.poste_date}}</p>
            <p>status: {{post.status}}</p>
        </div>
    </template>

    <h1 class="text-7xl mt-5">List Of offers</h1>
    <template v-if="!offersLoaded">
        <div class="flex flex-row flex-warp">
            <div class="skeleton w-32 h-32"></div>
            <div class="skeleton w-32 h-32"></div>
            <div class="skeleton w-32 h-32"></div>
        </div>
    </template>
    <template v-else>
        <div class="flex flex-row flex-wrap">
            <div :class="CardBackground(offer.status)"  class="card w-96 m-4 text-white" v-for="offer in offers" :key="offer.id">
                <div class="card-body">
                    <h2 class="card-title text-4xl">{{ offer.title }}</h2>
                    <p>{{ offer.description }}</p>
                    <p>Offered on {{ offer.offer_date }}</p> <!-- Corrected typo in "post_date" -->
                    <p>{{offer.status}}</p>
                    <div class="card-actions justify-end">
                        <button :disabled="areButtonsDisabled" class="btn btn-info text-white" @click="() => {handleAcceptOffer(offer.id)}">
                            Accept
                        </button>
                        <button :disabled="areButtonsDisabled" class="btn btn-error text-white" @click="() => {handleDeclineOffer(offer.id)}">
                            Decline
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </template>
</template>

<script setup>
import { useUserStore } from '../stores/user';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import Header from './Header.vue';
import {apiURL} from '../config'
import {toast} from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

const store = useUserStore();
const router = useRouter();
const postId = ref(null); // Define a reactive variable to hold the post ID
const offers = ref([]);
const post = ref({});
const postLoaded = ref(false)
const offersLoaded = ref(false)
const areButtonsDisabled = ref(false);

function offerStatusColor(status){
    if(status === 'pending'){
        return 'text-warning';
    }else if(status === 'accepted'){
        return 'text-success';
    }else if(status === 'rejected'){
        return 'text-error';
    }
    else {
        return '';
    }
}

function CardBackground(status){
    if(status === 'pending'){
        return 'bg-blue-600';
    }else if(status === 'accepted'){
        return 'bg-green-600';
    }else if(status === 'rejected'){
        return 'bg-red-600';
    }
    else {
        return '';
    }
}

async function handleAcceptOffer(offerId){
    const { id } = router.currentRoute.value.params;
    const request = await fetch(`${apiURL}learner/${store.user.learner_id}/posts/${id}/accept_offer/${offerId}`,
        {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'x-access-token': localStorage.getItem('token')
            }
        }
    )
    
    const res = await request.json();
    if(res.message === "success")
    {
        toast('Offer has been accepted', {type: 'success', timeout: 1500});
    }else {
        toast('OOOOOPS! something went wrong', {type: 'error', timeout: 1500});
    }
}

async function handleDeclineOffer(offerId){
    const { id } = router.currentRoute.value.params;
    const request = await fetch(`${apiURL}learner/${store.user.learner_id}/posts/${id}/reject_offer/${offerId}`,
        {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'x-access-token': localStorage.getItem('token')
            }
        }
    )
    
    const res = await request.json();
    if(res.message === "success")
    {
        toast('Offer has been rejected', {type: 'success', timeout: 1500});
    }else {
        toast('OOOOOPS! something went wrong', {type: 'error', timeout: 1500});
    }
}

onMounted(async () => {
    const { id } = router.currentRoute.value.params;
    postId.value = id;

    const dataPost = await fetch(`${apiURL}learner/${store.user.learner_id}/posts/${id}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'x-access-token': localStorage.getItem('token')
        }
    });
    post.value = await dataPost.json();
    console.log(post.value);
    postLoaded.value = true;
    if (post.value.status === 'pending') {
        areButtonsDisabled.value = false;
    } else {
        areButtonsDisabled.value = true;
    }

    const dataOffers = await fetch(`${apiURL}learner/${store.user.learner_id}/posts/${id}/recieved_offers`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'x-access-token': localStorage.getItem('token')
        }
    });
    const response = await dataOffers.json();
    offers.value = response;
    offersLoaded.value = true;
    console.log(response);
});
</script>

<style>
    .btn:disabled {
        color: black !important;
    }
</style>
