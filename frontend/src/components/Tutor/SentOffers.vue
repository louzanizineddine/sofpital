<script setup>
import { onMounted } from 'vue';
import { useUserStore } from '../../stores/user';
import { ref } from 'vue';

const store = useUserStore();
const dataLoaded = ref(false);
const sentOffers = ref([]);

onMounted(async () => {
    console.log(`Sent offers component mounted`);
    const data = await fetch(`http://localhost:8000/api/tutor/${store.user.tutor_id}/offers`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'x-access-token': localStorage.getItem('token'),
        }
    });
    const response = await data.json();
    console.log(response);
    dataLoaded.value = true;
    sentOffers.value = response;
    // console.log(data)
});
</script>

<template v-if="dataLoaded">
    <div class="mt-8 dark:text-white">
        <h1 class="text-2xl font-bold text-white-900">Sent offers</h1>
        <div class="overflow-x-auto">
            <table class="table">
                <!-- head -->
                <thead>
                    <tr>
                        <th>Learner</th>
                        <th>Description</th>
                        <th>Status</th>
                        <th>Details</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- use v-for to loop through the sentOffers array -->
                    <tr v-for="(offer, index) in sentOffers" :key="index">
                        <td>
                            <div class="flex items-center gap-3">
                                <div class="avatar">
                                    <div class="mask mask-squircle w-12 h-12">
                                        
                                    </div>
                                </div>
                            </div>
                        </td>
                        <td>
                            {{ offer.title }}
                            <br />
                            <span class="badge badge-ghost badge-sm">{{ offer.description }}</span>
                        </td>
                        <td><span class="text-green">{{ offer.status }}</span></td>
                        <th>
                            <button class="btn btn-ghost btn-xs">details</button>
                        </th>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
