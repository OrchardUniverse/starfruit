<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Model List</h1>
    <input
      v-model="search"
      type="text"
      placeholder="Search models..."
      class="mb-4 p-2 border rounded"
    />
    <ul>
      <li
        v-for="model in filteredModels"
        :key="model"
        @click="viewModelDetail(model)"
        class="p-4 mb-2 border rounded cursor-pointer hover:bg-gray-100"
      >
        {{ model }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      search: '',
      models: [],
    };
  },
  computed: {
    filteredModels() {
      return this.models.filter(model =>
        model.toLowerCase().includes(this.search.toLowerCase())
      );
    },
  },
  methods: {
    viewModelDetail(id) {
      this.$router.push({ name: 'ModelDetail', params: { id } });
    },
    async fetchModels() {
      try {
        const response = await axios.get('http://localhost:9966/api/models');
        this.models = response.data;
      } catch (error) {
        console.error('Error fetching models:', error);
      }
    },
  },
  created() {
    this.fetchModels();
  },
};
</script>
