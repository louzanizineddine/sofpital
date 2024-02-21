// stores/counter.js
import { defineStore } from 'pinia'
import {checkToken} from '../utils'
import {apiURL} from '../config'


export const useUserStore = defineStore('User', {
  state: () => {
    return {
      loggedIn: checkToken() == null ? false : true,
      token: null,
      user: null,
      newSentOffer: false
    }
  },
  actions: {
    logout() {
      localStorage.removeItem('token');
      this.loggedIn = !this.loggedIn;
      this.token = null;
      this.user = null;
    },

    login(tk) {
      localStorage.setItem('token', tk);
      this.loggedIn = !this.loggedIn;
    },

    getToken() {
      this.token = checkToken();
    },

    async fetchUserInfo(user_id) {
      const data = await fetch(`${apiURL}user/${user_id}`, {
        mathod: 'GET',
        headers: {
          'x-access-token': localStorage.getItem('token'),
          'Content-Type': 'application/json',
        }
      })
      const response = await data.json();
      if (response.message === 'Token is not valid') {
        return null;
      } 
      this.user = response;
    }

  },
})
