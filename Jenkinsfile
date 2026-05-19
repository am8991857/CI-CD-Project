pipeline {
    agent any

    stages {
        // 1. مرحلة السحب من الجيت هاب
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git'
            }
        }

        // 2. مرحلة بناء البيئة وتنزيل المكتبات
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

        // 4. مرحلة الرفع والتشغيل
        stage('Deploy') {
            steps {
                echo 'Deploying Application...'
                // بنشغله في الخلفية (nohup) علشان الـ pipeline يخلص والتطبيق يفضل شغال
                sh 'nohup python app.py > log.txt 2>&1 &'
                echo 'Application deployed successfully on port 5000!'
            }
        }
    }
}