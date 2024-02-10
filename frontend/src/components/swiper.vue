<script>

import 'swiper/swiper-bundle.css'
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.min.css'

export default {
    data() {
      return {
        images: [
          { src: "./images/genie-1.jpg"},
          { src: './images/genie-2.jpg'},
          { src: 'path/to/image3.jpg' },
        ],
        swiperOption: {
          slidesPerView: 1,
          autoplay: {
            delay: 5000,
            disableOnInteraction: false,
          },
          loop: true,
          pagination: {
            el: '.swiper-pagination',
            clickable: true,
          },
        },
      }
    },
  }
</script>

<template>
    <div class="swiper-container">
      <Swiper :options="swiperOption">
        <SwiperSlide v-for="(image, index) in images" :key="index">
          <img :src="image.src" alt="Slide Image">
        </SwiperSlide>
      </Swiper>
    </div>
  </template>

<style scoped>
.swiper-container {
  @apply  w-full h-64 md:h-96 xl:h-128;
}

.swiper-slide {
  @apply h-full;
}

.swiper-slide img {
  @apply w-full h-full object-cover;
}

.swiper-pagination {
  @apply bottom-0 left-0 right-0;
}
</style>