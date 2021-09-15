
pipeline {
    agent any
    stages {
        stage('Checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/mzakariabigdata/flask_app_ed'

            }
    }
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
    
        post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}