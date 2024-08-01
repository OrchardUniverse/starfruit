<!-- App.vue -->
<template>
  <div id="app">
    <header>
      <nav>
        <div class="logo">Model Hub</div>
        <div class="search-bar">
          <input v-model="searchQuery" @input="searchModels" placeholder="Search models...">
        </div>
        <div class="nav-links">
          <a href="#" class="nav-link">Models</a>
          <a href="#" class="nav-link">Datasets</a>
          <a href="#" class="nav-link">Docs</a>
        </div>
      </nav>
    </header>

    <main>
      <div class="sidebar">
        <h3>Filter by tags</h3>
        <div v-for="tag in allTags" :key="tag" class="tag-filter">
          <input type="checkbox" :id="tag" :value="tag" v-model="selectedTags">
          <label :for="tag">{{ tag }}</label>
        </div>
      </div>

      <div class="content">
        <h2>Models</h2>
        <div class="model-grid">
          <div v-for="model in filteredModels" :key="model.id" class="model-card">
            <h3>{{ model.name }}</h3>
            <p>{{ model.description }}</p>
            <div class="model-tags">
              <span v-for="tag in model.tags" :key="tag" class="tag">{{ tag }}</span>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      selectedTags: [],
      models: [
        { id: 1, name: 'BERT', description: 'Bidirectional Encoder Representations from Transformers', tags: ['nlp', 'transformer'] },
        { id: 2, name: 'GPT-3', description: 'Generative Pre-trained Transformer 3', tags: ['nlp', 'transformer', 'text-generation'] },
        { id: 3, name: 'ResNet', description: 'Residual Networks for image classification', tags: ['computer-vision', 'classification'] },
        // Add more models here
      ],
    };
  },
  computed: {
    allTags() {
      return [...new Set(this.models.flatMap(model => model.tags))];
    },
    filteredModels() {
      return this.models.filter(model => {
        const matchesSearch = model.name.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                              model.description.toLowerCase().includes(this.searchQuery.toLowerCase());
        const matchesTags = this.selectedTags.length === 0 || this.selectedTags.every(tag => model.tags.includes(tag));
        return matchesSearch && matchesTags;
      });
    },
  },
  methods: {
    searchModels() {
      // This method is called on input, but filtering is handled by the computed property
    },
  },
};
</script>

<style scoped>
#app {
  font-family: Arial, sans-serif;
  color: #333;
}

header {
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #4a4a4a;
}

.search-bar input {
  width: 300px;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.nav-links {
  display: flex;
  gap: 1rem;
}

.nav-link {
  color: #4a4a4a;
  text-decoration: none;
  font-weight: 500;
}

main {
  display: flex;
  max-width: 1200px;
  margin: 80px auto 0;
  padding: 2rem;
}

.sidebar {
  width: 250px;
  padding-right: 2rem;
}

.tag-filter {
  margin-bottom: 0.5rem;
}

.content {
  flex-grow: 1;
}

.model-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

.model-card {
  background-color: #fff;
  border: 1px solid #e1e4e8;
  border-radius: 6px;
  padding: 1rem;
  transition: box-shadow 0.3s ease;
}

.model-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.model-tags {
  margin-top: 0.5rem;
}

.tag {
  display: inline-block;
  background-color: #e1e4e8;
  color: #586069;
  padding: 0.2rem 0.5rem;
  border-radius: 12px;
  font-size: 0.8rem;
  margin-right: 0.5rem;
  margin-bottom: 0.5rem;
}
</style>