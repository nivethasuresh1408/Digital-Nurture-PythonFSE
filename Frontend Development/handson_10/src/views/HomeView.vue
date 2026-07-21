<template>
  <div class="home">

    <h2>Welcome to Student Portal</h2>

    <p>
      This project demonstrates:
    </p>

    <ul>
      <li>Axios API Integration</li>
      <li>Centralized API Layer</li>
      <li>Advanced Pinia State Management</li>
      <li>Global Error Handling</li>
    </ul>

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

margin-top:70px;

}

ul{

list-style:none;

margin:25px 0;

}

li{

margin:10px;

}

button{

padding:12px 20px;

background:#2c5aa0;

color:white;

border:none;

border-radius:6px;

cursor:pointer;

}

button:hover{

background:#1f4478;

}

</style>