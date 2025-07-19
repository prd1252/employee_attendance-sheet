pipeline {
    agent any

    environment {
        IMAGE_NAME = 'employee-attendance-app'
        CONTAINER_NAME = 'attendance-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/prd1252/employee_attendance-sheet.git'
            }
        }

        stage('Test Docker Access') {
            steps {
                script {
                    echo "Checking Docker installation..."
                    bat 'docker --version'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    bat "docker build -t %IMAGE_NAME% ."
                }
            }
        }

        stage('Stop Previous Container') {
            steps {
                script {
                    echo "Stopping old container..."
                    bat "docker stop %CONTAINER_NAME% || exit 0"
                    bat "docker rm %CONTAINER_NAME% || exit 0"
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo "Running container..."
                    bat "docker run -d --name %CONTAINER_NAME% -p 8000:8000 %IMAGE_NAME%"
                }
            }
        }
    }

    post {
        success {
            echo "✅ Build and deployment successful!"
        }
        failure {
            echo "❌ Build failed!"
        }
    }
}
