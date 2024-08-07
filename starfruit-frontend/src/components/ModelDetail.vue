<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Model Detail</h1>
    <div v-if="model">
      <p><strong>ID:</strong> {{ model.id }}</p>
      <p><strong>Created At:</strong> {{ model.created_at }}</p>
      <p><strong>Tags:</strong> {{ model.tags }}</p>
      <p><strong>Pipeline Tag:</strong> {{ model.pipeline_tag }}</p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      model: null,
    };
  },
  async created() {
    const modelId = this.$route.params.id;
    try {
      const response = await axios.get(`http://localhost:9966/api/models/model/?id=${modelId}`);
      this.model = response.data;
    } catch (error) {
      console.error('Error fetching model:', error);
    }
  },
};
</script>
