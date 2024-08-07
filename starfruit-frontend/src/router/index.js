import { createRouter, createWebHistory } from 'vue-router';
import ModelList from '../components/ModelList.vue';
import ModelDetail from '../components/ModelDetail.vue';
import HuggingFaceModels from '../components/HuggingFaceModels.vue';

const routes = [
  { path: '/', redirect: '/models' },
  { path: '/models', component: ModelList },
  { path: '/model/:id', component: ModelDetail, name: 'ModelDetail' },
  { path: '/huggingface_models', component: HuggingFaceModels },
  // Add a placeholder component for Datasets page
  { path: '/datasets', component: { template: '<div>Datasets Page</div>' } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
