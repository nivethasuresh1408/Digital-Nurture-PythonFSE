import { Link, useNavigate } from "react-router-dom";

import { useDispatch } from "react-redux";

import { enroll } from "../redux/enrollmentSlice";

function CourseCard({ course }) {

  const dispatch = useDispatch();

  const navigate = useNavigate();

  const handleEnroll = () => {

    dispatch(enroll(course));

    navigate("/profile");

  };

  return (

    <div className="course-card">

      <h2>{course.name}</h2>

      <p>Code : {course.code}</p>

      <p>Credits : {course.credits}</p>

      <p>Grade : {course.grade}</p>

      <Link to={`/courses/${course.id}`}>

        <button>View Details</button>

      </Link>

      <br /><br />

      <button onClick={handleEnroll}>

        Enroll

      </button>

    </div>

  );
}

export default CourseCard;