pipeline {
    agent any

    environment {
        BACKEND_IMAGE  = "assignment-backend"
        FRONTEND_IMAGE = "assignment-frontend"
        BACKEND_PORT   = "5000"
        FRONTEND_PORT  = "8080"
        WORKSPACE_DIR  = "/workspace"
    }

    stages {

        stage('Build (Maven - Demo)') {
            steps {
                echo '>>> Simulating Maven build for demonstration purposes...'
                echo 'mvn clean package -DskipTests'
                echo '>>> Maven build stage complete.'
            }
        }

        stage('Docker Build') {
            steps {
                echo '>>> Building Backend Docker Image...'
                sh "docker build -t ${BACKEND_IMAGE} ${WORKSPACE_DIR}/backend"

                echo '>>> Building Frontend Docker Image...'
                sh "docker build -t ${FRONTEND_IMAGE} ${WORKSPACE_DIR}/frontend"
            }
        }

        stage('Run Containers') {
            steps {
                echo '>>> Stopping old containers if any...'
                sh "docker rm -f ${BACKEND_IMAGE} || true"
                sh "docker rm -f ${FRONTEND_IMAGE} || true"

                echo '>>> Starting Backend Container...'
                sh "docker run -d --name ${BACKEND_IMAGE} -p ${BACKEND_PORT}:5000 ${BACKEND_IMAGE}"

                echo '>>> Starting Frontend Container...'
                sh "docker run -d --name ${FRONTEND_IMAGE} -p ${FRONTEND_PORT}:80 ${FRONTEND_IMAGE}"

                echo '>>> Both containers are running!'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed. Backend: http://localhost:5000 | Frontend: http://localhost:8080'
        }
        failure {
            echo '❌ Pipeline failed. Check logs above.'
        }
    }
}