import { useDispatch, useSelector } from "react-redux";

import { unenroll } from "../redux/enrollmentSlice";

function ProfilePage() {

  const dispatch = useDispatch();

  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (

    <div className="page">

      <h2>Student Profile</h2>

      <br />

      <h3>Enrolled Courses</h3>

      <br />

      {enrolledCourses.length === 0 ? (

        <p>No Courses Enrolled</p>

      ) : (

        enrolledCourses.map((course) => (

          <div
            key={course.id}
            className="course-card"
          >

            <h3>{course.name}</h3>

            <p>{course.code}</p>

            <button
              onClick={() =>
                dispatch(unenroll(course.id))
              }
            >

              Remove

            </button>

          </div>

        ))

      )}

    </div>

  );
}

export default ProfilePage;