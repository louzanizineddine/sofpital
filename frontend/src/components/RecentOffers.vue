<script setup>

import { ref, onMounted } from 'vue';
import { useUserStore } from '../stores/user';

const store = useUserStore();

onMounted(async () => {
    console.log(`rendering recent offers`)
    const data = await fetch(`http://localhost:8000/api/learner/${store.user.learner_id}/posts`,
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'x-access-token': localStorage.getItem('token')
            }
        },
    )

    const offers = await data.json()
    console.log(offers);
})
</script>

<template>
    <div class="mt-8">

    </div>
</template>