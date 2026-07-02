from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route("/api/courses/<path:path>", methods=["GET"])
def gateway_course(path):

    url = f"http://localhost:5001/api/courses/{path}"

    response = requests.get(url)

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


@app.route(
    "/api/students/<int:id>/enroll",
    methods=["POST"]
)
def gateway_student(id):

    url = f"http://localhost:5002/api/students/{id}/enroll"

    response = requests.post(
        url,
        json=request.json
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


if __name__ == "__main__":

    app.run(port=5000)