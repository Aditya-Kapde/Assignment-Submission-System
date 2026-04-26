# 🚀 Student Assignment Submission System (DevOps Project)

A simple full-stack web application demonstrating a **complete CI/CD pipeline using Jenkins and Docker Compose**.

---

## 📌 Project Overview

This project allows:

* Teachers to create, edit, and delete assignments
* Students to submit answers
* Viewing assignments, submissions, and submission counts

The main focus is on **DevOps implementation**, including:

* Containerization using Docker & Docker Compose
* CI/CD pipeline using Jenkins
* Automated build and deployment

---

## 🧱 Tech Stack

### 🔹 Backend
* Python (Flask)

### 🔹 Frontend
* HTML, CSS, JavaScript
* Nginx (for serving frontend)

### 🔹 DevOps Tools
* Docker & Docker Compose
* Jenkins

---

## ⚙️ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /assignments | Get all assignments |
| GET | /assignments/{id} | Get single assignment |
| POST | /assignments | Create assignment |
| PUT | /assignments/{id} | Update assignment |
| DELETE | /assignments/{id} | Delete assignment |
| POST | /assignments/{id}/submit | Submit an answer |
| GET | /assignments/{id}/submissions | View submissions |
| GET | /assignments/{id}/stats | Get submission count |

---

## 📂 Project Structure

```
Assignment-Submission-System/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   └── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
└── README.md
```

---

## 🐳 Running with Docker Compose (Recommended)

### 1. Clone the repository
```bash
git clone https://github.com/Aditya-Kapde/Assignment-Submission-System.git
cd Assignment-Submission-System
```

### 2. Start everything with one command
```bash
docker-compose up -d --build
```

### 3. Access the Application
* Frontend → http://localhost:8181
* Backend API → http://localhost:5000

### 4. Stop everything
```bash
docker-compose down
```

---

## 🧪 API Testing (cURL)

### Create Assignment
```bash
curl -X POST http://localhost:5000/assignments \
-H "Content-Type: application/json" \
-d '{"title":"Math HW","description":"Solve integrals","deadline":"2025-12-31T23:59"}'
```

### Get All Assignments
```bash
curl http://localhost:5000/assignments
```

### Get Single Assignment
```bash
curl http://localhost:5000/assignments/1
```

### Update Assignment
```bash
curl -X PUT http://localhost:5000/assignments/1 \
-H "Content-Type: application/json" \
-d '{"title":"Updated Math HW","description":"Solve derivatives","deadline":"2025-12-31T23:59"}'
```

### Delete Assignment
```bash
curl -X DELETE http://localhost:5000/assignments/1
```

### Submit Assignment
```bash
curl -X POST http://localhost:5000/assignments/1/submit \
-H "Content-Type: application/json" \
-d '{"student_name":"Alice","answer":"The answer is 42"}'
```

### View Submissions
```bash
curl http://localhost:5000/assignments/1/submissions
```

### Get Submission Stats
```bash
curl http://localhost:5000/assignments/1/stats
```

---

## ⚙️ Jenkins CI/CD Pipeline

### Pipeline Stages
1. **Build (Maven - Demo)**
2. **Docker Compose Build**
3. **Run Containers**

### How it Works
```text
Code Push → Jenkins → Docker Compose Build → Run Containers → App Live
```

### Run Jenkins (Docker)
```bash
docker run -d \
  --name jenkins \
  -p 8081:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```

### Setup Jenkins
1. Open → http://localhost:8081
2. Unlock Jenkins
3. Install plugins
4. Create pipeline job
5. Paste `Jenkinsfile`
6. Click **Build Now**

---

## 👨‍💻 Author

**Aditya Kapde**

---

## ⭐ Conclusion

This project demonstrates a **complete DevOps lifecycle**, from development to deployment using Docker Compose and Jenkins.
