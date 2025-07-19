pipeline {
    agent any

    environment {
        IMAGE_NAME = 'employee_attendance-app'
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
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}").run("-p 8000:8000")
                }
            }
        }
    }
}