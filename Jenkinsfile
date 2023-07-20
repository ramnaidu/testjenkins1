pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                python3 helloworld.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
        stage('Logging'){
            parallel{
                stage('Log1'){
                    steps{
                        echo "this is log1"
                    }
                }
                stage('Log2'){
                    steps{
                        echo 'this is log2'
                    }
                }
            }
        }
    }
}
