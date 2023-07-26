pipeline {
    agent any
    parameters {
        string(name: 'tag', defaultValue: '', description: 'Tag to build')
        choice(choices: ['dev', 'test', 'staging', 'qastaging', 'security', 'performance', 'uat', "exploratory", 'pre-production', 'production'],description: 'Run Test on which environment?', name: 'environment')
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                pip3 install -r requirements.txt
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
            when {
                expression { params.environment == 'qastaging' }
            }
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
