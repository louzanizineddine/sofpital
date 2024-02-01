import { createRouter, createWebHistory } from "vue-router";

import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import Logout from '../components/Logout.vue'


const routes =
[
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/register',
        name: 'Register',
        component: Register,
    },
    {
        path: '/logout',
        name: 'Logout',
        component: Logout
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router;