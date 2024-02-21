<template>
    <div>
        <Header />
        <Search />
        <h1 class="text-4xl font-bold mt-6">Meetings</h1>
        <div class="flex flex-row flex-wrap justify-center">
            <div v-if="loading" class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl m-3">
                <div class="md:flex">
                    <div class="md:flex-shrink-0">
                        <div class="skeleton h-48 w-full object-cover md:w-48"></div>
                    </div>
                    <div class="p-8">
                        <div class="skeleton w-32 h-4 mb-6"></div>
                        <div class="skeleton w-48 h-4 mb-6"></div>
                        <div class="skeleton w-32 h-4 mb-2"></div>
                        <div class="skeleton w-48 h-4 mb-2"></div>
                        <div class="skeleton w-24 h-4 mb-2"></div>
                        <div class="skeleton w-32 h-12 mt-4"></div>
                    </div>
                </div>
            </div>
            <div v-else-if="meetings.length === 0" class="text-center text-gray-500 mt-4">
                No meetings for now.
            </div>
            <div v-else v-for="meet in meetings" :key="meet.id"
                class="max-w-md mx-auto bg-blue-700 text-white rounded-xl shadow-md overflow-hidden md:max-w-2xl mt-8">
                <div class="md:flex">
                    <div class="md:flex-shrink-0">
                        <img class="h-full w-full object-cover md:w-48" src="https://picsum.photos/2010"
                            alt="Doctor's image">
                    </div>
                    <div class="p-8">
                        <div class="uppercase tracking-wide text-sm font-semibold">{{ meet.tutor.user.first_name }} {{
                            meet.tutor.user.last_name }}</div>
                        <p class="block mt-1 text-lg leading-tight font-medium">About post: {{ meet.post.title }}</p>
                        <p class="mt-2">Duration: {{ meet.duration }} minutes</p>
                        <p class="">Meeting date due to: {{ formatDate(meet.date) }}</p>
                        <button class="btn mt-3">
                            mark as completed
                        </button>
                    </div>
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
                <div v-if="loading" class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl m-3">
                    <div class="md:flex">
                        <div class="md:flex-shrink-0">
                            <div class="skeleton h-48 w-full object-cover md:w-48"></div>
                        </div>
                        <div class="p-8">
                            <div class="skeleton w-32 h-4 mb-6"></div>
                            <div class="skeleton w-48 h-4 mb-6"></div>
                            <div class="skeleton w-32 h-4 mb-2"></div>
                            <div class="skeleton w-48 h-4 mb-2"></div>
                            <div class="skeleton w-24 h-4 mb-2"></div>
                            <div class="skeleton w-32 h-12 mt-4"></div>
                        </div>
                    </div>
                </div>
                <div v-else-if="accepted_offers.length === 0" class="text-center text-gray-500 mt-4">
                    No accepted_offers for now.
                </div>
                <div v-else v-for="offer in accepted_offers" :key="offer.id"
                    class="max-w-md mx-auto bg-blue-700 text-white rounded-xl shadow-md overflow-hidden md:max-w-2xl mt-8">
                    <div class="md:flex">
                        <div class="md:flex-shrink-0">
                            <img class="h-full w-full object-cover md:w-48" src="https://picsum.photos/2010"
                                alt="Doctor's image">
                        </div>
                        <div class="p-8">
                            <div class="uppercase tracking-wide text-sm font-semibold">{{ offer.title }}</div>
                            <p class="block mt-1 text-lg leading-tight font-medium text-black">{{ offer.description }}</p>
                            <p class="mt-2">Posted on: {{ formatDate(offer.offer_date) }}</p>
                            <p class="">Offer by Tutor: {{ offer.tutor.user.first_name }} {{ offer.tutor.user.last_name }}</p>
                            <button class="btn mt-3" @click="showModal(offer.id)">Set up a Meeting</button>
                            <dialog :id="`modal_${offer.id}`" class="modal text-black">
                                <div class="modal-box">
                                    <h3 class="text-2xl">Insert The meeting information</h3>
                                    <form method="dialog">
                                        <label for="meeting_date" class="label mt-3">Meeting Date</label>
                                        <input type="datetime-local" v-model="meetingForm.date"
                                            class="input input-bordered w-full max-w-xs" />
                                        <label for="meeting_location" class="label mt-3">Meeting Duration in Minutes</label>
                                        <input type="number" min="15" max="120" v-model="meetingForm.duration"
                                            placeholder="Meeting Duration" class="input input-bordered w-full max-w-xs" />
                                        <br>
                                        <button
                                            @click.prevent="() => submitNewMeeting(offer.id, offer.tutor_id, offer.post_id)"
                                            class="btn mt-4 mr-3 bg-blue-600 text-white">Submit</button>
                                        <button class="btn">Close</button>
                                    </form>
                                </div>
                            </dialog>
                        </div>
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
import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'
import { getTutorInfo, getPostInfo, formatDate } from '../utils.js'
import {apiURL} from '../config'


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
    const data = await fetch(`${apiURL}meeting/`, {
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
        const url = `${apiURL}learner/${store.user.learner_id}/offers/accepted_offers`;
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
    }
};

const fetchMeetings = async () => {
    loading.value = true;
    try {
        const page = currentPage.value;
        const url = `${apiURL}meeting/learner/${store.user.learner_id}?page=${page}&per_page=${perPage}`;
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'x-access-token': localStorage.getItem('token')
            }
        });
        const data = await response.json();
        console.log(data);
        meetings.value = data.meetings;
        totalPages.value = data.total_pages;
    } catch (error) {
        console.error('Error fetching meetings:', error);
    } finally {
    }
};

const fetchDetails = async (meeting) => {
    const tutor = await getTutorInfo(meeting.tutor_id);
    if (tutor) {
        meeting.tutor = tutor;
    }

    const post = await getPostInfo(meeting.learner_id, meeting.post_id);
    if (post) {
        meeting.post = post;
    }
}
onMounted(async () => {
    await fectchAcceptedOffers();
    await fetchMeetings();
    for (let i = 0; i < meetings.value.length; i++) {
        await fetchDetails(meetings.value[i]);
    }
    console.log(meetings.value);

    for (let i = 0; i < accepted_offers.value.length; i++) {

        const tutor = await getTutorInfo(accepted_offers.value[i].tutor_id);
        if (tutor) {
            accepted_offers.value[i].tutor = tutor;
        }
    }
    console.log(accepted_offers.value);

    loading.value = false;
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