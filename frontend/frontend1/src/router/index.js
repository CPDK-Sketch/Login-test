import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import Returns from '../views/Returns.vue';
import Admin from '../views/Admin.vue';
import Billing from '../views/Billing.vue';
import Hub from '../views/Hub.vue';

const routes = [
  { path: '/', name: 'Login', component: Login },
  { path: '/returns', name: 'Returns', component: Returns },
  { path: '/admin', name: 'Admin', component: Admin },
  { path: '/billing', name: 'Billing', component: Billing },
  { path: '/hub', name: 'Hub', component: Hub }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
