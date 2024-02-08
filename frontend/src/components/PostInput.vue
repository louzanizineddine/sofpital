<script setup>
import 'flowbite/dist/flowbite.js'

import { ref, onMounted } from 'vue';
import { useUserStore } from '../stores/user';
import {toast} from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'
const userState = useUserStore();
const post_form = ref({
    title: '',
    description: '',
    tags: '',
});

console.log(post_form)


async function publishPost() {
    console.log(post_form.value)

    const tagsArray = post_form.value.tags.split(',').map(tag => tag.trim());

    // Create an array of tag objects
    const tags = tagsArray.map(tag => ({ name: tag }));

    const data = await fetch(`http://localhost:8000/api/learner/${userState.user.learner_id}/posts`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-access-token': localStorage.getItem('token')
        },
        body: JSON.stringify(
            {
                learner_id: userState.user.learner_id,
                title: post_form.value.title,
                description: post_form.value.description,
                poste_date: new Date().toISOString(),
                tags: tags,
            }
        ),
    });
    const response = await data.json();
    console.log(response);
    if (response.status === 'success') {
        // reset the form
        post_form.value.title = '';
        post_form.value.description = '';
        post_form.value.tags = '';
        toast('Your post have been published successfully', {type: 'success', timeout: 1500});
    }
}

</script>

<template>
    <div class="bg-primary text-black mt-4 basis-2/4 p-4 border-solid rounded">
        <div class="mb-3">
            <h1 class="text-xl">Post title</h1>
            <label for="title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
            </label>
            <textarea id="title" rows="2" v-model="post_form.title"
                class="block p-2.5 w-full text-sm text-white-900 bg-gray-700"
                placeholder="Are you stuck ask for help"></textarea>
        </div>
        <div class="">
            <h1  class="text-xl">Describe you post in details</h1>
            <label for="desciption" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
            </label>
            <textarea id="description" rows="5" v-model="post_form.description"
            class="block p-2.5 w-full text-sm text-white-900 bg-gray-700"
                placeholder="Are you stuck ask for help"></textarea>
        </div>
        <div class="">
            <h1  class="text-xl">Add Tags</h1>
            <label for="tags" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
            </label>
            <input id="tags" v-model="post_form.tags"
            class="block p-2.5 w-full text-sm text-white-900 bg-gray-700"
                placeholder="Add tags separated by commas">
        </div>
        <button type="submit" @click="publishPost"
            class="mt-4 inline-flex items-center px-5 py-2.5 text-sm font-medium text-center text-white bg-blue-700 rounded-lg focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-900 hover:bg-blue-800">
            Publish post
        </button>
    </div>

</template>