import { useState } from "react";

function StudentProfile() {

  const [profile, setProfile] = useState({

    name: "",

    email: "",

    semester: ""

  });

  function handleChange(event) {

    setProfile({

      ...profile,

      [event.target.name]: event.target.value

    });

  }

  return (

    <div className="profile">

      <h2>Student Profile</h2>

      <input
        type="text"
        name="name"
        placeholder="Enter Name"
        value={profile.name}
        onChange={handleChange}
      />

      <input
        type="email"
        name="email"
        placeholder="Enter Email"
        value={profile.email}
        onChange={handleChange}
      />

      <input
        type="text"
        name="semester"
        placeholder="Semester"
        value={profile.semester}
        onChange={handleChange}
      />

      <div className="profile-output">

        <p><strong>Name:</strong> {profile.name}</p>

        <p><strong>Email:</strong> {profile.email}</p>

        <p><strong>Semester:</strong> {profile.semester}</p>

      </div>

    </div>

  );

}

export default StudentProfile;