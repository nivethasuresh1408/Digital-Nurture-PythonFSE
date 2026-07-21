<template>

<h2>Enrolled Courses</h2>

<br>

<div

v-if="enrolledCourses.length===0"

>

No Courses Enrolled

</div>

<div

v-for="course in enrolledCourses"

:key="course.id"

class="card"

>

<h3>{{course.title}}</h3>

<p>ID : {{course.id}}</p>

</div>

<br>

<button

@click="store.$reset()"

>

Reset Enrollment

</button>

</template>

<script setup>

import {

storeToRefs

}

from 'pinia'

import {

useEnrollmentStore

}

from '../stores/enrollment'

const store=

useEnrollmentStore()

const{

enrolledCourses

}=storeToRefs(store)

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

padding:10px 18px;

background:red;

color:white;

border:none;

border-radius:5px;

cursor:pointer;

}

</style>