# 🚀 AssignHub: Student Assignment Submission System (DevOps Project)

A modern, full-stack web application built to demonstrate a **complete CI/CD pipeline using Jenkins and Docker Compose**, wrapped in a clean and highly responsive user interface.

---

## 📌 Project Overview

**AssignHub** is a streamlined portal designed to simplify assignment management. It allows:

* **Educators** to create, edit, and delete assignments seamlessly.
* **Students** to view active tasks and submit their answers.
* **Everyone** to monitor submission counts, deadlines, and assignment statuses in real-time.

### ✨ Key Features & Recent Upgrades
* **Modern UI/UX:** A newly overhauled, aesthetically pleasing interface featuring a clean color palette, interactive stats cards, and smooth navigation.
* **Dynamic Interactivity:** Real-time search, sorting, and status-based filtering (Open vs. Overdue) without page reloads.
* **Single-Page Application (SPA) Feel:** Smooth transitions between creating assignments and viewing the master list, powered by modern vanilla JavaScript.
* **DevOps Focus:** Fully containerized architecture using Docker & Docker Compose with an automated Jenkins CI/CD pipeline.

---

## 🧱 Tech Stack

### 🔹 Backend
* **Python (Flask):** Lightweight, fast API routing.
* **Flask-CORS:** Handling cross-origin requests securely.

### 🔹 Frontend
* **HTML5, CSS3, JavaScript (Vanilla):** Custom-built, responsive UI grid system using the `Inter` font family and FontAwesome icons.
* **Nginx (Alpine):** High-performance web server containerizing the static frontend.

### 🔹 DevOps Tools
* **Docker & Docker Compose:** Orchestrating multi-container environments.
* **Jenkins:** CI/CD pipeline automation for build and deployment.

---

## 📂 Project Structure

```text
Assignment-Submission-System/
├── backend/
│   ├── app.py               # Flask application & API logic
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile           # Backend container build instructions
├── frontend/
│   ├── index.html           # Main SPA interface & logic
│   └── Dockerfile           # Nginx container build instructions
├── docker-compose.yml       # Multi-container orchestration
├── Jenkinsfile              # CI/CD Pipeline configuration
└── README.md                # Project documentation
```

---

## 🐳 Running with Docker Compose (Recommended)

Getting the project running is incredibly simple using Docker Compose.

### 1. Clone the repository
```bash
git clone https://github.com/Aditya-Kapde/Assignment-Submission-System.git
cd Assignment-Submission-System
```

### 2. Start the Application
Run the following command to build the images and start the containers in detached mode:
```bash
docker-compose up -d --build
```

### 3. Access the Application
* **Frontend UI** → http://localhost:8181
* **Backend API** → http://localhost:5000

### 4. Stop the Application
When you're done testing, you can gracefully spin down the containers:
```bash
docker-compose down
```

---

## ⚙️ Core API Endpoints

The Flask backend exposes the following RESTful endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/assignments` | Retrieve a list of all assignments |
| `POST` | `/assignments` | Create a new assignment |
| `POST` | `/assignments/{id}/submit` | Submit an answer to a specific assignment |
| `GET` | `/assignments/{id}/submissions` | View all submissions for an assignment |

*(Note: Advanced endpoints like PUT and DELETE are currently mocked in the UI and are staged for future backend implementation).*

---

## 🧪 API Testing (cURL)

You can interact with the backend directly from your terminal:

**Create an Assignment:**
```bash
curl -X POST http://localhost:5000/assignments \
-H "Content-Type: application/json" \
-d '{"title":"Math HW","description":"Solve integrals","deadline":"2026-12-31T23:59"}'
```

**Get All Assignments:**
```bash
curl http://localhost:5000/assignments
```

**Submit an Answer:**
```bash
curl -X POST http://localhost:5000/assignments/1/submit \
-H "Content-Type: application/json" \
-d '{"student_name":"Alice","answer":"The answer is 42"}'
```

**View Submissions:**
```bash
curl http://localhost:5000/assignments/1/submissions
```

---

## ⚙️ Jenkins CI/CD Pipeline

This project embraces automation to ensure code quality and rapid delivery.

### Pipeline Stages
1. **Build:** Prepares the environment and validates code.
2. **Docker Compose Build:** Assembles the latest Docker images for the frontend and backend.
3. **Run Containers:** Deploys the freshly built images to the server environment.

### Run a Local Jenkins Server (Docker)
If you want to test the pipeline locally, you can run Jenkins via Docker:
```bash
docker run -d \
  --name jenkins \
  -p 8081:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```

**Setup Instructions:**
1. Navigate to http://localhost:8081
2. Unlock Jenkins and install the suggested plugins.
3. Create a new Pipeline Job.
4. Point it to this repository or paste the provided `Jenkinsfile`.
5. Click **Build Now** to watch the deployment in action!

---

## 👨‍💻 Author

**Aditya Kapde**

---

## ⭐ Conclusion

AssignHub is more than just a task manager—it is a demonstration of bridging robust frontend user experiences with modern backend deployment strategies. It showcases a **complete DevOps lifecycle**, from development to production deployment using Docker Compose and Jenkins.
