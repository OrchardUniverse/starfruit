import { createRouter, createWebHistory } from 'vue-router';
import ModelList from '../components/ModelList.vue';
import ModelDetail from '../components/ModelDetail.vue';
import HuggingFaceModels from '../components/HuggingFaceModels.vue';
import HuggingFaceModelDetail from '../components/HuggingFaceModelDetail.vue';

const routes = [
  { path: '/', redirect: '/models' },
  { path: '/models', component: ModelList },
  { path: '/model/:id', component: ModelDetail, name: 'ModelDetail' },
  { path: '/datasets', component: { template: '<div>Datasets Page</div>' } },
  { path: '/huggingface_models', component: HuggingFaceModels },
  { path: '/huggingface_model/:id', component: HuggingFaceModelDetail, name: 'HuggingFaceModelDetail' },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
