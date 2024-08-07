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
        :key="model.id"
        @click="viewModelDetail(model.id)"
        class="p-4 mb-2 border rounded cursor-pointer hover:bg-gray-100"
      >
        {{ model.name }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      search: '',
      models: [
        // Sample data
        { id: 1, name: 'Model 1', created_at: '2024-01-01', tags: ['tag1', 'tag2'], pipeline_tag: 'pipeline1' },
        { id: 2, name: 'Model 2', created_at: '2024-01-02', tags: ['tag3'], pipeline_tag: 'pipeline2' },
        // Add more models as needed
      ],
    };
  },
  computed: {
    filteredModels() {
      return this.models.filter(model =>
        model.name.toLowerCase().includes(this.search.toLowerCase())
      );
    },
  },
  methods: {
    viewModelDetail(id) {
      this.$router.push({ name: 'ModelDetail', params: { id } });
    },
  },
};
</script>

