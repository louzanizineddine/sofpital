<script setup>
    import { ref } from 'vue'
    import { useRouter } from 'vue-router';
    import {apiURL} from '../config'

    const router = useRouter();

    const form = ref({
        email: '',
        password: '',
        username: '',
        first_name: '',
        last_name: '',
        gender: '',
        role: '',
        subjects: [],
    });

    const handleRegister = async () => {
        const data = await fetch(`${apiURL}auth/signup`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(form.value),
        });
        const response = await data.json();
        console.log(response);

        if (response.status === 'success') {
            router.push({ name: 'Login' });
        }
    };

    const handleSubjectSelection = (subject) => {
    const index = form.value.subjects.indexOf(subject);
    if (index === -1) {
        form.value.subjects.push(subject);
    } else {
        form.value.subjects.splice(index, 1);
    }
};

</script>
<!-- 
bg-gray-50 dark:bg-gray-900 -->
<template>
    <html>
        <body class="leading-normal tracking-normal text-white gradient">
        <!-- <section class="bg-gray-50 dark:bg-gray-900"> -->
        <nav id="header" class="fixed w-full z-30 top-0 text-white">
        <div class="w-full container mx-auto flex flex-wrap items-center justify-between mt-0 py-2">
            <div class="pl-4 flex items-center">
                <router-link :to="{name: 'Home'}" class="toggleColour text-white no-underline hover:no-underline font-bold text-2xl lg:text-4xl" href="#">
                <!--Icon from: http://www.potlabicons.com/ -->
                <!-- <svg class="h-8 fill-current inline" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512.005 512.005">
                <rect fill="#2a2a31" x="16.539" y="425.626" width="479.767" height="50.502" transform="matrix(1,0,0,1,0,0)" />
                <path
                    class="plane-take-off"
                    d=" M 510.7 189.151 C 505.271 168.95 484.565 156.956 464.365 162.385 L 330.156 198.367 L 155.924 35.878 L 107.19 49.008 L 211.729 230.183 L 86.232 263.767 L 36.614 224.754 L 0 234.603 L 45.957 314.27 L 65.274 347.727 L 105.802 336.869 L 240.011 300.886 L 349.726 271.469 L 483.935 235.486 C 504.134 230.057 516.129 209.352 510.7 189.151 Z "
                />
                </svg> -->
                <img src="./../views/logo.png" alt="Icon" style="width: 50px; height: 50px;" class="inline" />
                Sofpital
                </router-link>
            </div>
            <div class="block lg:hidden pr-4">
            <button id="nav-toggle" class="flex items-center p-1 text-pink-800 hover:text-gray-900 focus:outline-none focus:shadow-outline transform transition hover:scale-105 duration-300 ease-in-out">
                <svg class="fill-current h-6 w-6" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <title>Menu</title>
                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
                </svg>
            </button>
            </div>
            <div class="w-full flex-grow lg:flex lg:items-center lg:w-auto hidden mt-2 lg:mt-0 bg-white lg:bg-transparent text-black p-4 lg:p-0 z-20" id="nav-content">
            <ul class="list-reset lg:flex justify-end flex-1 items-center">
                <!-- <li class="mr-3">
                <a class="inline-block py-2 px-4 text-black font-bold no-underline" href="#howitworks">How It Works</a>
                </li>
                <li class="mr-3">
                <a class="inline-block text-black font-bold no-underline hover:text-gray-800 hover:text-underline py-2 px-4" href="#Pricing">Pricing</a>
                </li> -->
                <li class="mr-3">
                <a class="inline-block text-black no-underline hover:text-gray-800 hover:text-underline py-2 px-4" href="#"><router-link :to="{name: 'Home'}">Home</router-link></a>
                </li>
            </ul>
            <button
                id="navAction"
                class="mx-auto lg:mx-0 hover:underline bg-white text-gray-800 font-bold rounded-full mt-4 lg:mt-0 py-4 px-8 shadow opacity-75 focus:outline-none focus:shadow-outline transform transition hover:scale-105 duration-300 ease-in-out">
                <router-link :to="{name: 'Login'}">Sign in</router-link>
            </button>
            </div>
        </div>
        <hr class="border-b border-gray-100 opacity-25 my-0 py-0" />
            </nav>
        <div class="pt-24">
        <!-- <section class="bg-gray-50 dark:bg-gray-900 gradient"> -->
            <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
                <div
                    class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                    <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                        <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                            Register new account
                        </h1>
                        <form class="max-w-sm mx-auto" @submit.prevent="handleRegister">
                            <div class="mb-5">
                                <label 
                                    for="email"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email</label>
                                    <input 
                                    type="email" 
                                    id="email"
                                    v-model="form.email"
                                    class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
                                    placeholder="youremail.com" required>
                            </div>
                            <div class="mb-5">
                                <label for="username" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">User
                                    name</label>
                                <input 
                                    type="username" 
                                    id="username"
                                    v-model="form.username"
                                    class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
                                    placeholder="amin" required>
                            </div>
                            <div class="mb-5">
                                <label for="firstname"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">First
                                    name</label>
                                <input 
                                    type="firstname"
                                    id="firstname"
                                    v-model="form.first_name"
                                    class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
                                    placeholder="" required>
                            </div>

                            <div class="mb-5">
                                <label for="lastname" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Last
                                    name</label>
                                <input 
                                    type="lastname" 
                                    id="lastname"
                                    v-model="form.last_name"
                                    class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
                                    placeholder="" required>
                            </div>
                            <div class="mb-5">
                                <label for="password"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                                <input type="password" id="password"
                                    v-model="form.password"
                                    class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
                                    required>
                            </div>
                            <div class="mb-5">

                                <label for="gender"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">gender</label>
                                <select id="gender"
                                    v-model="form.gender"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">

                                    <option>male</option>
                                    <option>female</option>
                                </select>
                            </div>

                            <div class="mb-5">

                                <label for="role" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Use
                                    sofpital
                                    as</label>
                                <select id="role"
                                    v-model="form.role"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">

                                    <option>learner</option>
                                    <option>tutor</option>
                                </select>
                            </div>

                            <div v-if="form.role === 'tutor'" class="mb-5">
                                <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                                    Subjects
                                </label>
                                <div class="flex flex-wrap">
                                    <div
                                        v-for="subject in ['Linux', 'Java', 'Python', 'Windows', 'Programming']"
                                        :key="subject"
                                        @click="handleSubjectSelection(subject)"
                                        class="cursor-pointer bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 text-gray-900 dark:text-white text-sm rounded-lg p-2.5 mr-2 mb-2"
                                        :class="{ 'bg-blue-500 text-white': form.subjects.includes(subject) }"
                                    >
                                        {{ subject }}
                                    </div>
                                </div>
                            </div>

                            <button type="submit"
                                class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 gradient">Register
                                new account</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <!-- </section> -->
    </body>
</html>
</template>

<style scoped>
.gradient {
    background: linear-gradient(90deg, #daae51 10%, #1956b5 87%);
}
</style>