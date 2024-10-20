from flask import Flask, send_from_directory, request, jsonify
import json
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def admin_dashboard():
    return send_from_directory('.', 'admin2.html')

@app.route('/save_event', methods=['POST'])
def save_event():
    try:
        event_data = request.json
        file_path = os.path.join(os.path.dirname(__file__), 'events.json')
        with open(file_path, 'r+') as file:
            events = json.load(file)
            events.append(event_data)
            file.seek(0)
            json.dump(events, file, indent=4)
        return jsonify({"message": "Event saved successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/update_event', methods=['POST'])
def update_event():
    try:
        updated_event = request.json
        file_path = os.path.join(os.path.dirname(__file__), 'events.json')
        with open(file_path, 'r+') as file:
            events = json.load(file)
            for event in events:
                if event["title"] == updated_event["title"]:
                    event.update(updated_event)
            file.seek(0)
            json.dump(events, file, indent=4)
        return jsonify({"message": "Event updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete_event', methods=['POST'])
def delete_event():
    try:
        event_title = request.json.get("title")
        file_path = os.path.join(os.path.dirname(__file__), 'events.json')
        with open(file_path, 'r+') as file:
            events = json.load(file)
            events = [event for event in events if event["title"] != event_title]
            file.seek(0)
            file.truncate()
            json.dump(events, file, indent=4)
        return jsonify({"message": "Event deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_events', methods=['GET'])
def get_events():
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'events.json')
        with open(file_path, 'r') as file:
            events = json.load(file)
        return jsonify(events)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/clear_events', methods=['POST'])
def clear_events():
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'events.json')
        with open(file_path, 'w') as file:
            json.dump([], file, indent=4)
        return jsonify({"message": "All events cleared successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/admin2.css')
def admin2_css():
    return send_from_directory('.', 'admin2.css')

@app.route('/images/<path:filename>')
def send_image(filename):
    return send_from_directory('../../images', filename)

if __name__ == '__main__':
    app.run(port=10000)
