pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // سحب الكود من المستودع بتاعك
                git branch: 'main', url: 'https://github.com/am8991857/CI-CD-Project.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Setting up Virtual Environment and Installing dependencies...'
                sh '''
                    # التأكد من وجود venv وتجهيزها
                    python3 -m venv venv
                    # تفعيل البيئة وتسطيب المكتبات
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running Tests...'
                sh '''
                    # تفعيل البيئة وتشغيل الاختبارات جواها
                    . venv/bin/activate
                    pytest test_app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                sh '''
                    # 1. لو التطبيق شغال القديم شغال، بنقفل البورت الأول عشان ميعملش Conflict
                    fuser -k 5000/tcp || true
                    
                    # 2. تشغيل التطبيق في الخلفية ومنع جينكنز من قتله
                    . venv/bin/activate
                    export JENKINS_NODE_COOKIE=dontKillMe
                    nohup python app.py > log.txt 2>&1 &
                '''
                echo 'Application deployed successfully on port 5000!'
            }
        }
    }
}
