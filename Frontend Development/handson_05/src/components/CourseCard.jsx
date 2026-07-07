function CourseCard({

  name,

  code,

  credits,

  grade,

  onEnroll

}) {

  return (

    <div className="course-card">

      <h2>{name}</h2>

      <p>

        <strong>Code:</strong> {code}

      </p>

      <p>

        <strong>Credits:</strong> {credits}

      </p>

      <p>

        <strong>Grade:</strong> {grade}

      </p>

      <button onClick={onEnroll}>

        Enroll

      </button>

    </div>

  );

}

export default CourseCard;