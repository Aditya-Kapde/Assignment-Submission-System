from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

assignments = {}
submissions = {}
assignment_counter = [1]

@app.route("/assignments", methods=["GET"])
def get_assignments():
    return jsonify(list(assignments.values()))

@app.route("/assignments", methods=["POST"])
def create_assignment():
    data = request.json
    aid = assignment_counter[0]
    assignment_counter[0] += 1
    assignments[aid] = {
        "id": aid,
        "title": data["title"],
        "description": data["description"],
        "deadline": data["deadline"],
        "created_at": datetime.utcnow().isoformat()
    }
    return jsonify(assignments[aid]), 201

@app.route("/assignments/<int:aid>/submit", methods=["POST"])
def submit_assignment(aid):
    if aid not in assignments:
        return jsonify({"error": "Assignment not found"}), 404
    data = request.json
    if aid not in submissions:
        submissions[aid] = []
    submissions[aid].append({
        "student_name": data["student_name"],
        "answer": data["answer"],
        "submitted_at": datetime.utcnow().isoformat()
    })
    return jsonify({"message": "Submitted successfully"}), 201

@app.route("/assignments/<int:aid>/submissions", methods=["GET"])
def get_submissions(aid):
    if aid not in assignments:
        return jsonify({"error": "Assignment not found"}), 404
    return jsonify(submissions.get(aid, []))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)