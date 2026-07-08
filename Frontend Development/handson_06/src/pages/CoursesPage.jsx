import courses from "../data/courses";
import CourseCard from "../components/CourseCard";

function CoursesPage() {
  return (
    <div className="page">
      <h2>Available Courses</h2>

      <div className="course-grid">
        {courses.map((course) => (
          <CourseCard key={course.id} course={course} />
        ))}
      </div>
    </div>
  );
}

export default CoursesPage;