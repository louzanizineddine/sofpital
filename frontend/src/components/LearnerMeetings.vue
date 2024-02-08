<template>
    <Header />

    <h1 class="text-4xl font-bold mt-6">Meetings</h1>

    <span v-if="meetings.length === 0">No meetings</span>

    <span class="text-error">To be implemented later</span>
    <!-- <template v-else>
        <div class="flex flex-row flex-wrap justify-center">
            <div class="card w-96 bg-blue-600 text-primary-content m-4" v-for="meet in meetings">
                <div class="card-body">
                    <h2 class="card-title">{{ meet.title }}</h2>
                    <p>{{ meet.description }}</p>
                    <p>postd on {{ meet.poste_date }}</p>
                </div>
            </div>
        </div>
    </template> -->
</template>


<script setup>
import { useUserStore } from '../stores/user';
import { onMounted, ref } from 'vue';
import Header from './Header.vue';
const store = useUserStore();
console.log('Meetings component');

const meetings = ref([]);
onMounted(async () => {
    const data = await fetch(`http://localhost:8000/api/meeting/${store.user.learner_id}`,
        {
            method: 'GET',
            headers: {
                contentType: 'application/json',
                'x-access-token': localStorage.getItem('token')
            }
        }
    )
    const response = await data.json();
    meetings.value = response;
    console.log(response);
})

</script>