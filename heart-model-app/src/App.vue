<template>
  <!-- <PredictPatient/> -->
  <TestComponent />
</template>

<script>
// import PredictPatient from './components/PredictPatient.vue';
import TestComponent from './components/TestComponent.vue';

export default {
  name: 'App',
  components: {
    
    TestComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
