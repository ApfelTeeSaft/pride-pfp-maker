from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/pridepfp')
def serve_subroute():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/')
def main():
    return send_from_directory(os.path.join(app.root_path, 'main'), 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
