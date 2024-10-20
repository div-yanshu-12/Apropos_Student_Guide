from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import json

app = Flask(__name__, static_url_path='/static', static_folder='.')
CORS(app)  # Enable CORS

@app.route('/')
def load_events():
    return send_from_directory('.', 'events.html')

@app.route('/events.json')
def get_events():
    try:
        with open('webpages/admin/events.json') as file:
            events = json.load(file)
        return jsonify(events)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(port=11000)
