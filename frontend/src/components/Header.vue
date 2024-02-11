<script setup>
import { useUserStore } from '../stores/user';
import { useRouter } from 'vue-router';
const userState = useUserStore();
const router = useRouter();
const HandleLogout = () => {
    userState.logout();
    router.push({ name: 'Login' });
}

</script>

<template>
    <div class="navbar bg-base-100 shadow">
        <div class="w-2/4">
            <router-link to="/dashboard">
            <a class="text-blue-500 no-underline hover:no-underline font-bold text-2xl lg:text-4xl" href="#">
              <!--Icon from: http://www.potlabicons.com/ -->
              <!-- <svg class="h-8 fill-current inline" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512.005 512.005">
                <rect fill="#2a2a31" x="16.539" y="425.626" width="479.767" height="50.502" transform="matrix(1,0,0,1,0,0)" />
                <path
                  class="plane-take-off"
                  d=" M 510.7 189.151 C 505.271 168.95 484.565 156.956 464.365 162.385 L 330.156 198.367 L 155.924 35.878 L 107.19 49.008 L 211.729 230.183 L 86.232 263.767 L 36.614 224.754 L 0 234.603 L 45.957 314.27 L 65.274 347.727 L 105.802 336.869 L 240.011 300.886 L 349.726 271.469 L 483.935 235.486 C 504.134 230.057 516.129 209.352 510.7 189.151 Z "
                />
              </svg> -->
              <img src="../views/Screenshot_from_2024-02-10_14-57-26-removebg-preview (1).png" alt="Icon" style="width: 50px; height: 50px;" class="inline" />
              Sofpital
            </a></router-link>
            <!-- </a>class="text-5xl font-bold text-primary">Sofpital</router-link> -->
        </div>
        <div class="flex-none gap-2">
            <div class="navbar-center hidden lg:flex">
                <ul class="menu menu-horizontal px-1">
                    <li>
                        
                        <router-link to="/dashboard">Dashboard</router-link>
                    </li>
                    <li>
                        <template v-if="userState.user.role === 'learner'">
                            <router-link to="/learner_posts">posts</router-link>
                        </template>
                        <template v-else>
                            <router-link to="/tutor_recommendations">recommendations</router-link>
                        </template>
                    </li>
                    <li>
                        <template v-if="userState.user.role === 'learner'">
                            <router-link to="/learner_offers">offers</router-link>
                        </template>
                        <template v-else>
                            <router-link to="/tutor_offers">offers</router-link>
                        </template>
                    </li>
                    <li>
                        <template v-if="userState.user.role === 'learner'">
                            <router-link to="/learner_meetings">meetings</router-link>
                        </template>
                        <template v-else>
                            <router-link to="/tutor_meetings">meetings</router-link>
                        </template>
                    </li>
                </ul>
            </div>
            <div class="dropdown dropdown-end">
                <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
                    <div class="w-10 rounded-full">
                        <img alt="Tailwind CSS Navbar component"
                            src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
                    </div>
                </div>
                <ul tabindex="0" class="mt-3 z-[1] p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
                    <li>
                        <router-link to="/profile">Profile
                        </router-link>
                    </li>
                    <li><a>Settings</a></li>
                    <li><a @click="HandleLogout">Logout</a></li>
                </ul>
            </div>
        </div>
    </div>
</template>

<style scoped>
.gradient {
    background: linear-gradient(90deg, #daae51 10%, #1956b5 87%);
}
</style>
