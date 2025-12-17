import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/HomePage.vue'; 
import About from '../views/AboutPage.vue'; 
import RegisterPage from '../views/RegisterPage.vue'; 
import LoginPage from '../views/LoginPage.vue'; 
import LKPage from '../views/LKPage.vue'; 
import KatalogPage from '../views/KatalogPage.vue'; 
import TarifPage from '../views/TarifPage.vue'; 
import BronPage from '../views/BronPage.vue'; 
import IndividPage from '../views/IndividPage.vue'; 
import RecoveryPage from '../views/RecoveryPage.vue';
//import AdminPanel from '../views/AdminPanel.vue';



const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/product/:id',
    name: 'Product',
    component: () => import('../views/ProductPage.vue'),
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterPage, 
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage, 
  },
  {
    path: '/lk',
    name: 'Lk',
    component: LKPage,
  },
  {
    path: '/katalog',
    name: 'Katalog',
    component: KatalogPage,
  },
  {
    path: '/tarif',
    name: 'Tarif',
    component: TarifPage,
  },
  {
    path: '/bron',
    name: 'Bron',
    component: BronPage,
  },
  {
    path: '/bron/:id', 
    component: BronPage,
    name: 'BronPage'
  },
  {
    path: '/katalog/:id',
    name: 'Individ',
    component: IndividPage,
  },
  {
    path: '/recovery',
    name: 'Recovery',
    component: RecoveryPage,
  },
{
  path: '/admin',
  name: 'AdminPanel',
  component: () => import('../views/AdminPanel.vue'),
  meta: { requiresAuth: true }
},
{
  path: '/admin-login',
  name: 'AdminLogin',
  component: () => import('../views/AdminLogin.vue')
}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;