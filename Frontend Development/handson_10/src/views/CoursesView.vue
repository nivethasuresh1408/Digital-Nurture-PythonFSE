<template>

<h2>Available Courses</h2>

<br>

<div v-if="loading">

Loading Courses...

</div>

<div v-else>

<CourseCard

v-for="course in courses"

:key="course.id"

:id="course.id"

:title="course.title"

@enroll="enrollCourse"

/>

</div>

</template>

<script setup>

import { ref,onMounted } from 'vue'

import CourseCard from '../components/CourseCard.vue'

import { getAllCourses }

from '../api/courseApi'

import {

useEnrollmentStore

}

from '../stores/enrollment'

const store=useEnrollmentStore()

const courses=ref([])

const loading=ref(true)

onMounted(async()=>{

try{

    const apiCourses = await getAllCourses()

const courseNames = [
  "Data Structures",
  "Operating Systems",
  "Database Management",
  "Computer Networks",
  "Software Engineering"
]

courses.value = apiCourses.map((course, index) => ({
  id: course.id,
  title: courseNames[index] || `Course ${course.id}`
}))

}

catch(error){

alert(error.message)

}

finally{

loading.value=false

}

})

function enrollCourse(id){

store.fetchAndEnroll(id)

}

</script>