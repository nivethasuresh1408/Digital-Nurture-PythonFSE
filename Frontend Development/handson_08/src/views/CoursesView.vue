<template>

<h2>Available Courses</h2>

<br>

<input
  type="text"
  placeholder="Search Course..."
  v-model="searchTerm"
/>

<br><br>

<CourseCard

  v-for="course in filteredCourses"

  :key="course.id"

  :name="course.name"

  :code="course.code"

  :credits="course.credits"

  :grade="course.grade"

  @enroll="enrollCourse(course)"
/>

</template>

<script setup>

import { ref, computed, onMounted } from 'vue'

import CourseCard from '../components/CourseCard.vue'

import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

const searchTerm = ref('')

const courses = ref([])

onMounted(()=>{

courses.value=[

{
id:1,
name:'Data Structures',
code:'CS101',
credits:4,
grade:'A'
},

{
id:2,
name:'Operating Systems',
code:'CS102',
credits:3,
grade:'A+'
},

{
id:3,
name:'Database Management',
code:'CS103',
credits:4,
grade:'B+'
},

{
id:4,
name:'Computer Networks',
code:'CS104',
credits:3,
grade:'A'
},

{
id:5,
name:'Software Engineering',
code:'CS105',
credits:4,
grade:'A'
}

]

})

const filteredCourses = computed(()=>{

return courses.value.filter(course=>

course.name.toLowerCase().includes(

searchTerm.value.toLowerCase()

)

)

})

function enrollCourse(course){

store.enroll(course)

alert(course.name+" enrolled successfully!")

}

</script>

<style scoped>

input{

width:300px;

padding:10px;

border:1px solid gray;

border-radius:5px;

}

</style>