import { useState, useEffect } from "react";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

import coursesData from "./data/courses";

import "./index.css";

function App() {

  const [courses, setCourses] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  const [searchTerm, setSearchTerm] = useState("");

  const [enrolledCourses, setEnrolledCourses] = useState([]);

  useEffect(() => {

    async function fetchCourses() {

      try {

        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts?_limit=5"
        );

        if (!response.ok) {

          throw new Error("Failed to fetch courses.");

        }

        const posts = await response.json();

        const fetchedCourses = posts.map((post, index) => ({
          id: post.id,
          name: coursesData[index]?.name || post.title,
          code: coursesData[index]?.code || `CS${101 + index}`,
          credits: coursesData[index]?.credits || 3,
          grade: coursesData[index]?.grade || "A"
        }));

        setCourses(fetchedCourses);

      } catch (err) {

        setError(err.message);

      } finally {

        setLoading(false);

      }

    }

    fetchCourses();

  }, []);

  useEffect(() => {

    console.log("Courses updated");

  }, [courses]);

  function handleEnroll(course) {

    if (!enrolledCourses.find(c => c.id === course.id)) {

      setEnrolledCourses([...enrolledCourses, course]);

    }

  }

  const filteredCourses = courses.filter(course =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (

    <>

      <Header
        siteName="Student Portal"
        enrolledCount={enrolledCourses.length}
      />

      <main>

        <h2>Available Courses</h2>

        <input
          type="text"
          placeholder="Search courses..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />

        {loading && <h3>Loading...</h3>}

        {error && <h3>{error}</h3>}

        <div className="course-grid">

          {!loading &&
            filteredCourses.map(course => (

              <CourseCard
                key={course.id}
                {...course}
                onEnroll={() => handleEnroll(course)}
              />

            ))}

        </div>

        <StudentProfile />

      </main>

      <Footer />

    </>

  );

}

export default App;