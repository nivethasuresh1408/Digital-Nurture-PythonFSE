<template>

<div class="home">

  <h2>Welcome to Student Portal</h2>

  <p>
    This application demonstrates Vue 3 Composition API,
    Vue Router and Pinia State Management.
  </p>

  <RouterLink to="/courses">
    <button>View Courses</button>
  </RouterLink>

</div>

</template>

<script setup>

import { RouterLink } from 'vue-router'

</script>

<style scoped>

.home{

  text-align:center;

  margin-top:100px;

}

button{

  margin-top:25px;

  padding:12px 20px;

  border:none;

  background:#2c5aa0;

  color:white;

  border-radius:6px;

  cursor:pointer;

}

button:hover{

  background:#1f4478;

}

</style>