<template>

<div class="course-card">

  <h3>{{ name }}</h3>

  <p><strong>Code:</strong> {{ code }}</p>

  <p><strong>Credits:</strong> {{ credits }}</p>

  <p><strong>Grade:</strong> {{ grade }}</p>

  <button @click="$emit('enroll')">

    Enroll

  </button>

</div>

</template>

<script setup>

defineProps({

  name:String,
  code:String,
  credits:Number,
  grade:String

})

defineEmits(['enroll'])

</script>

<style scoped>

.course-card{

  background:white;

  padding:20px;

  margin:20px 0;

  border-radius:10px;

  box-shadow:0 2px 10px rgba(0,0,0,.2);

}

button{

  margin-top:10px;

  padding:10px 18px;

  background:#2c5aa0;

  color:white;

  border:none;

  border-radius:5px;

  cursor:pointer;

}

button:hover{

  background:#1f4478;

}

</style>