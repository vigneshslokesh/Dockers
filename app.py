from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!!"

@app.route('/api', methods=['GET'])
def api():
    return "This is simple API"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
