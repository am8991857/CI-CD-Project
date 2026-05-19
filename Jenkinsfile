pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/am8991857/CI-CD-Project.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        // 3. مرحلة الاختبار
        stage('Test') {
            steps {
                echo 'Running Tests...'
                sh 'pytest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                sh 'nohup python app.py > log.txt 2>&1 &'
                echo 'Application deployed successfully on port 5000!'
            }
        }
    }
}
