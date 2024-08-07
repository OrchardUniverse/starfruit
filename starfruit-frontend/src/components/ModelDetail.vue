<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Model Detail</h1>
    <div v-if="model">
      <p><strong>ID:</strong> {{ model.id }}</p>
      <p><strong>Created At:</strong> {{ model.created_at }}</p>
      <p><strong>Tags:</strong> {{ model.tags.join(', ') }}</p>
      <p><strong>Pipeline Tag:</strong> {{ model.pipeline_tag }}</p>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      model: null,
    };
  },
  created() {
    const modelId = this.$route.params.id;
    // Fetch model details based on the model ID
    // For now, we'll use sample data
    const models = [
      { id: 1, created_at: '2024-01-01', tags: ['tag1', 'tag2'], pipeline_tag: 'pipeline1' },
      { id: 2, created_at: '2024-01-02', tags: ['tag3'], pipeline_tag: 'pipeline2' },
    ];
    this.model = models.find(model => model.id == modelId);
  },
};
</script>

