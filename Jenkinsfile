pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/erria02/task-nest.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'make install'
            }
        }
        stage('Make migrations') {
            steps {
                sh 'make migrate'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'make test'
            }
        }
    }
}
