<script setup>
import { useUserStore } from '../stores/user';
import { useRouter } from 'vue-router';
import { ref, onMounted, watch } from 'vue';
import { storeToRefs } from 'pinia';
import 'flowbite/dist/flowbite.js';
import Header from './Header.vue';
import RecommendedPosts from './Tutor/RecommendedPosts.vue';
import SentOffers from './Tutor/SentOffers.vue';
const store = useUserStore();
const {newSentOffer} = ref(store);

watch(newSentOffer, (newVal, oldVal) => {
   console.log('newSentOffer', newVal);
});

</script>

<template>
   <Header />

   <div class="flex flex-row">
      <div class="basis-3/4">
         <RecommendedPosts />
         <SentOffers />
      </div>
   </div>
</template>
