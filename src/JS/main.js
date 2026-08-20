import { createApp } from 'vue'
import '../style/style.css'
import App from '../App.vue'
import router from './router.js' // 1. Panggil file router tadi

const app = createApp(App)

app.use(router) // 2. Pasang router ke dalam aplikasi
app.mount('#app')