pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}

pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker { image 'python:3.5.1' }
            }
            steps {
                sh 'python --version'
            }
        }
        stage('Sonarqube') {
            agent {
                docker { image 'sonarqube' }
            }
            steps {
                sh 'ls'
            }
        }
    }
}