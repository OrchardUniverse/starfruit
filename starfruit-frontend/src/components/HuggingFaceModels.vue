<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">HuggingFace Models</h1>
    <div class="mb-4 flex">
      <input
        v-model="search"
        type="text"
        placeholder="Search models..."
        class="p-2 border rounded flex-grow"
      />
      <button
        @click="searchModels"
        class="ml-2 p-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        Search
      </button>
    </div>
    <ul>
      <li
        v-for="model in filteredModels"
        :key="model.id"
        class="p-4 mb-2 border rounded cursor-pointer hover:bg-gray-100"
      >
        <p><strong>ID:</strong> {{ model.id }}</p>
        <p><strong>Created At:</strong> {{ model.created_at }}</p>
        <p><strong>Tags:</strong> {{ model.tags }}</p>
        <p><strong>Pipeline Tag:</strong> {{ model.pipeline_tag }}</p>
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
        model.id.toLowerCase().includes(this.search.toLowerCase())
      );
    },
  },
  methods: {
    async fetchModels() {
      try {
        const response = await axios.get('http://localhost:9966/api/huggingface_models');
        this.models = response.data;
      } catch (error) {
        console.error('Error fetching models:', error);
      }
    },
    async searchModels() {
      try {
        const response = await axios.post('http://localhost:9966/api/huggingface_models/search', {
          query: this.search
        });
        this.models = response.data;
      } catch (error) {
        console.error('Error searching models:', error);
      }
    },
  },
  created() {
    this.fetchModels();
  },
};
</script>
