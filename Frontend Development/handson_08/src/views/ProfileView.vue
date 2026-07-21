<template>

<h2>Student Profile</h2>

<br>

<h3>

Enrolled Courses

</h3>

<div

v-for="course in store.enrolledCourses"

:key="course.id"

class="course"

>

<h4>{{course.name}}</h4>

<p>{{course.code}}</p>

<p>{{course.credits}} Credits</p>

<button

@click="store.unenroll(course.id)"

>

Remove

</button>

</div>

<br>

<h3>

Total Credits :

{{store.totalCredits}}

</h3>

</template>

<script setup>

import { useEnrollmentStore }

from '../stores/enrollment'

const store=useEnrollmentStore()

</script>

<style scoped>

.course{

background:white;

padding:20px;

margin:15px 0;

box-shadow:0 2px 10px rgba(0,0,0,.2);

border-radius:10px;

}

button{

background:red;

color:white;

border:none;

padding:8px 15px;

border-radius:5px;

cursor:pointer;

}

</style>