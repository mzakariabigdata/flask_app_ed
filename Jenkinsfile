
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
                docker { image 'maven:3.3.3' }
            }
            steps {
                sh 'mvn --version'
            }
        }
    }
}