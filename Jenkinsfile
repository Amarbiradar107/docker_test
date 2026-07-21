pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Amarbiradar107/docker_test.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Start Grid') {
            steps {
                sh '''
                    docker compose up -d

                    echo "Waiting for Selenium Hub..."

                    until curl -s http://localhost:4444/status | grep -q "ready"
                    do
                        echo "Hub not ready..."
                        sleep 5
                    done

                    echo "Hub is ready"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker compose run automation pytest -v --html=report.html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Automation Report'
                ])
            }
        }
    }

    post {
        always {
            sh 'docker compose down'
        }
    }
}