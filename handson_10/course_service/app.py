from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "courses.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY,
        name TEXT,
        code TEXT
    )
    """)

    cursor.execute(
        "INSERT OR IGNORE INTO courses VALUES (1,'Python','PY101')"
    )

    cursor.execute(
        "INSERT OR IGNORE INTO courses VALUES (2,'Java','JV101')"
    )

    conn.commit()
    conn.close()


@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM courses WHERE id=?",
        (id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:

        return jsonify(
            {
                "id": row[0],
                "name": row[1],
                "code": row[2]
            }
        )

    return jsonify({"message": "Course not found"}), 404


if __name__ == "__main__":

    init_db()

    app.run(port=5001)