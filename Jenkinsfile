pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('python') {
            agent{
                docker {
                    image 'python'
                }

            }
            steps {
                sh 'python --version'
            }
        }
    }

}
