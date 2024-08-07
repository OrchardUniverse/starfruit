<template>
  <div>
    <MainHeader />
    <router-view />
  </div>
</template>

<script>
import MainHeader from './components/MainHeader.vue';

export default {
  name: 'App',
  components: {
    MainHeader,
  },
};
</script>

<style>
/* Add any global styles if needed */
</style>
