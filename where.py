from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world! (Second time)", 200

# We only need this for local development.
if __name__ == '__main__':
    app.run()
