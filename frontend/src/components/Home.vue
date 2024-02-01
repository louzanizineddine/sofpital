<script setup>
    import { ref, onMounted} from 'vue';
    import checkToken  from '../utils.js';
    import { useRouter } from 'vue-router';
    import axios from 'axios';
    onMounted( async () => {
        console.log('home page')
        console.log('mounted')
            // create a router 
            const router = useRouter();
            const token = checkToken();
            console.log(token)
            if (token === null) {
                router.push({ name: 'Login' });
            }
            const data = await fetch(`http://localhost:8000/api/user/${token.sub}`, {
                mathod: 'GET',
                headers: {
                    'x-access-token': localStorage.getItem('token'),
                    'Content-Type': 'application/json',
                }
            })

            const response = await data.json();
            if (response.message === 'Token is not valid') {
                router.push({ name: 'Login' });
            }else {
                console.log(response)
            }
    })
</script>

<template>

<section class="bg-gray-50 dark:bg-gray-900">
</section>
</template>