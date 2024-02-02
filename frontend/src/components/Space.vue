<script setup>
    import { useUserStore } from '../stores/user';
    import Header from './Header.vue';
    import PostInput from './PostInput.vue';
    import UpcomingMeetings from './UpcomingMeetings.vue';
    import 'flowbite/dist/flowbite.js'

    const userState = useUserStore();
    // import { ref, onMounted} from 'vue';
    // import checkToken  from '../utils.js';
    // import { useRouter } from 'vue-router';
    // import axios from 'axios';
    // onMounted( async () => {
    //     console.log('home page')
    //     console.log('mounted')
    //         // create a router 
    //         const router = useRouter();
    //         const token = checkToken();
    //         console.log(token)
    //         if (token === null) {
    //             router.push({ name: 'Login' });
    //         }
    //         const data = await fetch(`http://localhost:8000/api/user/${token.sub}`, {
    //             mathod: 'GET',
    //             headers: {
    //                 'x-access-token': localStorage.getItem('token'),
    //                 'Content-Type': 'application/json',
    //             }
    //         })

    //         const response = await data.json();
    //         if (response.message === 'Token is not valid') {
    //             router.push({ name: 'Login' });
    //         }else {
    //             console.log(response)
    //         }
    // })
</script>

<template>
    <div class="container mx-auto">
        <Header />

        <div class="flex flex-row justify-evenly">
            <PostInput />
            <UpcomingMeetings/>
        </div>
    </div>
</template>