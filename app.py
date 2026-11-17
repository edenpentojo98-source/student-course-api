
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Allow frontend applications to access this API
CORS(app)

# Sample course data
courses = [
    {
        "id": 1,
        "code": "IT101",
        "name": "Introduction to Information Technology",
        "instructor": "Mr. Santos",
        "units": 3
    },
    {
        "id": 2,
        "code": "CS102",
        "name": "Computer Programming",
        "instructor": "Ms. Reyes",
        "units": 3
    },
    {
        "id": 3,
        "code": "IT103",
        "name": "Web Development",
        "instructor": "Mr. Cruz",
        "units": 3
    },
    {
        "id": 4,
        "code": "IT104",
        "name": "Database Management",
        "instructor": "Ms. Garcia",
        "units": 3
    },
    {
        "id": 5,
        "code": "IT105",
        "name": "System Integration and Architecture",
        "instructor": "Mr. Dela Cruz",
        "units": 3
    }
]


# Home endpoint
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Student Course API",
        "status": "running"
    })


# Health check endpoint
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "success",
        "message": "Student Course API is running"
    }), 200


# Get all courses
@app.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify({
        "status": "success",
        "total_courses": len(courses),
        "courses": courses
    }), 200


# Get one course by ID
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return jsonify({
                "status": "success",
                "course": course
            }), 200

    return jsonify({
        "status": "error",
        "message": f"Course with ID {course_id} was not found"
    }), 404


# Run the application
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

