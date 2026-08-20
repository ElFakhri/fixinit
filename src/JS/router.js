import { createRouter, createWebHistory } from 'vue-router'
import Home from '../Home.vue' // Sesuaikan letak folder jika berbeda
import Login from '../Login.vue'
import Register from '../Register.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/Register',
    name: 'Register',
    component: Register
  },
  {
    path: '/form',
    name: 'Form',
    component: 'Form'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router