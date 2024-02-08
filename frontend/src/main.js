import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import './style.css'
import App from './App.vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faUserSecret)

const pinia = createPinia();
const app = createApp(App);

app.component('font-awesome-icon', FontAwesomeIcon) // Register component globally here

app.use(pinia)
app.use(router)
app.mount('#app')
