<template>
  <header class="header">
    <h1>Student Portal</h1>

    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/courses">Courses</RouterLink>
      <RouterLink to="/profile">Profile</RouterLink>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.header{
  background:#2c5aa0;
  color:white;
  padding:20px;
  display:flex;
  justify-content:space-between;
  align-items:center;
}

nav{
  display:flex;
  gap:20px;
}

a{
  color:white;
  text-decoration:none;
  font-weight:bold;
}

a.router-link-active{
  text-decoration:underline;
}
</style>