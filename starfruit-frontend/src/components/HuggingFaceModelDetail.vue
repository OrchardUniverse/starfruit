<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">HuggingFace Model Detail</h1>
    <div v-if="model">
      <p><strong>ID:</strong> {{ model.id }}</p>
      <p><strong>Created At:</strong> {{ model.created_at }}</p>
      <p><strong>Tags:</strong> {{ model.tags }}</p>
      <p><strong>Pipeline Tag:</strong> {{ model.pipeline_tag }}</p>
      <button
        @click="downloadModel"
        class="mt-4 p-2 bg-green-600 text-white rounded hover:bg-green-700"
      >
        Download
      </button>
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
      const response = await axios.get(`http://localhost:9966/api/huggingface_models/model?id=${modelId}`);
      this.model = response.data;
    } catch (error) {
      console.error('Error fetching model:', error);
    }
  },
  methods: {
    async downloadModel() {
      try {
        // const response = await axios.post(`http://localhost:9966/api/huggingface_models/${this.model.id}/download`);
        alert('Download triggered successfully, start to download and please wait for minutes');

        const response = await axios.post('http://localhost:9966/api/huggingface_models/download', {
          id: this.model.id
        });

        alert('Successfully download the model: ' + response.data.id);
      } catch (error) {
        console.error('Error triggering download:', error);
      }
    },
  },
};
</script>

