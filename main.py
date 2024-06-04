from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/pridepfp')
def serve_subroute():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/')
def main():
    return send_from_directory(os.path.join(app.root_path, 'main'), 'index.html')

@app.route('/css/mainstyles.css')
def serve_css():
    # Serve styles.css from the 'main' subfolder
    return send_from_directory(os.path.join(app.root_path, 'main'), 'styles.css')

@app.route('/src/<path:filename>')
def serve_static(filename):
    # Serve static files from the 'src' folder
    return send_from_directory(os.path.join(app.root_path, 'src'), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
