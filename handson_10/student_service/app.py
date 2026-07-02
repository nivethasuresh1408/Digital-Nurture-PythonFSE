from flask import Flask, jsonify, request
import sqlite3
import requests

app = Flask(__name__)

DATABASE = "students.db"


def init_db():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    cursor.execute(
        "INSERT OR IGNORE INTO students VALUES (1,'Nivetha')"
    )

    conn.commit()

    conn.close()


@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll(id):

    data = request.get_json()

    course_id = data["course_id"]

    try:

        response = requests.get(
            f"http://localhost:5001/api/courses/{course_id}"
        )

    except requests.exceptions.ConnectionError:

        return jsonify(
            {
                "message":
                "Course Service unavailable"
            }
        ), 503

    if response.status_code != 200:

        return jsonify(
            {
                "message":
                "Course not found"
            }
        ), 404

    return jsonify(
        {
            "message":
            "Enrollment Successful"
        }
    )


if __name__ == "__main__":

    init_db()

    app.run(port=5002)