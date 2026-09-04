import { createRouter, createWebHistory } from "vue-router";
import Home from "../Home.vue"; // Sesuaikan letak folder jika berbeda
import Login from "../Login.vue";
import Register from "../Register.vue";
import Form from "../Form.vue";
import Admin from "../Admin.vue";
import AdminSelesai from "../Admin_selesai.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/Register",
    name: "Register",
    component: Register,
  },
  {
    path: "/form",
    name: "Form",
    component: Form,
  },
  {
    path: "/Admin",
    name: "Admin",
    component: Admin,
  },
  {
    path: "/Admin_selesai",
    name: "AdminSelesai",
    component: AdminSelesai,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
