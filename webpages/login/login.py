from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def login_page():
    return send_from_directory('.', 'login.html')


@app.route('/login.css')
def login_css():
    return send_from_directory('.', 'login.css')

@app.route('/images/<path:filename>')
def send_image(filename):
    return send_from_directory('../../images', filename)

@app.route('/webpage')
def student_page():
    return send_from_directory('../../', 'webpage.html')

@app.route('/admin')
def admin_page():
    return send_from_directory('../admin', 'admin.html')

if __name__ == '__main__':
    app.run(port=4000)
