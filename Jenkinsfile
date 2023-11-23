pipeline {
    agent any
    
    stages {
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
