from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

assignments = {}
submissions = {}
assignment_counter = [1]

# GET all assignments
@app.route("/assignments", methods=["GET"])
def get_assignments():
    return jsonify(list(assignments.values()))

# GET single assignment by ID
@app.route("/assignments/<int:aid>", methods=["GET"])
def get_assignment(aid):
    if aid not in assignments:
        return jsonify({"error": "Assignment not found"}), 404
    return jsonify(assignments[aid])

# POST create assignment
@app.route("/assignments", methods=["POST"])
def create_assignment():
    data = request.json
    if not data or not all(k in data for k in ["title", "description", "deadline"]):
        return jsonify({"error": "Missing required fields: title, description, deadline"}), 400
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

# PUT update assignment
@app.route("/assignments/<int:aid>", methods=["PUT"])
def update_assignment(aid):
    if aid not in assignments:
        return jsonify({"error": "Assignment not found"}), 404
    data = request.json
    if "title" in data:
        assignments[aid]["title"] = data["title"]
    if "description" in data:
        assignments[aid]["description"] = data["description"]
    if "deadline" in data:
        assignments[aid]["deadline"] = data["deadline"]
    assignments[aid]["updated_at"] = datetime.utcnow().isoformat()
    return jsonify(assignments[aid])

# DELETE assignment
@app.route("/assignments/<int:aid>", methods=["DELETE"])
def delete_assignment(aid):
    if aid not in assignments:
        return jsonify({"error": "Assignment not found"}), 404
    del assignments[aid]
    submissions.pop(aid, None)
    return jsonify({"message": "Assignment deleted successfully"})

# POST submit assignment
@app.route("/assignments/<int:aid>/submit", methods=["POST"])
def submit_assignment(aid):
    if aid not in assignments:
        return jsonify({"error": "Assignment not found"}), 404
    data = request.json
    if not data or not all(k in data for k in ["student_name", "answer"]):
        return jsonify({"error": "Missing required fields: student_name, answer"}), 400
    if aid not in submissions:
        submissions[aid] = []
    submissions[aid].append({
        "student_name": data["student_name"],
        "answer": data["answer"],
        "submitted_at": datetime.utcnow().isoformat()
    })
    return jsonify({"message": "Submitted successfully"}), 201

# GET all submissions for an assignment
@app.route("/assignments/<int:aid>/submissions", methods=["GET"])
def get_submissions(aid):
    if aid not in assignments:
        return jsonify({"error": "Assignment not found"}), 404
    return jsonify(submissions.get(aid, []))

# GET submission stats (count)
@app.route("/assignments/<int:aid>/stats", methods=["GET"])
def get_stats(aid):
    if aid not in assignments:
        return jsonify({"error": "Assignment not found"}), 404
    count = len(submissions.get(aid, []))
    return jsonify({
        "assignment_id": aid,
        "title": assignments[aid]["title"],
        "submission_count": count
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
