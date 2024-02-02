<script setup>
import 'flowbite/dist/flowbite.js'
</script>

<template>
    <div class="dark:text-white mt-4 basis-2/4 p-4 border-solid rounded border-2 shadow">
        <div class="mb-3">
            <h1>Post title</h1>
            <label for="message" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
            </label>
            <textarea id="message" rows="2"
                class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Are you stuck ask for help"></textarea>
        </div>
        <div class="">
            <h1>Describe you post in details</h1>
            <label for="message" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
            </label>
            <textarea id="message" rows="5"
                class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="Are you stuck ask for help"></textarea>
        </div>
        <button type="submit"
            class="mt-4 inline-flex items-center px-5 py-2.5 text-sm font-medium text-center text-white bg-blue-700 rounded-lg focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-900 hover:bg-blue-800">
            Publish post
        </button>
    </div>  
</template>