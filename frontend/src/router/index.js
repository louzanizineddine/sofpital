import { createRouter, createWebHistory } from "vue-router";

import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import Logout from '../components/Logout.vue'
import Profile from '../components/Profile.vue'
import Dashboard from '../components/Dashboard.vue'
import Home from '../views/Home.vue'
import PostInput from '../components/PostInput.vue'
import LearnerOffers from '../components/LearnerOffers.vue'
import LearnerPosts from '../components/LearnerPosts.vue'
import LearnerMeetings from '../components/LearnerMeetings.vue'
import OffersForOnePost from '../components/OffersForOnePost.vue'
import Room from '../components/Room.vue'

import TutorOffers from '../components/Tutor/TutorOffers.vue'
import TutorMeetings from '../components/Tutor/TutorMeetings.vue'
import TutorRecommendations from '../components/Tutor/TutorRecommendations.vue'
import PasswordReset from '../components/PasswordReset.vue'


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
        path: '/reset_password',
        name: 'PasswordReset',
        component: PasswordReset,
    },
    {
        path: '/post_input',
        name: 'PostInput',
        component: PostInput,
        meta: {
            requiresAuth: true
        }
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
    },
    {
        path: '/learner_offers',
        name: 'LearnOffers',
        component: LearnerOffers,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/learner_posts',
        name: 'LearnerPosts',
        component: LearnerPosts,
        meta: {
            requiresAuth: true
        }
    },
    {
        path:'/learner_posts/post/:id/recieved_offers',
        name: 'OffersForOnePost',
        component: OffersForOnePost,
        meta :{
            requiresAuth: true
        }
    },
    {
        path: '/learner_meetings',
        name: 'LearnerMeetings',
        component: LearnerMeetings,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/tutor_recommendations',
        name: 'TutorRecommendations',
        component: TutorRecommendations,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/tutor_offers',
        name: 'TutorOffers',
        component: TutorOffers,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/tutor_meetings',
        name: 'TutorMeetings',
        component: TutorMeetings,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/room',
        name: 'Room',
        component: Room,
        meta: {
            requiresAuth: true
        }
    }
    ,{
        path: '/:pathMatch(.*)*',
        redirect: { name: 'Home' }
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
