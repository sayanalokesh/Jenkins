pipeline {
    agent any
    
    stages {
        stage('checkout') {
            steps {
                git branch: 'main', changelog: false, credentialsId: '852f6ad8-6028-4d8d-8d99-3b6194b24592', poll: false, url: 'https://github.com/sayanalokesh/Jenkins.git'
                // git branch: 'main', changelog: false, credentialsId: '383e4d90-dd14-41ea-b1d0-e09fce7cd3d9', poll: false, url: 'https://github.com/sayanalokesh/Jenkins.git'
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
                // sh 'python3 app.py'  // Example deployment script
                sh 'pip install gunicorn'
                sh 'nohup gunicorn -w 4 -b 0.0.0.0:8000 app:app > gunicorn.log 2>&1 &'
            }
        }
    }
    
    post {
        success {
            mail bcc: '', body: 'hello build is successful', cc: '', from: '', replyTo: '', subject: 'email form jenkins', to: 'stripathy95@gmail.com'
            // mail to: 'lokesh.sayana@email.com', 
            //      subject: 'Build Success', 
            //      body: 'Your Jenkins build succeeded!'
        }
        failure {
            mail bcc: '', body: 'hello build is unsuccessful', cc: '', from: '', replyTo: '', subject: 'email form jenkins', to: 'stripathy95@gmail.com'
            // mail to: 'lokesh.sayana@email.com', 
            //      subject: 'Build Failure', 
            //      body: 'Your Jenkins build failed!'
        }
    }
}
