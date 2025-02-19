import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/HomePage.vue'; // Страница "Главная"
import About from '../views/AboutPage.vue'; // Страница "О нас"
import RegisterPage from '../views/RegisterPage.vue'; // Импортируем новую страницу
import LoginPage from '../views/LoginPage.vue'; 
import WherePage from '../views/WherePage.vue'; 
import KatalogPage from '../views/KatalogPage.vue'; 
import PokypkaPage from '../views/PokypkaPage.vue'; 
import KorzinaPage from '../views/KorzinaPage.vue'; 
import IndividPage from '../views/IndividPage.vue'; 
import RecoveryPage from '../views/RecoveryPage.vue'; 

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
    path: '/where',
    name: 'Where',
    component: WherePage,
  },
  {
    path: '/katalog',
    name: 'Katalog',
    component: KatalogPage,
  },
  {
    path: '/pokypka',
    name: 'Pokypka',
    component: PokypkaPage,
  },
  {
    path: '/korzina',
    name: 'Korzina',
    component: KorzinaPage,
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
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;