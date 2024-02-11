<template>
    <div>
        <Header />
        <Search />
        <h1 class="text-4xl font-bold mt-6">Meetings</h1>
        <div class="flex flex-row flex-wrap justify-center">
            <div v-if="loading" class="card w-96 bg-blue-500 text-primary-content m-4">
                <div class="card-body">
                    <div class="skeleton w-full h-8 mb-4"></div>
                    <div class="skeleton w-full h-6 mb-4"></div>
                    <div class="skeleton w-full h-6"></div>
                </div>
            </div>
            <div v-else-if="meetings.length === 0" class="text-center text-gray-500 mt-4">
                No meetings for now.
            </div>
            <div v-else v-for="meet in meetings" :key="meet.id" class="card w-96 bg-blue-600 text-primary-content m-4">
                <div class="card-body">
                    <!-- <h2 class="card-title">{{ post.title }}</h2>
            <p>{{ post.description }}</p>
            <p> posted on {{ post.poste_date }}</p> -->
                    {{ meet }}
                </div>
            </div>
        </div>
        <!-- Pagination controls -->
        <div class="flex flex-row justify-center">
            <div class="pagination">
                <input v-for="page in totalPages" :key="page" class="join-item btn btn-square" type="radio" name="options"
                    :aria-label="page" @change="changePage(page)" :checked="page === currentPage">
            </div>
        </div>


        <div>
            <h1 class="text-4xl font-bold mt-6">Set up a new Meeting Now</h1>
            <div class="flex flex-row flex-wrap justify-center">
                <div v-if="loading" class="card w-96 bg-blue-500 text-primary-content m-4">
                    <div class="card-body">
                        <div class="skeleton w-full h-8 mb-4"></div>
                        <div class="skeleton w-full h-6 mb-4"></div>
                        <div class="skeleton w-full h-6"></div>
                    </div>
                </div>
                <div v-else-if="accepted_offers.length === 0" class="text-center text-gray-500 mt-4">
                    No accepted_offers for now.
                </div>
                <div v-else v-for="offer in accepted_offers" :key="offer.id"
                    class="card w-96 bg-blue-600 text-primary-content m-4">
                    <div class="card-body">
                        <h2 class="card-title">{{ offer.title }}</h2>
                        <p>{{ offer.description }}</p>
                        <p> posted on {{ offer.offer_date }}</p>
                        <p>Offer by Tutor {{ offer.tutor_id }}</p>
                        <!-- Open the modal using ID.showModal() method -->
                        <button class="btn" @click="showModal(offer.id)">Set up a Meeing</button>
                        <dialog :id="`modal_${offer.id}`" class="modal text-black">
                            <div class="modal-box">
                                <h3 class="text-2xl">Insert The meeting information</h3>
                                <!-- <div class="modal-action"> -->
                                <form method="dialog">
                                    <label for="meeting_date" class="label mt-3">Meeting Date</label>
                                    <input type="datetime-local" v-model="meetingForm.date"
                                        class="input input-bordered w-full max-w-xs" />

                                    <label for="meeting_location" class="label mt-3">Meeting Duration in Minutes</label>
                                    <input type="number" min="15" max="120" v-model="meetingForm.duration"
                                        placeholder="Meeting Duration" class="input input-bordered w-full max-w-xs" />
                                    <br>
                                    <button @click.prevent="() => submitNewMeeting(offer.id, offer.tutor_id, offer.post_id)"
                                        class="btn mt-4 mr-3 bg-blue-600 text-white">Submit</button>
                                    <button class="btn">Close</button>
                                </form>
                                <!-- </div> -->
                            </div>
                        </dialog>
                    </div>
                </div>
            </div>
            <!-- Pagination controls -->
            <!-- <div class="flex flex-row justify-center">
        <div class="pagination">
          <input v-for="page in totalPages" :key="page" 
            class="join-item btn btn-square" 
            type="radio" 
            name="options" 
            :aria-label="page" 
            @change="changePage(page)" 
            :checked="page === currentPage">
        </div>
      </div> -->
        </div>
    </div>
</template>
  
  
<script setup>
import { useUserStore } from '../stores/user';
import { onMounted, ref, computed } from 'vue';
import Header from './Header.vue';
import Search from './Search.vue';
import {toast} from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'


const store = useUserStore();
const meetings = ref([]);
const currentPage = ref(1);
const totalPages = ref(1);
const perPage = 6;
const loading = ref(false);

const accepted_offers = ref([]);

const meetingForm = ref({
    date: '',
    duration: '',
});


const submitNewMeeting = async (offerId, tutorId, postId) => {
    const data = await fetch(`http://localhost:8000/api/meeting/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-access-token': localStorage.getItem('token'),
        },
        body: JSON.stringify({
            date: new Date(meetingForm.value.date).toISOString(),
            duration: meetingForm.value.duration,
            learner_id: store.user.learner_id,
            tutor_id: tutorId,
            offer_id: offerId,
            post_id: postId,
        }),
    });

    const response = await data.json();
    if (response.status === 'success') {
        console.log('Offer submitted successfully');
        toast('Your New Meeting have been added successfully', { type: 'success', timeout: 1500 });
        meetingForm.value.title = '';
        meetingForm.value.description = '';
        closeModal();
    } else {
        console.log('Meeting submission failed');
        toast('Your New Meeting submission failed', { type: 'error', timeout: 1500 });
    }
}

const fectchAcceptedOffers = async () => {
    loading.value = true;
    try {
        const page = currentPage.value;
        const url = `http://localhost:8000/api/learner/${store.user.learner_id}/offers/accepted_offers`;
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'x-access-token': localStorage.getItem('token')
            }
        });
        const data = await response.json();
        console.log(data);
        accepted_offers.value = data;
    } catch (error) {
        console.error('Error fetching meetings:', error);
    } finally {
        loading.value = false;
    }
};

const fetchMeetings = async () => {
    loading.value = true;
    try {
        const page = currentPage.value;
        const url = `http://localhost:8000/api/meeting/learner/${store.user.learner_id}?page=${page}&per_page=${perPage}`;
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'x-access-token': localStorage.getItem('token')
            }
        });
        const data = await response.json();
        meetings.value = data.meetings;
        totalPages.value = data.total_pages;
    } catch (error) {
        console.error('Error fetching meetings:', error);
    } finally {
        loading.value = false;
    }
};

onMounted(async () => {
    await fectchAcceptedOffers();
    await fetchMeetings();
});


function showModal(offerId) {
    document.getElementById(`modal_${offerId}`).showModal();
}

// Define closeModal method to dynamically close the modal associated with each post
function closeModal() {
    document.getElementById(`modal_${offerId}`).close();
}


const changePage = (page) => {
    currentPage.value = page;
    fetchMeetings();
};

</script>