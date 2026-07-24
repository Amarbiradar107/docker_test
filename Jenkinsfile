pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: ['smoke', 'regression', 'sanity', 'api', 'all'],
            description: 'Select Test Suite'
        )
    }

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
                sh 'docker compose run automation pytest -m ${params.TEST_SUITE} --html=reports/report.html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, icon: '', keepAll: false, reportDir: 'reports', reportFiles: 'report.html', reportName: 'HTML Report', reportTitles: '', useWrapperFileDirectly: true])
            }
        }
    }

    post {
        always {
            sh 'docker compose down'
        }
    }
}