from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='/static', static_folder='.')

@app.route('/')
def load_webpage():
    return send_from_directory('.', 'webpage.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(port=7000)
