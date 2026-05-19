from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to my CI/CD App!</h1><p>Pipeline worked successfully.</p>"

if __name__ == '__main__':
    # هنشغله على بورت 5000
    app.run(host='0.0.0.0', port=5000)