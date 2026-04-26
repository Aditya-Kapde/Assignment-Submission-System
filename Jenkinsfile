pipeline {
    agent any

    stages {

        stage('Build (Maven - Demo)') {
            steps {
                echo '>>> Simulating Maven build...'
            }
        }

        stage('Docker Check') {
            steps {
                bat 'docker --version'
                bat 'docker compose version'
            }
        }

        stage('Docker Compose Build') {
            steps {
                bat "docker compose -f \"%WORKSPACE%\\docker-compose.yml\" build"
            }
        }

        stage('Run Containers') {
            steps {
                bat "docker compose -f \"%WORKSPACE%\\docker-compose.yml\" down"
                bat "docker compose -f \"%WORKSPACE%\\docker-compose.yml\" up -d"
            }
        }
    }

    post {
        success {
            echo '✅ SUCCESS'
            echo 'Frontend: http://localhost:8181'
            echo 'Backend: http://localhost:5000'
        }
        failure {
            echo '❌ FAILED'
        }
    }
}