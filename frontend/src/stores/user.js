// stores/counter.js
import { defineStore } from 'pinia'
import checkToken from '../utils'

export const useUserStore = defineStore('User', {
  state: () => {
    return { 
        loggedIn: checkToken() == null ? false : true,
    }
  },
  // could also be defined as
  // state: () => ({ count: 0 })
  actions: {
    logout() {
        localStorage.removeItem('token');
        this.loggedIn = !this.loggedIn;
    },

    login(tk)
    {
        localStorage.setItem('token', tk);
        this.loggedIn = !this.loggedIn;
    }
  },
})