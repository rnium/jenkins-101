pipeline {
    agent {
        node {
            label 'docker-agent-alpine'
        }
    }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Starting build"
                sh '''
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
        stage("Test") {
            steps {
                echo "Testing"
                sh '''
                cd myapp
                python3 fetch.py
                '''
            }
        }
        stage("Deploy") {
            steps {
                echo "Deploying..."
                sh '''
                echo "deployed"
                '''
            }
        }
    }
}
