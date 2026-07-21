<template>

<div v-if="course">

<h2>{{ course.name }}</h2>

<p><strong>Code :</strong> {{ course.code }}</p>

<p><strong>Credits :</strong> {{ course.credits }}</p>

<p><strong>Grade :</strong> {{ course.grade }}</p>

<br>

<button @click="enrollCourse">

Enroll

</button>

</div>

<div v-else>

<h2>Course Not Found</h2>

</div>

</template>

<script setup>

import { computed } from 'vue'

import { useRoute,useRouter } from 'vue-router'

import { useEnrollmentStore } from '../stores/enrollment'

const route=useRoute()

const router=useRouter()

const store=useEnrollmentStore()

const courses=[

{id:1,name:'Data Structures',code:'CS101',credits:4,grade:'A'},

{id:2,name:'Operating Systems',code:'CS102',credits:3,grade:'A+'},

{id:3,name:'Database Management',code:'CS103',credits:4,grade:'B+'},

{id:4,name:'Computer Networks',code:'CS104',credits:3,grade:'A'},

{id:5,name:'Software Engineering',code:'CS105',credits:4,grade:'A'}

]

const course=computed(()=>{

return courses.find(

c=>c.id==route.params.id

)

})

function enrollCourse(){

store.enroll(course.value)

router.push('/profile')

}

</script>

<style scoped>

button{

padding:10px 20px;

background:#2c5aa0;

color:white;

border:none;

border-radius:5px;

cursor:pointer;

}

</style>