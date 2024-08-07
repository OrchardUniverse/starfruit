<template>
  <header class="bg-blue-600 text-white p-4">
    <nav class="container mx-auto flex justify-between items-center">
      <div class="text-2xl font-bold">
        <router-link to="/">Starfruit Model Hub</router-link>
      </div>
      <div>
        <router-link
          to="/models"
          class="mx-4 hover:underline"
          :class="{ 'text-yellow-300': isActive('/models') }"
        >
          Models
        </router-link>
        <router-link
          to="/huggingface_models"
          class="mx-4 hover:underline"
          :class="{ 'text-yellow-300': isActive('/huggingface_models') }"
        >
          HuggingFace Models
        </router-link>
        <router-link
          to="/datasets"
          class="mx-4 hover:underline"
          :class="{ 'text-yellow-300': isActive('/datasets') }"
        >
          Datasets
        </router-link>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'MainHeader',
  methods: {
    isActive(route) {
      return this.$route.path === route;
    },
  },
};
</script>
