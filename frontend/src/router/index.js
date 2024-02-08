import { createRouter, createWebHistory } from "vue-router";

import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import Logout from '../components/Logout.vue'
import Profile from '../components/Profile.vue'
import Dashboard from '../components/Dashboard.vue'
import Home from '../views/Home.vue'

const routes = [
    {
        path: '/',
        component: Home,
        name: 'Home',
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
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard,
        meta: {
            requiresAuth: true
        }
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
