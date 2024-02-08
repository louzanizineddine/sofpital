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
    <div class="navbar bg-base-100">
        <div class="flex-1">
           <router-link to="/dashboard" class="text-lg font-bold text-primary">Sofpital</router-link>
        </div>
        <div class="flex-none gap-2">
            <div class="form-control">
                <input type="text" placeholder="Search" class="input input-bordered w-24 md:w-auto" />
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