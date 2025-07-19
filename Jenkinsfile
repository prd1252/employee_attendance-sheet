pipeline {
    agent any

    environment {
        IMAGE_NAME = 'employee_attendance-app'
        CONTAINER_NAME = 'attendance-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/prd1252/employee_attendance-sheet.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Stop Previous Container') {
            steps {
                script {
                    echo "Stopping old container (if any)..."
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo "Running new container..."
                    sh "docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}"
                }
            }
        }
    }

    post {
        success {
            echo "✅ Build and container deployment successful!"
        }
        failure {
            echo "❌ Build failed!"
        }
    }
}