from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def get_static(path):
    return send_from_directory('static', path)

# We only need this for local development.
if __name__ == '__main__':
    app.run()
