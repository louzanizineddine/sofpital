<template>
  <li class="flex justify-between gap-x-6 py-5">
    <div class="flex min-w-0 gap-x-4">
      <img class="h-12 w-12 flex-none rounded-full bg-gray-50"
        src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
        alt="">
      <div class="min-w-0 flex-auto">
        <p class="text-sm font-semibold leading-6 text-white-900">{{ post.title }}</p>
        <p class="text-sm leading-6 text-white-500">{{ post.description }}</p>
      </div>
    </div>
    <div class="hidden shrink-0 sm:flex sm:flex-col sm:items-end">
      <p class="text-sm leading-6 text-white-900">{{ post.status }}</p>
      <p class="mt-1 text-xs leading-5 text-white-500">{{ post.poste_date }}</p>
      <!-- Update onclick to dynamically target the modal based on post id -->
      <button class="btn" @click="showModal(post.id)">Make an offer</button>
      <!-- Assign dynamic id based on post id -->
      <dialog :id="`modal_${post.id}`" class="modal">
        <div class="modal-box">
          <h3 class="font-bold text-lg">Add you offer details</h3>
          <form method="dialog">
            <!-- if there is a button in form, it will close the modal -->
            <label for="title" class="label mt-3">Offer title</label>
            <input type="text" v-model="OfferForm.title" placeholder="Offer title"
              class="input input-bordered w-full max-w-xs" />

            <label for="description" class="label mt-3">Offer description</label>
            <input type="text" v-model="OfferForm.description" placeholder="Offer description"
              class="input input-bordered w-full max-w-xs" />
            <br>

            <button @click.prevent="submitOffer" class="btn mt-4 mr-3 bg-blue-600 text-white">Submit</button>
            <button class="btn mt-4 bg-red-600 text-white">Close</button>
          </form>
        </div>
      </dialog>
    </div>
  </li>
</template>

<script setup>
import { ref } from 'vue';
import { useUserStore } from '../../stores/user';
import { apiURL } from '../../config'

import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

const store = useUserStore();
const props = defineProps(['post']);

// Define showModal method to dynamically open the modal associated with each post
function showModal(postId) {
  document.getElementById(`modal_${postId}`).showModal();
}

// Define closeModal method to dynamically close the modal associated with each post
function closeModal() {
  document.getElementById(`modal_${props.post.id}`).close();
}

const OfferForm = ref({
  title: '',
  description: '',
});

async function submitOffer() {

  const data = await fetch(`${apiURL}tutor/${store.user.tutor_id}/offers/post/${props.post.id}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-access-token': localStorage.getItem('token'),
    },
    body: JSON.stringify({
      title: OfferForm.value.title,
      description: OfferForm.value.description,
      learner_id: props.post.learner_id,
      tutor_id: store.user.tutor_id,
      post_id: props.post.id,
      offer_date: new Date().toISOString(),
    }),
  });

  const response = await data.json();

  if (response.status === 'success') {
    console.log('Offer submitted successfully');
    toast('Your offer have been added successfully', { type: 'success', timeout: 1500 });
    OfferForm.value.title = '';
    OfferForm.value.description = '';
    closeModal();
    store.user.newSentOffer = true
  } else {
    console.log('Offer submission failed');
    toast('Your offer submission failed', { type: 'error', timeout: 1500 });
  }
}

</script>