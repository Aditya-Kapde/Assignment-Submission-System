pipeline {
    agent any

    environment {
        WORKSPACE_DIR = "${WORKSPACE}"
    }

    stages {

        stage('Build (Maven - Demo)') {
            steps {
                echo '>>> Simulating Maven build for demonstration purposes...'
                echo 'mvn clean package -DskipTests'
                echo '>>> Maven build stage complete.'
            }
        }

        stage('Docker Compose Build') {
            steps {
                echo '>>> Building Docker images with docker-compose...'
                sh 'docker-compose -f ${WORKSPACE}/docker-compose.yml build'
                echo '>>> Build complete.'
            }
        }

        stage('Run Containers') {
            steps {
                echo '>>> Stopping existing containers if running...'
                sh 'docker-compose -f ${WORKSPACE}/docker-compose.yml down || true'

                echo '>>> Starting all containers with docker-compose...'
                sh 'docker-compose -f ${WORKSPACE}/docker-compose.yml up -d'

                echo '>>> All containers are running!'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
            echo 'Backend API: http://localhost:5000'
            echo 'Frontend UI: http://localhost:8080'
        }
        failure {
            echo '❌ Pipeline failed. Check the logs above for details.'
        }
    }
}
