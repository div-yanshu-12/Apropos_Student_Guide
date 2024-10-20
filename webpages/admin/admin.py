from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def admin_login():
    return send_from_directory('.', 'admin.html')

@app.route('/admin.css')
def admin_css():
    return send_from_directory('.', 'admin.css')

@app.route('/images/<path:filename>')
def send_image(filename):
    return send_from_directory('../../images', filename)

if __name__ == '__main__':
    app.run(port=9000)
