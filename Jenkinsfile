pipeline {
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/erria02/task-nest.git'
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
        stage('Run server') {
            steps {
                sh 'make run'
            }
        }
    }
}
