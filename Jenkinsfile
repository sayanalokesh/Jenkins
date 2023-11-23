pipeline {
    agent any
    
    stages {
        stage('checkout') {
            steps {
                git branch: 'main', changelog: false, credentialsId: '383e4d90-dd14-41ea-b1d0-e09fce7cd3d9', poll: false, url: 'https://github.com/sayanalokesh/Jenkins.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'  // Install dependencies using pip
            }
        }
        
        stage('Test') {
            steps {
                sh 'pytest'  // Run unit tests using pytest
            }
        }
        
        stage('Deploy') {
            steps {
                // Add deployment steps to staging environment if tests pass
                sh 'python3 app.py'  // Example deployment script
            }
        }
    }
    
    post {
        success {
            mail to: 'lokesh.sayana@email.com', 
                 subject: 'Build Success', 
                 body: 'Your Jenkins build succeeded!'
        }
        failure {
            mail to: 'lokesh.sayana@email.com', 
                 subject: 'Build Failure', 
                 body: 'Your Jenkins build failed!'
        }
    }
}
