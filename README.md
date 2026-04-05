# 🚀 Student Assignment Submission System (DevOps Project)

A simple full-stack web application demonstrating a **complete CI/CD pipeline using Jenkins and Docker**.

---

## 📌 Project Overview

This project allows:

* Teachers to create assignments
* Students to submit answers
* Viewing assignments and submissions

The main focus is on **DevOps implementation**, including:

* Containerization using Docker
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

* Docker
* Jenkins

---

## ⚙️ Features

* Create assignments
* Submit assignments
* View assignments
* View submissions
* CI/CD pipeline with Jenkins
* Dockerized backend and frontend

---

## 📂 Project Structure

```
assignment-devops/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   └── Dockerfile
├── Jenkinsfile
└── README.md
```

---

## 🐳 Running the Project (Docker)

### 1. Clone the repository

```bash
git clone https://github.com/Aditya-Kapde/Assignment-Submission-System.git
cd assignment-devops
```

---

### 2. Run Backend

```bash
cd backend
docker build -t assignment-backend .
docker run -d -p 5000:5000 --name assignment-backend assignment-backend
```

---

### 3. Run Frontend

```bash
cd ../frontend
docker build -t assignment-frontend .
docker run -d -p 8080:80 --name assignment-frontend assignment-frontend
```

---

### 4. Access the Application

* Frontend → http://localhost:8080
* Backend API → http://localhost:5000

---

## 🧪 API Testing (cURL)

### Create Assignment

```bash
curl -X POST http://localhost:5000/assignments \
-H "Content-Type: application/json" \
-d '{"title":"Math HW","description":"Solve integrals","deadline":"2025-12-31T23:59"}'
```

---

### Get Assignments

```bash
curl http://localhost:5000/assignments
```

---

### Submit Assignment

```bash
curl -X POST http://localhost:5000/assignments/1/submit \
-H "Content-Type: application/json" \
-d '{"student_name":"Alice","answer":"The answer is 42"}'
```

---

### View Submissions

```bash
curl http://localhost:5000/assignments/1/submissions
```

---

## ⚙️ Jenkins CI/CD Pipeline

### Pipeline Stages

1. **Build (Maven - Demo)**
2. **Docker Build**
3. **Run Containers**

---

### How it Works

```text
Code Push → Jenkins → Docker Build → Run Containers → App Live
```

---

### Run Jenkins (Docker)

```bash
docker run -d \
  --name jenkins \
  -p 8081:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v ~/dev/devops/sas:/workspace \
  jenkins/jenkins:lts
```

---

### Setup Jenkins

1. Open → http://localhost:8081
2. Unlock Jenkins
3. Install plugins
4. Create pipeline job
5. Paste `Jenkinsfile`
6. Click **Build Now**

---

## 🔥 DevOps Workflow

* Developer triggers build
* Jenkins executes pipeline
* Docker builds images
* Containers are deployed automatically

---

## 📸 Screenshots (Optional)

* Jenkins Pipeline Success
* Running Containers
* Frontend UI

---

## 🚀 Future Improvements

* Add Kubernetes deployment
* Add Terraform for infrastructure
* Add database (MongoDB/PostgreSQL)
* Add authentication system

---

## 👨‍💻 Author

**Aditya Kapde**

---

## ⭐ Conclusion

This project demonstrates a **complete DevOps lifecycle**, from development to deployment using modern tools like Docker and Jenkins.

---
