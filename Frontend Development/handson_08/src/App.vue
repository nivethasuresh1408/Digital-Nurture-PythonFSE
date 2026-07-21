<template>
  <Header />

  <main class="container">
    <RouterView />
  </main>
</template>

<script setup>
import Header from './components/Header.vue'
</script>

<style>
*{
  margin:0;
  padding:0;
  box-sizing:border-box;
}

body{
  font-family:Arial, Helvetica, sans-serif;
  background:#f4f6f8;
}

.container{
  width:90%;
  margin:auto;
  margin-top:30px;
}
</style>