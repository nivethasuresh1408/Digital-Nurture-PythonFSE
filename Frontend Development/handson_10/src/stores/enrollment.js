import { defineStore } from 'pinia'
import { ref } from 'vue'

import { getCourseById } from '../api/courseApi'

export const useEnrollmentStore = defineStore('enrollment', () => {

  const enrolledCourses = ref([])

  async function fetchAndEnroll(courseId) {

    try {

        const course = await getCourseById(courseId)

const courseNames = {
  1: "Data Structures",
  2: "Operating Systems",
  3: "Database Management",
  4: "Computer Networks",
  5: "Software Engineering"
}

enrolledCourses.value.push({
  id: course.id,
  title: courseNames[course.id]
})

    } catch (error) {

      alert(error.message)

    }

  }

  function $reset() {

    enrolledCourses.value = []

  }

  return {

    enrolledCourses,

    fetchAndEnroll,

    $reset

  }

})