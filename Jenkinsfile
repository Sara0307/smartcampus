pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test Python') {
            steps {
                sh '''
                    python3 --version
                    python3 -m pytest -v
                '''
            }
        }
    }
}
