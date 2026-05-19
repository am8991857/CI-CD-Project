pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    venv/bin/pip install --upgrade pip
                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    export PYTHONPATH=.
                    venv/bin/pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    pkill -f "app.py" || true
                    nohup venv/bin/python app.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
