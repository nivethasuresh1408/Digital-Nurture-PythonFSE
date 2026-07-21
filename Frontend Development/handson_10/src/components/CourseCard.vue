<template>

<div class="card">

<h3>{{ title }}</h3>

<p>ID : {{ id }}</p>

<button @click="$emit('enroll', id)">

Enroll

</button>

</div>

</template>

<script setup>

defineProps({

id:Number,

title:String

})

defineEmits(['enroll'])

</script>

<style scoped>

.card{

background:white;

padding:20px;

margin:20px 0;

border-radius:10px;

box-shadow:0 2px 8px rgba(0,0,0,.2);

}

button{

margin-top:15px;

padding:10px 18px;

background:#2c5aa0;

color:white;

border:none;

border-radius:5px;

cursor:pointer;

}

</style>