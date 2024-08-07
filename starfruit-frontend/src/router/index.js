import { createRouter, createWebHistory } from 'vue-router';
import ModelList from '../components/ModelList.vue';
import ModelDetail from '../components/ModelDetail.vue';

const routes = [
  { path: '/', component: ModelList },
  { path: '/model/:id', component: ModelDetail, name: 'ModelDetail' },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

