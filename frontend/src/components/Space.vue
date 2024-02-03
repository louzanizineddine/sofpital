<script setup>
    import { useUserStore } from '../stores/user';
    import Header from './Header.vue';
    import PostInput from './PostInput.vue';
    import UpcomingMeetings from './UpcomingMeetings.vue';
    import { useRouter } from 'vue-router';
    import { ref, onMounted} from 'vue';
    import 'flowbite/dist/flowbite.js';

    const router = useRouter()
    const userState = useUserStore();
    console.log(userState.user)
    userState.getToken();

    const loaded = ref(false);

    onMounted( async () => {
        console.log('personal learner space')
        console.log('mounted')
        if (!userState.loggedIn) {
            router.push({ name: 'Login' });
        }
        // check if user info is available
        if (userState.user === null) {
            console.log('fetching user info another time')
            const res = await userState.fetchUserInfo(userState.token.sub);
            if (res === null) {
                router.push({ name: 'Login' });
            }
            console.log(userState.user);
            loaded.value = true;
        }
    })


</script>

<script>
</script>
<template>
    <div class="container mx-auto">
        <template v-if="loaded">
            <Header />
    
            <div class="flex flex-row justify-evenly">
                <PostInput />
                <UpcomingMeetings/>
            </div>
        </template>
    </div>
</template>