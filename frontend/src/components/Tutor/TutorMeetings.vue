<template>
    <Header />
    <div class="max-w-md mx-auto bg-blue-700 text-white rounded-xl shadow-md overflow-hidden md:max-w-2xl mt-8">
        <div class="md:flex">
            <div class="md:flex-shrink-0">
                <img class="h-full w-full object-cover md:w-48" src="https://picsum.photos/2010" alt="Doctor's image">
            </div>
            <div class="p-8">
                <div class="uppercase tracking-wide text-sm font-semibold">{{ zineddine }} {{
                    louzani }}</div>
                <p class="block mt-1 text-lg leading-tight font-medium">About post: {{ test }}</p>
                <p class="mt-2">Duration: {{ 30 }} minutes</p>
                <p class="">Meeting date due to: {{ `23 02 2024` }}</p>
                <button class="btn mt-3">
                    mark as completed
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import Header from '../Header.vue';
</script>