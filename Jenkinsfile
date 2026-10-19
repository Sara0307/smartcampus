
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                bat '"C:\\Users\\hafih\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" --version'
                bat '"C:\\Users\\hafih\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest --version'
            }
        }

        stage('Test Python') {
            steps {
                bat '"C:\\Users\\hafih\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest -v'
            }
        }
    }

    post {
        always {
            echo 'Execution du pipeline terminee.'
        }
    }
}
